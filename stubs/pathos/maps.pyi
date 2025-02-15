from _typeshed import Incomplete

class Map:
    pool: Incomplete
    args: Incomplete
    kwds: Incomplete
    def __init__(self, pool: Incomplete | None = ..., *args, **kwds) -> None: ...
    def __call__(self, func, *args, **kwds): ...
    def __cls__(self): ...
    def __meth__(self): ...
    def __attr__(self): ...
    __self__: Incomplete
    __func__: Incomplete
    __get__: Incomplete
    def close(self) -> None: ...
    def join(self) -> None: ...
    def clear(self) -> None: ...
    def __del__(self) -> None: ...

class Smap(Map):
    def __init__(self, pool: Incomplete | None = ..., *args, **kwds) -> None: ...
    def __call__(self, func, *args, **kwds): ...

class Imap(Map):
    def __init__(self, pool: Incomplete | None = ..., *args, **kwds) -> None: ...
    def __call__(self, func, *args, **kwds): ...

class Amap(Map):
    def __init__(self, pool: Incomplete | None = ..., *args, **kwds) -> None: ...
    def __call__(self, func, *args, **kwds): ...

class Asmap(Map):
    def __init__(self, pool: Incomplete | None = ..., *args, **kwds) -> None: ...
    def __call__(self, func, *args, **kwds): ...

class Uimap(Map):
    def __init__(self, pool: Incomplete | None = ..., *args, **kwds) -> None: ...
    def __call__(self, func, *args, **kwds): ...

class Ismap(Map):
    def __init__(self, pool: Incomplete | None = ..., *args, **kwds) -> None: ...
    def __call__(self, func, *args, **kwds): ...
