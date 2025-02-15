from typing import Any, ClassVar

class NDArrayBacked:
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    T: Any
    _dtype: Any
    _ndarray: Any
    nbytes: Any
    ndim: Any
    shape: Any
    size: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def _from_backing_data(self, *args, **kwargs) -> Any: ...
    @classmethod
    def _simple_new(cls, *args, **kwargs) -> Any: ...
    def copy(self, *args, **kwargs) -> Any: ...
    def delete(self, *args, **kwargs) -> Any: ...
    def ravel(self, *args, **kwargs) -> Any: ...
    def repeat(self, *args, **kwargs) -> Any: ...
    def reshape(self, *args, **kwargs) -> Any: ...
    def swapaxes(self, *args, **kwargs) -> Any: ...
    def transpose(self, *args, **kwargs) -> Any: ...
    def __len__(self) -> Any: ...
    def __reduce__(self) -> Any: ...
    def __setstate__(self, state) -> Any: ...
    def __setstate_cython__(self, *args, **kwargs) -> Any: ...

def __pyx_unpickle_NDArrayBacked(*args, **kwargs) -> Any: ...
