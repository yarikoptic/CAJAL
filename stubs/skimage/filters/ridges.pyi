from .._shared.utils import check_nD as check_nD
from ..feature.corner import hessian_matrix as hessian_matrix, hessian_matrix_eigvals as hessian_matrix_eigvals
from ..util import img_as_float as img_as_float, invert as invert
from _typeshed import Incomplete

def compute_hessian_eigenvalues(image, sigma, sorting: str = ..., mode: str = ..., cval: int = ...): ...
def meijering(image, sigmas=..., alpha: Incomplete | None = ..., black_ridges: bool = ..., mode: str = ..., cval: int = ...): ...
def sato(image, sigmas=..., black_ridges: bool = ..., mode: str = ..., cval: int = ...): ...
def frangi(image, sigmas=..., scale_range: Incomplete | None = ..., scale_step: Incomplete | None = ..., alpha: float = ..., beta: float = ..., gamma: int = ..., black_ridges: bool = ..., mode: str = ..., cval: int = ...): ...
def hessian(image, sigmas=..., scale_range: Incomplete | None = ..., scale_step: Incomplete | None = ..., alpha: float = ..., beta: float = ..., gamma: int = ..., black_ridges: bool = ..., mode: str = ..., cval: int = ...): ...
