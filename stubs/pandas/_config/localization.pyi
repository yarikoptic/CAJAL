from pandas._config.config import options as options
from typing import Callable, Iterator

def set_locale(new_locale: Union[str, tuple[str, str]], lc_var: int = ...) -> Iterator[Union[str, tuple[str, str]]]: ...
def can_set_locale(lc: str, lc_var: int = ...) -> bool: ...
def get_locales(prefix: Union[str, None] = ..., normalize: bool = ..., locale_getter: Callable[[], bytes] = ...) -> Union[list[str], None]: ...
