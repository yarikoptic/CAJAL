from pandas.compat._optional import import_optional_dependency as import_optional_dependency
from pandas.core.dtypes.common import is_integer as is_integer, is_list_like as is_list_like
from pandas.io.excel._base import ExcelWriter as ExcelWriter
from typing import Any, Callable, Hashable, Literal, Sequence, TypeVar, overload

ExcelWriter_t = type[ExcelWriter]
usecols_func = TypeVar('usecols_func', bound=Callable[[Hashable], object])

def register_writer(klass: ExcelWriter_t) -> None: ...
def get_default_engine(ext: str, mode: Literal['reader', 'writer'] = ...) -> str: ...
def get_writer(engine_name: str) -> ExcelWriter_t: ...
@overload
def maybe_convert_usecols(usecols: Union[str, list[int]]) -> list[int]: ...
@overload
def maybe_convert_usecols(usecols: list[str]) -> list[str]: ...
@overload
def maybe_convert_usecols(usecols: usecols_func) -> usecols_func: ...
@overload
def maybe_convert_usecols(usecols: None) -> None: ...
@overload
def validate_freeze_panes(freeze_panes: tuple[int, int]) -> Literal[True]: ...
@overload
def validate_freeze_panes(freeze_panes: None) -> Literal[False]: ...
def fill_mi_header(row: list[Hashable], control_row: list[bool]) -> tuple[list[Hashable], list[bool]]: ...
def pop_header_name(row: list[Hashable], index_col: Union[int, Sequence[int]]) -> tuple[Union[Hashable, None], list[Hashable]]: ...
def combine_kwargs(engine_kwargs: Union[dict[str, Any], None], kwargs: dict) -> dict: ...
