import abc
from typing import List

from src.antlr.gen.JavaParser import RuleContext
from src.data_structures.graph.graph_interface import IGraph


class ILanguagePattern(metaclass=abc.ABCMeta):

    @classmethod
    @abc.abstractmethod
    def concat(cls,
               left: IGraph,
               right: IGraph) -> IGraph:
        """concatenate two graphs sequentially"""

    @classmethod
    @abc.abstractmethod
    def merge(cls,
              left: IGraph,
              right: IGraph) -> IGraph:
        """merge two graphs affront nodes"""

    @classmethod
    @abc.abstractmethod
    def embed_in_if(cls,
                    condition: RuleContext,
                    then_part: IGraph) -> IGraph:
        """embed the then part graph into an if graph pattern"""

    @classmethod
    @abc.abstractmethod
    def embed_in_if_else(cls,
                         condition: RuleContext,
                         then_part: IGraph,
                         else_part: IGraph) -> IGraph:
        """embed the then part and else part graphs into an if-else graph pattern"""

    @classmethod
    @abc.abstractmethod
    def embed_in_switch_case(cls,
                             switcher: RuleContext,
                             labels: List[RuleContext],
                             bodies: List[IGraph]) -> IGraph:
        """embed the body graphs into a switch-case graph pattern"""

    @classmethod
    @abc.abstractmethod
    def embed_in_while(cls,
                       condition: RuleContext,
                       body: IGraph) -> IGraph:
        """embed the body graph into a while graph pattern"""

    @classmethod
    @abc.abstractmethod
    def embed_in_do_while(cls,
                          condition: RuleContext,
                          body: IGraph) -> IGraph:
        """embed the body graph into a do-while graph pattern"""

    @classmethod
    @abc.abstractmethod
    def embed_in_for(cls,
                     condition: RuleContext,
                     initializer: RuleContext,
                     successor: RuleContext,
                     body: IGraph) -> IGraph:
        """embed the body graph into a for graph pattern"""

    @classmethod
    @abc.abstractmethod
    def embed_in_try_catch(cls,
                           try_body: IGraph,
                           exceptions: List[RuleContext],
                           catch_bodies: List[IGraph]) -> IGraph:
        """embed the body and catch graphs into a try-catch graph pattern"""

    @classmethod
    @abc.abstractmethod
    def embed_in_function(cls,
                          body: IGraph) -> IGraph:
        """embed the body graph into a function graph pattern"""
