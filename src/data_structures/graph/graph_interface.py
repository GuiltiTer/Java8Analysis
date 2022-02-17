import abc
from typing import List, Tuple, Any, Dict, Union, Iterable


class IGraph(metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def node_keys(self) -> Iterable[int]:
        """get nodes"""

    @property
    @abc.abstractmethod
    def node_values(self) -> Iterable:
        """get nodes content"""

    @property
    @abc.abstractmethod
    def node_items(self) -> Iterable:
        """get graph node items"""

    @property
    @abc.abstractmethod
    def edge_keys(self) -> Iterable[Tuple[int, int]]:
        """get edges"""

    @property
    @abc.abstractmethod
    def edge_values(self) -> Iterable:
        """get edges content"""

    @property
    @abc.abstractmethod
    def edge_items(self) -> Iterable:
        """get graph edge items"""

    @property
    @abc.abstractmethod
    def head(self) -> int:
        """get the head node"""

    @property
    @abc.abstractmethod
    def last(self) -> int:
        """get the last node"""

    @abc.abstractmethod
    def successors(self, node: int):
        """successors of a given node"""

    @abc.abstractmethod
    def predecessors(self, node: int):
        """predecessors of a given node"""

    @abc.abstractmethod
    def add_node(self, node: int, value: Any = None) -> "IGraph":
        """add a node"""

    @abc.abstractmethod
    def remove_node(self, node: int) -> "IGraph":
        """remove a node"""

    @abc.abstractmethod
    def add_nodes_from(self, nodes: List) -> "IGraph":
        """add a set of nodes"""

    @abc.abstractmethod
    def remove_nodes_from(self, nodes: List) -> "IGraph":
        """remove a set of nodes"""

    @abc.abstractmethod
    def add_edge(self, f: int, t: int, value: Any = None) -> "IGraph":
        """add an edge"""

    @abc.abstractmethod
    def remove_edge(self, f: int, t: int) -> "IGraph":
        """remove an edge"""

    @abc.abstractmethod
    def add_edges_from(self, edges: List) -> "IGraph":
        """add a set of edges"""

    @abc.abstractmethod
    def remove_edges_from(self, edges: List) -> "IGraph":
        """remove a set of edges"""

    @abc.abstractmethod
    def compose(self, graph: "IGraph") -> None:
        """compose (union) with a graph"""

    @abc.abstractmethod
    def reset_node_order(self) -> None:
        """reset node labels from zero"""

    @abc.abstractmethod
    def build(self):
        """build graph"""

    @abc.abstractmethod
    def as_dict(self) -> Dict:
        """get a dictionary presentation of graph"""

    @abc.abstractmethod
    def copy(self) -> "IGraph":
        """return a deep copy of object"""

    @abc.abstractmethod
    def reversed(self):
        """return a reversed view of graph"""

    def __or__(self, other: "IGraph") -> "IGraph":
        """compose graphs and merge graph data"""

    @abc.abstractmethod
    def __rshift__(self, n: int) -> "IGraph":
        """shift right the nodes"""

    @abc.abstractmethod
    def __getitem__(self, item: Union[int, Tuple]):
        """get content of a node"""

    @abc.abstractmethod
    def __setitem__(self, item: Union[int, Tuple], content: Any):
        """set content of a node"""

    @abc.abstractmethod
    def __len__(self):
        """number of nodes"""
