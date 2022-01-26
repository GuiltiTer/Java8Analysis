from unittest import TestCase
from src.data_structures.graph.networkx_builder import NxDiGraphBuilder
import networkx


class TestNxDiGraphBuilder(TestCase):

    @staticmethod
    def dummy_graph():
        nodes = [
            (0, ["zero"]),
            (1, ["one"]),
            (2, ["two"]),
            (3, ["three"])
        ]
        edges = [
            (0, 1, "true"),
            (0, 2, "False"),
            (1, 3),
            (2, 3)
        ]
        return (NxDiGraphBuilder()
                .add_nodes_from(nodes)
                .add_edges_from(edges))

    def test_new(self):
        builder = NxDiGraphBuilder()
        self.assertEqual(set(), set(builder.node_keys))
        self.assertEqual(set(), set(builder.node_values))
        self.assertEqual(set(), set(builder.node_keys))
        self.assertEqual(set(), set(builder.node_values))

    def test_build(self):
        self.assertIsInstance(NxDiGraphBuilder().build(), networkx.DiGraph)

    def test_add_node(self):
        builder = NxDiGraphBuilder()
        builder.add_node(1, "x")
        self.assertEqual({1}, set(builder.node_keys))
        self.assertIn("x", list(builder.node_values))
        self.assertIn((1, "x"), set(builder.node_items))

    def test_remove_node(self):
        builder = self.dummy_graph()
        nodes = list(builder.node_keys)
        for node in nodes:
            builder.remove_node(node)
            self.assertNotIn(node, set(builder.node_keys))

    def test_head(self):
        builder = self.dummy_graph()
        self.assertEqual(0, builder.head)

    def test_last(self):
        builder = self.dummy_graph()
        self.assertEqual(3, builder.last)

    def test_add_edge(self):
        builder = (NxDiGraphBuilder()
                   .add_edge(1, 2, value="true")
                   .add_edge(2, 3, value="false"))

        self.assertEqual({1, 2, 3}, set(builder.node_keys))
        self.assertEqual({(1, 2), (2, 3)}, set(builder.edge_keys))
        self.assertEqual({((1, 2), "true"), ((2, 3), "false")},
                         set(builder.edge_items))

    def test_remove_edge(self):
        builder = self.dummy_graph()
        builder.remove_edge(0, 1)
        self.assertNotIn((0, 1), set(builder.edge_keys))

    def test_add_node_from(self):
        nodes = [
            (0, ["zero"]),
            (1, ["one"]),
        ]
        builder = NxDiGraphBuilder().add_nodes_from(nodes)
        self.assertEqual(nodes, list(builder.node_items))

    def test_compose(self):
        left = NxDiGraphBuilder().add_nodes_from([(0, ["zero"]), (1, ["one"])])
        right = NxDiGraphBuilder().add_nodes_from([(1, ["zero"]), (2, ["one"])])
        composed = left | right
        print(composed)
