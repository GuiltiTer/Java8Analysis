from typing import List

from antlr4 import RuleContext

from src.cfg_extractor.language_structure.structure_pattern_interface import ILanguagePattern
from src.data_structures.graph.builder_interface import IDiGraphBuilder
from src.data_structures.graph.networkx_builder import NxDiGraphBuilder as DiGraphBuilder
from enum import Enum, auto


class EdgeLabel(Enum):
    false = auto()
    true = auto()


class DiGraphEmbedder(ILanguagePattern):

    @staticmethod
    def concat(left: IDiGraphBuilder, right: IDiGraphBuilder) -> IDiGraphBuilder:
        right = right >> len(left)

        g = (DiGraphBuilder()
             .add_nodes_from([(left.last, []), (right.head, [])])
             .add_edge(left.last, right.head))
        return g | left | right

    @staticmethod
    def merge(left: IDiGraphBuilder, right: IDiGraphBuilder) -> IDiGraphBuilder:
        right = right >> len(left) - 1
        return left | right

    @staticmethod
    def embed_in_if(condition: RuleContext, then_part: "IDiGraphBuilder"):
        g_head = 0
        g = DiGraphBuilder().add_node(g_head, value=[condition])
        then_part = then_part >> len(g)
        g_last = then_part.last + 1
        g.add_node(g_last, value=[])
        g = g | then_part
        return g.add_edges_from([(g_head, g_last, EdgeLabel.false.name),
                                 (g_head, then_part.head, EdgeLabel.true.name),
                                 (then_part.last, g_last)])

    @staticmethod
    def embed_in_if_else(condition: RuleContext, then_part: "IDiGraphBuilder", else_part: "IDiGraphBuilder"):
        g_head = 0
        g = DiGraphBuilder().add_node(g_head, value=[condition])
        then_part = then_part >> len(g)
        else_part = else_part >> len(g) + len(then_part)
        g_last = else_part.last + 1
        g.add_node(g_last, value=[])
        g = g | then_part | else_part
        return g.add_edges_from([(g_head, else_part.head, EdgeLabel.false.name),
                                 (g_head, then_part.head, EdgeLabel.true.name),
                                 (then_part.last, g_last),
                                 (else_part.last, g_last)])

    @staticmethod
    def embed_in_switch_case(switcher: RuleContext, labels: List[RuleContext], bodies: List["IDiGraphBuilder"]):
        pass

    @staticmethod
    def embed_in_while(condition: RuleContext, body: "IDiGraphBuilder"):
        g_head, g_condition = 0, 1
        g = DiGraphBuilder().add_nodes_from([(g_head, []),
                                             (g_condition, [condition])])
        body = body >> len(g)
        g_last = body.last + 1
        g.add_node(g_last, value=[])
        g = g | body
        return g.add_edges_from([(g_head, g_condition),
                                 (g_condition, body.head, EdgeLabel.true.name),
                                 (g_condition, g_last, EdgeLabel.false.name),
                                 (body.last, g_condition)])

    @staticmethod
    def embed_in_do_while(condition: RuleContext, body: "IDiGraphBuilder"):
        g_head = 0
        g = DiGraphBuilder().add_node(g_head, [])
        body = body >> len(g)
        g_condition = body.last + 1
        g_last = g_condition + 1
        g.add_nodes_from([(g_condition, [condition]),
                          (g_last, [])])
        g = g | body
        return g.add_edges_from([(g_head, body.head),
                                 (body.last, g_condition),
                                 (g_condition, body.head, EdgeLabel.true.name),
                                 (g_condition, g_last, EdgeLabel.false.name)])

    @staticmethod
    def embed_in_for(condition: RuleContext,
                     initializer: RuleContext,
                     body: IDiGraphBuilder,
                     successor: RuleContext) -> IDiGraphBuilder:
        if condition:
            g = DiGraphEmbedder.embed_in_conditional_for(condition, initializer, body, successor)
        else:
            g = DiGraphEmbedder.embed_in_unconditional_for(initializer, body, successor)

        return g

    @staticmethod
    def embed_in_conditional_for(condition: RuleContext,
                                 initializer: RuleContext,
                                 body: IDiGraphBuilder,
                                 successor: RuleContext) -> IDiGraphBuilder:

        g_head, g_condition = 0, 1
        g = DiGraphBuilder().add_nodes_from([(g_head, [initializer]),
                                             (g_condition, [condition])])
        body = body >> len(g)
        g_successor = body.last + 1
        g_last = g_successor + 1
        g.add_nodes_from([(g_last, []), (g_successor, [successor] if successor else [])])
        g = g | body

        return g.add_edges_from([(g_head, g_condition), (g_condition, body.head, EdgeLabel.true.name),
                                 (g_condition, g_last, EdgeLabel.false.name), (body.last, g_successor),
                                 (g_successor, g_condition)])

    @staticmethod
    def embed_in_unconditional_for(initializer: RuleContext,
                                   body: IDiGraphBuilder,
                                   successor: RuleContext) -> IDiGraphBuilder:
        g_head = 0
        g = DiGraphBuilder().add_node(g_head, [initializer] if initializer else [])
        body = body >> len(g)
        g_succsessor = body.last + 1
        g_last = g_succsessor + 1
        g.add_nodes_from([(g_last, []), (g_succsessor, [successor] if successor else [])])
        g = g | body
        return g.add_edges_from([(g_head, body.head),
                                 (body.last, g_succsessor),
                                 (g_succsessor, body.head)])

    @staticmethod
    def embed_in_try_catch(body: "IDiGraphBuilder", exceptions: List[RuleContext],
                           catch_bodies: List["IDiGraphBuilder"]):
        pass

    @staticmethod
    def embed_in_function(body: "IDiGraphBuilder"):
        # todo: return and resolve null nodes
        end = body.last + 1
        g = DiGraphBuilder()
        g = g | body
        return (g
                .add_node(end, value=[])
                .add_edge(body.last, end))
