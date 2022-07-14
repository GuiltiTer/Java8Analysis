from typing import List

from antlr4 import RuleContext
from itertools import accumulate
from src.cfg_extractor.language_structure.structure_pattern_interface import ILanguagePattern
from src.data_structures.graph.builder_interface import IDiGraphBuilder
from src.data_structures.graph.networkx_builder import NxDiGraphBuilder as DiGraphBuilder
from enum import Enum, auto
from src.antlr.rule_utils import is_break, is_return, is_continue, is_throw


class EdgeLabel(Enum):
    false = auto()
    true = auto()


class DiGraphEmbedder(ILanguagePattern):

    @classmethod
    def concat(cls, left: IDiGraphBuilder, right: IDiGraphBuilder) -> IDiGraphBuilder:
        right = right >> len(left)

        g = (DiGraphBuilder()
             .add_nodes_from([(left.last, []), (right.head, [])])
             .add_edge(left.last, right.head))
        return g | left | right

    @classmethod
    def merge(cls, left: IDiGraphBuilder, right: IDiGraphBuilder) -> IDiGraphBuilder:
        right = right >> len(left) - 1
        return left | right

    @classmethod
    def embed_in_if(cls, condition: RuleContext, then_part: "IDiGraphBuilder"):
        g_head = 0
        g = DiGraphBuilder().add_node(g_head, value=[condition])
        then_part = then_part >> len(g)
        g_last = then_part.last + 1
        g.add_node(g_last, value=[])
        g = g | then_part
        return g.add_edges_from([(g_head, g_last, EdgeLabel.false.name),
                                 (g_head, then_part.head, EdgeLabel.true.name),
                                 (then_part.last, g_last)])

    @classmethod
    def embed_in_if_else(cls, condition: RuleContext, then_part: "IDiGraphBuilder", else_part: "IDiGraphBuilder"):
        g_head = 0
        g = DiGraphBuilder().add_node(g_head, value=[condition])
        then_part = then_part >> len(g)
        else_part = else_part >> len(g) + len(then_part)
        g_last = else_part.last + 1
        g = g | then_part | else_part
        g.add_node(g_last, value=[])
        return g.add_edges_from([(g_head, else_part.head, EdgeLabel.false.name),
                                 (g_head, then_part.head, EdgeLabel.true.name),
                                 (then_part.last, g_last),
                                 (else_part.last, g_last)])

    @classmethod
    def embed_in_switch_case(cls, switcher: RuleContext, labels: List[RuleContext], bodies: List["IDiGraphBuilder"]):
        g_head = 0
        start = 1
        shifted_bodies = []
        g = DiGraphBuilder().add_node(g_head, value=[switcher] if switcher else [])
        # accumulated_lengths = list((body >> start).last for body in bodies)
        # bodies = [body >> s + len(g)for body, s in zip(bodies, accumulated_lengths)]
        for i in range(len(bodies)):
            shifted_bodies.append(bodies[i] >> start)
            start = shifted_bodies[i].last + 1
        g_last = shifted_bodies[-1].last + 1
        for bodies_object in shifted_bodies:
            g = g | bodies_object
        g.add_node(g_last, value=[])
        g.add_edges_from([(g_head, body.head, label.getText() if label else []) for label, body in zip(labels, shifted_bodies)])
        g.add_edges_from([(body.last, body.last + 1) for label, body in zip(labels, shifted_bodies)])
        return cls.__split_on_break(g)

    @classmethod
    def embed_in_while(cls, condition: RuleContext, body: "IDiGraphBuilder"):
        g_head, g_condition = 0, 1
        g = DiGraphBuilder().add_nodes_from([(g_head, []),
                                             (g_condition, [condition])])
        body = body >> len(g)
        g_last = body.last + 1
        g.add_node(g_last, value=[])
        g = g | body
        g.add_edges_from([(g_head, g_condition),
                          (g_condition, body.head, EdgeLabel.true.name),
                          (g_condition, g_last, EdgeLabel.false.name),
                          (body.last, g_condition)])
        g = cls.__split_on_continue(g, g_condition)
        return cls.__split_on_break(g)

    @classmethod
    def embed_in_do_while(cls, condition: RuleContext, body: "IDiGraphBuilder"):
        g_head = 0
        g = DiGraphBuilder().add_node(g_head, [])
        body = body >> len(g)
        g_condition = body.last + 1
        g_last = g_condition + 1
        g.add_nodes_from([(g_condition, [condition]),
                          (g_last, [])])
        g = g | body
        g.add_edges_from([(g_head, body.head),
                          (body.last, g_condition),
                          (g_condition, body.head, EdgeLabel.true.name),
                          (g_condition, g_last, EdgeLabel.false.name)])
        g = cls.__split_on_continue(g, g_condition)
        return cls.__split_on_break(g)

    @classmethod
    def embed_in_for(cls,
                     condition,
                     initializer: RuleContext,
                     successor: IDiGraphBuilder,
                     body: RuleContext) -> IDiGraphBuilder:
        g = (cls.__embed_in_conditional_for(condition, initializer, successor, body) if condition
             else cls.__embed_in_unconditional_for(initializer, successor, body))
        return cls.__split_on_break(g)

    @classmethod
    def __embed_in_conditional_for(cls,
                                   condition: RuleContext,
                                   initializer: RuleContext,
                                   successor: RuleContext,
                                   body: IDiGraphBuilder) -> IDiGraphBuilder:

        g_head, g_condition = 0, 1
        g = DiGraphBuilder().add_nodes_from([(g_head, [initializer]),
                                             (g_condition, [condition])])
        body = body >> len(g)
        g_successor = body.last + 1
        g_last = g_successor + 1
        g.add_nodes_from([(g_last, []), (g_successor, [successor] if successor else [])])
        g = g | body
        g.add_edges_from([(g_head, g_condition), (g_condition, body.head, EdgeLabel.true.name),
                          (g_condition, g_last, EdgeLabel.false.name), (body.last, g_successor),
                          (g_successor, g_condition)])
        return cls.__split_on_continue(g, g_successor)

    @classmethod
    def __embed_in_unconditional_for(cls,
                                     initializer: RuleContext,
                                     successor: RuleContext,
                                     body: IDiGraphBuilder) -> IDiGraphBuilder:
        g_head = 0
        g = DiGraphBuilder().add_node(g_head, [initializer] if initializer else [])
        body = body >> len(g)
        g_successor = body.last + 1
        g_last = g_successor + 1
        g.add_nodes_from([(g_last, []), (g_successor, [successor] if successor else [])])
        g = g | body
        g.add_edges_from([(g_head, body.head),
                          (body.last, g_successor),
                          (g_successor, body.head)])
        return cls.__split_on_continue(g, g_successor)

    @classmethod
    def embed_in_try_catch(cls,
                           try_body: "IDiGraphBuilder",
                           exceptions: List[RuleContext],
                           catch_bodies: List["IDiGraphBuilder"]):
        g_head = 0
        g = DiGraphBuilder().add_node(g_head, try_body.head)
        accumulated_lengths = list(accumulate(len(body) for body in catch_bodies))
        catch_bodies = [body >> s + len(try_body) for body, s in zip(catch_bodies, accumulated_lengths)]
        g = g | try_body
        for label, data in g.node_items:
            for ctx in data:
                if is_throw(ctx):
                    g = g | catch_bodies[0]
                    g.remove_edges_from([(label, successor) for successor in g.successors(label)])
                    g_last = len(g) + 1
                    g.add_node(g_last, value=[]).add_edges_from([(label, g.last), (g.last, g_last)])
                    g[label] = data[:data.index(ctx)]
                    break
        return g

    @classmethod
    def __resolve_null_node(cls, graph: IDiGraphBuilder, body):
        null_nodes = []
        for label, data in graph.node_items:
            info = {"label": None, "predecessors": [], "successor": []}
            if not data:
                info['label'] = label
                for edge in graph.as_dict()['edges']:
                    if edge[0][0] == label:
                        info['successor'].append(edge[0][1])
                    elif edge[0][1] == label:
                        info['predecessors'].append((edge[0][0], edge[1] if edge[1] else []))

            if info["label"] is not None:
                null_nodes.append(info)

        for node in null_nodes:
            if node["label"] != graph.last:
                for p in node['predecessors']:
                    graph.add_edges_from([(p[0], s, p[1]) for s in node['successor']])
                graph.remove_node(node['label'])

        graph.reset_node_order()

        return graph

    @classmethod
    def embed_in_function(cls, body: "IDiGraphBuilder"):
        g = DiGraphBuilder()
        g = g | body
        g = cls.__split_on_return(g)
        return cls.__resolve_null_node(g, body)

    @classmethod
    def __split_on_return(cls, graph: IDiGraphBuilder):
        return cls.__direct_nodes_to_if(graph, graph.last, is_return)

    @classmethod
    def __split_on_continue(cls, graph: "IDiGraphBuilder", direction_reference):
        return cls.__direct_nodes_to_if(graph, direction_reference, is_continue)

    @classmethod
    def __split_on_break(cls, graph: "IDiGraphBuilder"):
        return cls.__direct_nodes_to_if(graph, graph.last, is_break)

    @classmethod
    def __split_on_throw(cls, graph: "IDiGraphBuilder", direction_reference):
        return cls.__direct_nodes_to_if(graph, direction_reference, is_throw)

    @classmethod
    def __direct_nodes_to_if(cls,
                             graph: "IDiGraphBuilder",
                             target_node,
                             jump_statement):
        h = graph.copy()
        for label, data in graph.node_items:
            for ctx in data:
                if jump_statement(ctx):
                    h.remove_edges_from([(label, successor) for successor in graph.successors(label)])
                    h.add_edge(label, target_node)
                    h[label] = data[:data.index(ctx)]
                    break
        return h
