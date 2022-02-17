from functools import reduce, cached_property
from typing import Dict

from data_structures.graph.networkx_builder import NxDiGraphBuilder as DigraphBuilder


class DominantTree:
    def __init__(self, cfg: DigraphBuilder):
        self.__cfg = cfg

    @cached_property
    def dominant_tree(self) -> DigraphBuilder:
        return self.__build_dominant_tree(self.__cfg)

    @cached_property
    def post_dominant_tree(self) -> DigraphBuilder:
        return self.__build_dominant_tree(self.__cfg.reversed())

    @classmethod
    def __build_dominant_tree(cls, cfg: DigraphBuilder) -> DigraphBuilder:
        g = DigraphBuilder()
        dominants = cls.get_dominants(cfg)
        dominants = {n: doms - {n} for n, doms in dominants.items()}
        q = [cfg.head]
        while len(q) != 0:
            m = q[0]
            q = q[1:]
            for node in cfg.node_keys:
                if len(dominants[node]) == 0:
                    continue

                dominants[node] -= {m}
                if len(dominants[node]) == 0:
                    g.add_edge(m, node)
                    q.append(node)
        return g

    @classmethod
    def get_dominants(cls, cfg: DigraphBuilder) -> Dict[int, set]:
        dominants = {cfg.head: {cfg.head}}
        other_than_head = set(cfg.node_keys) - {cfg.head}
        dominants.update({node: set(cfg.node_keys) for node in other_than_head})

        changed = True
        while changed:
            changed = False
            for node in other_than_head:
                dom_of_preds = map(dominants.__getitem__, cfg.predecessors(node))
                new_dom = {node}.union(reduce(set.intersection, dom_of_preds))
                changed = new_dom != dominants[node] or changed
                dominants[node] = new_dom

        return dominants
