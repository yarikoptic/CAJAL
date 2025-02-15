from _typeshed import Incomplete
from pandas._config import get_option as get_option
from pandas._typing import FuncType as FuncType
from pandas.core.computation.check import NUMEXPR_INSTALLED as NUMEXPR_INSTALLED
from pandas.core.ops import roperator as roperator
from pandas.util._exceptions import find_stack_level as find_stack_level

USE_NUMEXPR = NUMEXPR_INSTALLED

def set_use_numexpr(v: bool = ...) -> None: ...
def set_numexpr_threads(n: Incomplete | None = ...) -> None: ...
def evaluate(op, a, b, use_numexpr: bool = ...): ...
def where(cond, a, b, use_numexpr: bool = ...): ...
def set_test_mode(v: bool = ...) -> None: ...
def get_test_result() -> list[bool]: ...
