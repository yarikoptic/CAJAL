from _typeshed import Incomplete
from collections.abc import Generator

def dijkstra_path(G, source, target, weight: str = ...): ...
def dijkstra_path_length(G, source, target, weight: str = ...): ...
def single_source_dijkstra_path(G, source, cutoff: Incomplete | None = ..., weight: str = ...): ...
def single_source_dijkstra_path_length(G, source, cutoff: Incomplete | None = ..., weight: str = ...): ...
def single_source_dijkstra(G, source, target: Incomplete | None = ..., cutoff: Incomplete | None = ..., weight: str = ...): ...
def multi_source_dijkstra_path(G, sources, cutoff: Incomplete | None = ..., weight: str = ...): ...
def multi_source_dijkstra_path_length(G, sources, cutoff: Incomplete | None = ..., weight: str = ...): ...
def multi_source_dijkstra(G, sources, target: Incomplete | None = ..., cutoff: Incomplete | None = ..., weight: str = ...): ...
def dijkstra_predecessor_and_distance(G, source, cutoff: Incomplete | None = ..., weight: str = ...): ...
def all_pairs_dijkstra(G, cutoff: Incomplete | None = ..., weight: str = ...) -> Generator[Incomplete, None, None]: ...
def all_pairs_dijkstra_path_length(G, cutoff: Incomplete | None = ..., weight: str = ...) -> Generator[Incomplete, None, None]: ...
def all_pairs_dijkstra_path(G, cutoff: Incomplete | None = ..., weight: str = ...) -> Generator[Incomplete, None, None]: ...
def bellman_ford_predecessor_and_distance(G, source, target: Incomplete | None = ..., weight: str = ..., heuristic: bool = ...): ...
def bellman_ford_path(G, source, target, weight: str = ...): ...
def bellman_ford_path_length(G, source, target, weight: str = ...): ...
def single_source_bellman_ford_path(G, source, weight: str = ...): ...
def single_source_bellman_ford_path_length(G, source, weight: str = ...): ...
def single_source_bellman_ford(G, source, target: Incomplete | None = ..., weight: str = ...): ...
def all_pairs_bellman_ford_path_length(G, weight: str = ...) -> Generator[Incomplete, None, None]: ...
def all_pairs_bellman_ford_path(G, weight: str = ...) -> Generator[Incomplete, None, None]: ...
def goldberg_radzik(G, source, weight: str = ...): ...
def negative_edge_cycle(G, weight: str = ..., heuristic: bool = ...): ...
def find_negative_cycle(G, source, weight: str = ...): ...
def bidirectional_dijkstra(G, source, target, weight: str = ...): ...
def johnson(G, weight: str = ...): ...
