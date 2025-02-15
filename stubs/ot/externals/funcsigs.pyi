from _typeshed import Incomplete

def signature(obj): ...

class _void: ...
class _empty: ...

class _ParameterKind(int):
    def __new__(self, *args, **kwargs): ...

class Parameter:
    POSITIONAL_ONLY: Incomplete
    POSITIONAL_OR_KEYWORD: Incomplete
    VAR_POSITIONAL: Incomplete
    KEYWORD_ONLY: Incomplete
    VAR_KEYWORD: Incomplete
    empty: Incomplete
    def __init__(self, name, kind, default=..., annotation=..., _partial_kwarg: bool = ...) -> None: ...
    @property
    def name(self): ...
    @property
    def default(self): ...
    @property
    def annotation(self): ...
    @property
    def kind(self): ...
    def replace(self, name=..., kind=..., annotation=..., default=..., _partial_kwarg=...): ...
    def __hash__(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

class BoundArguments:
    arguments: Incomplete
    def __init__(self, signature, arguments) -> None: ...
    @property
    def signature(self): ...
    @property
    def args(self): ...
    @property
    def kwargs(self): ...
    def __hash__(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

class Signature:
    empty: Incomplete
    def __init__(self, parameters: Incomplete | None = ..., return_annotation=..., __validate_parameters__: bool = ...) -> None: ...
    @classmethod
    def from_function(cls, func): ...
    @property
    def parameters(self): ...
    @property
    def return_annotation(self): ...
    def replace(self, parameters=..., return_annotation=...): ...
    def __hash__(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def bind(self, *args, **kwargs): ...
    def bind_partial(self, *args, **kwargs): ...
