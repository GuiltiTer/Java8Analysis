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
    def embed_in_if(condition: RuleContext, then_part: "IDiGraphBuilder"):
        g = DiGraphBuilder()
        g_head = 0
        g.add_node(g_head, value=[condition])
        then_part = then_part >> len(g)
        g_last = then_part.last + 1
        g.add_node(g_last, value=[])
        g = g | then_part
        return g.add_edges_from([(g_head, g_last, EdgeLabel.false.name),
                                 (g_head, then_part.head, EdgeLabel.true.name),
                                 (then_part.last, g_last)])

    @staticmethod
    def embed_in_if_else(condition: RuleContext, then_part: "IDiGraphBuilder", else_part: "IDiGraphBuilder"):
        pass

    @staticmethod
    def embed_in_switch_case(switcher: RuleContext, labels: List[RuleContext], bodies: List["IDiGraphBuilder"]):
        pass

    @staticmethod
    def embed_in_while(condition: RuleContext, body: "IDiGraphBuilder"):
        pass

    @staticmethod
    def embed_in_do_while(condition: RuleContext, body: "IDiGraphBuilder"):
        pass

    @staticmethod
    def embed_in_for(condition: RuleContext, body: "IDiGraphBuilder"):
        pass

    @staticmethod
    def embed_in_try_catch(body: "IDiGraphBuilder", exceptions: List[RuleContext],
                           catch_bodies: List["IDiGraphBuilder"]):
        pass

    @staticmethod
    def embed_in_function(body: "IDiGraphBuilder"):
        # todo: return and resolve null nodes
        g = DiGraphBuilder()
        end = body.last + 1
        g = g | body
        return (g
                .add_node(end, value=[])
                .add_edge(body.last, end))
