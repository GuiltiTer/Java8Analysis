import abc
from typing import List

from src.antlr.gen.JavaParser import RuleContext
from src.data_structures.graph.builder_interface import IDiGraphBuilder


class ILanguagePattern(metaclass=abc.ABCMeta):

    @staticmethod
    @abc.abstractmethod
    def concat(left: IDiGraphBuilder,
               right: IDiGraphBuilder) -> IDiGraphBuilder:
        """concatenate two graphs sequentially"""

    @staticmethod
    @abc.abstractmethod
    def merge(left: IDiGraphBuilder,
              right: IDiGraphBuilder) -> IDiGraphBuilder:
        """merge two graphs affront nodes"""

    @staticmethod
    @abc.abstractmethod
    def embed_in_if(condition: RuleContext,
                    then_part: IDiGraphBuilder) -> IDiGraphBuilder:
        """embed the then part graph into an if graph pattern"""

    @staticmethod
    @abc.abstractmethod
    def embed_in_if_else(condition: RuleContext,
                         then_part: IDiGraphBuilder,
                         else_part: IDiGraphBuilder) -> IDiGraphBuilder:
        """embed the then part and else part graphs into an if-else graph pattern"""

    @staticmethod
    @abc.abstractmethod
    def embed_in_switch_case(switcher: RuleContext,
                             labels: List[RuleContext],
                             bodies: List[IDiGraphBuilder]) -> IDiGraphBuilder:
        """embed the body graphs into a switch-case graph pattern"""

    @staticmethod
    @abc.abstractmethod
    def embed_in_while(condition: RuleContext,
                       body: IDiGraphBuilder) -> IDiGraphBuilder:
        """embed the body graph into a while graph pattern"""

    @staticmethod
    @abc.abstractmethod
    def embed_in_do_while(condition: RuleContext,
                          body: IDiGraphBuilder) -> IDiGraphBuilder:
        """embed the body graph into a do-while graph pattern"""

    @staticmethod
    @abc.abstractmethod
    def embed_in_for(condition: RuleContext,
                     body: IDiGraphBuilder) -> IDiGraphBuilder:
        """embed the body graph into a for graph pattern"""

    @staticmethod
    @abc.abstractmethod
    def embed_in_try_catch(body: IDiGraphBuilder,
                           exceptions: List[RuleContext],
                           catch_bodies: List[IDiGraphBuilder]) -> IDiGraphBuilder:
        """embed the body and catch graphs into a try-catch graph pattern"""

    @staticmethod
    @abc.abstractmethod
    def embed_in_function(body: IDiGraphBuilder) -> IDiGraphBuilder:
        """embed the body graph into a function graph pattern"""
