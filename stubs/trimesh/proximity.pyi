from . import util as util
from .constants import log_time as log_time, tol as tol
from .exceptions import closure as closure
from .grouping import group_min as group_min
from .triangles import points_to_barycentric as points_to_barycentric
from _typeshed import Incomplete

def nearby_faces(mesh, points): ...
def closest_point_naive(mesh, points): ...
def closest_point(mesh, points): ...
def signed_distance(mesh, points): ...

class NearestQueryResult:
    nearest: Incomplete
    distances: Incomplete
    normals: Incomplete
    triangle_indices: Incomplete
    barycentric_coordinates: Incomplete
    interpolated_normals: Incomplete
    vertex_indices: Incomplete
    def __init__(self) -> None: ...
    def has_normals(self): ...

class ProximityQuery:
    def __init__(self, mesh) -> None: ...
    def on_surface(self, points): ...
    def vertex(self, points): ...
    def signed_distance(self, points): ...

def longest_ray(mesh, points, directions): ...
def max_tangent_sphere(mesh, points, inwards: bool = ..., normals: Incomplete | None = ..., threshold: float = ..., max_iter: int = ...): ...
def thickness(mesh, points, exterior: bool = ..., normals: Incomplete | None = ..., method: str = ...): ...
