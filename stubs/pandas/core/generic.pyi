import numpy as np
from _typeshed import Incomplete
from collections.abc import Generator
from datetime import timedelta
from pandas._config import config as config
from pandas._libs import lib as lib
from pandas._libs.tslibs import BaseOffset as BaseOffset, Period as Period, Tick as Tick, Timestamp as Timestamp, to_offset as to_offset
from pandas._typing import AnyArrayLike as AnyArrayLike, ArrayLike as ArrayLike, Axis as Axis, ColspaceArgType as ColspaceArgType, CompressionOptions as CompressionOptions, Dtype as Dtype, DtypeArg as DtypeArg, DtypeObj as DtypeObj, FilePath as FilePath, FillnaOptions as FillnaOptions, FloatFormatType as FloatFormatType, FormattersType as FormattersType, Frequency as Frequency, IgnoreRaise as IgnoreRaise, IndexKeyFunc as IndexKeyFunc, IndexLabel as IndexLabel, IntervalClosedType as IntervalClosedType, JSONSerializable as JSONSerializable, Level as Level, Manager as Manager, NDFrameT as NDFrameT, NaPosition as NaPosition, RandomState as RandomState, Renamer as Renamer, SortKind as SortKind, StorageOptions as StorageOptions, Suffixes as Suffixes, T as T, TimedeltaConvertibleTypes as TimedeltaConvertibleTypes, TimestampConvertibleTypes as TimestampConvertibleTypes, ValueKeyFunc as ValueKeyFunc, WriteBuffer as WriteBuffer, npt as npt
from pandas.compat._optional import import_optional_dependency as import_optional_dependency
from pandas.core import arraylike as arraylike, indexing as indexing, missing as missing, nanops as nanops, sample as sample
from pandas.core.array_algos.replace import should_use_regex as should_use_regex
from pandas.core.arrays import ExtensionArray as ExtensionArray
from pandas.core.base import PandasObject as PandasObject
from pandas.core.construction import create_series_with_explicit_dtype as create_series_with_explicit_dtype, extract_array as extract_array
from pandas.core.describe import describe_ndframe as describe_ndframe
from pandas.core.dtypes.common import ensure_object as ensure_object, ensure_platform_int as ensure_platform_int, ensure_str as ensure_str, is_bool as is_bool, is_bool_dtype as is_bool_dtype, is_datetime64_any_dtype as is_datetime64_any_dtype, is_datetime64tz_dtype as is_datetime64tz_dtype, is_dict_like as is_dict_like, is_dtype_equal as is_dtype_equal, is_extension_array_dtype as is_extension_array_dtype, is_float as is_float, is_list_like as is_list_like, is_number as is_number, is_numeric_dtype as is_numeric_dtype, is_re_compilable as is_re_compilable, is_scalar as is_scalar, is_timedelta64_dtype as is_timedelta64_dtype, pandas_dtype as pandas_dtype
from pandas.core.dtypes.generic import ABCDataFrame as ABCDataFrame, ABCSeries as ABCSeries
from pandas.core.dtypes.inference import is_hashable as is_hashable, is_nested_list_like as is_nested_list_like
from pandas.core.dtypes.missing import isna as isna, notna as notna
from pandas.core.flags import Flags as Flags
from pandas.core.frame import DataFrame as DataFrame
from pandas.core.indexers.objects import BaseIndexer as BaseIndexer
from pandas.core.indexes.api import DatetimeIndex as DatetimeIndex, Index as Index, MultiIndex as MultiIndex, PeriodIndex as PeriodIndex, RangeIndex as RangeIndex, default_index as default_index, ensure_index as ensure_index
from pandas.core.internals import ArrayManager as ArrayManager, BlockManager as BlockManager, SingleArrayManager as SingleArrayManager
from pandas.core.internals.construction import mgr_to_mgr as mgr_to_mgr
from pandas.core.missing import find_valid_index as find_valid_index
from pandas.core.ops import align_method_FRAME as align_method_FRAME
from pandas.core.resample import Resampler as Resampler
from pandas.core.reshape.concat import concat as concat
from pandas.core.series import Series as Series
from pandas.core.sorting import get_indexer_indexer as get_indexer_indexer
from pandas.core.window import Expanding as Expanding, ExponentialMovingWindow as ExponentialMovingWindow, Rolling as Rolling, Window as Window
from pandas.errors import AbstractMethodError as AbstractMethodError, InvalidIndexError as InvalidIndexError, SettingWithCopyError as SettingWithCopyError, SettingWithCopyWarning as SettingWithCopyWarning
from pandas.io.formats.format import DataFrameFormatter as DataFrameFormatter, DataFrameRenderer as DataFrameRenderer
from pandas.io.formats.printing import pprint_thing as pprint_thing
from pandas.io.pytables import HDFStore as HDFStore
from pandas.util._decorators import deprecate_kwarg as deprecate_kwarg, deprecate_nonkeyword_arguments as deprecate_nonkeyword_arguments, doc as doc, rewrite_axis_style_signature as rewrite_axis_style_signature
from pandas.util._exceptions import find_stack_level as find_stack_level
from pandas.util._validators import validate_ascending as validate_ascending, validate_bool_kwarg as validate_bool_kwarg, validate_fillna_kwargs as validate_fillna_kwargs, validate_inclusive as validate_inclusive
from typing import Any, Callable, ClassVar, Hashable, Literal, Mapping, NoReturn, Sequence, overload

bool_t = bool

class NDFrame(PandasObject, indexing.IndexingMixin):
    def __init__(self, data: Manager, copy: bool_t = ..., attrs: Union[Mapping[Hashable, Any], None] = ...) -> None: ...
    @property
    def attrs(self) -> dict[Hashable, Any]: ...
    @attrs.setter
    def attrs(self, value: Mapping[Hashable, Any]) -> None: ...
    @property
    def flags(self) -> Flags: ...
    def set_flags(self, *, copy: bool_t = ..., allows_duplicate_labels: Union[bool_t, None] = ...) -> NDFrameT: ...
    @property
    def shape(self) -> tuple[int, ...]: ...
    @property
    def axes(self) -> list[Index]: ...
    @property
    def ndim(self) -> int: ...
    @property
    def size(self) -> int: ...
    @overload
    def set_axis(self, labels, *, axis: Axis = ..., inplace: Union[Literal[False], lib.NoDefault] = ..., copy: Union[bool_t, lib.NoDefault] = ...) -> NDFrameT: ...
    @overload
    def set_axis(self, labels, *, axis: Axis = ..., inplace: Literal[True], copy: Union[bool_t, lib.NoDefault] = ...) -> None: ...
    @overload
    def set_axis(self, labels, *, axis: Axis = ..., inplace: Union[bool_t, lib.NoDefault] = ..., copy: Union[bool_t, lib.NoDefault] = ...) -> Union[NDFrameT, None]: ...
    def swapaxes(self, axis1: Axis, axis2: Axis, copy: bool_t = ...) -> NDFrameT: ...
    def droplevel(self, level: IndexLabel, axis: Axis = ...) -> NDFrameT: ...
    def pop(self, item: Hashable) -> Union[Series, Any]: ...
    def squeeze(self, axis: Incomplete | None = ...): ...
    @overload
    def rename_axis(self, mapper: Union[IndexLabel, lib.NoDefault] = ..., *, inplace: Literal[False] = ..., **kwargs) -> NDFrameT: ...
    @overload
    def rename_axis(self, mapper: Union[IndexLabel, lib.NoDefault] = ..., *, inplace: Literal[True], **kwargs) -> None: ...
    @overload
    def rename_axis(self, mapper: Union[IndexLabel, lib.NoDefault] = ..., *, inplace: bool_t = ..., **kwargs) -> Union[NDFrameT, None]: ...
    def equals(self, other: object) -> bool_t: ...
    def __neg__(self) -> NDFrameT: ...
    def __pos__(self) -> NDFrameT: ...
    def __invert__(self) -> NDFrameT: ...
    def __nonzero__(self) -> NoReturn: ...
    __bool__: Incomplete
    def bool(self) -> bool_t: ...
    def abs(self) -> NDFrameT: ...
    def __abs__(self) -> NDFrameT: ...
    def __round__(self, decimals: int = ...) -> NDFrameT: ...
    __hash__: ClassVar[None]
    def __iter__(self): ...
    def keys(self) -> Index: ...
    def items(self) -> Generator[Incomplete, None, None]: ...
    def __len__(self) -> int: ...
    def __contains__(self, key) -> bool_t: ...
    @property
    def empty(self) -> bool_t: ...
    __array_priority__: int
    def __array__(self, dtype: Union[npt.DTypeLike, None] = ...) -> np.ndarray: ...
    def __array_wrap__(self, result: np.ndarray, context: Union[tuple[Callable, tuple[Any, ...], int], None] = ...): ...
    def __array_ufunc__(self, ufunc: np.ufunc, method: str, *inputs: Any, **kwargs: Any): ...
    def to_excel(self, excel_writer, sheet_name: str = ..., na_rep: str = ..., float_format: Union[str, None] = ..., columns: Union[Sequence[Hashable], None] = ..., header: Union[Sequence[Hashable], bool_t] = ..., index: bool_t = ..., index_label: IndexLabel = ..., startrow: int = ..., startcol: int = ..., engine: Union[str, None] = ..., merge_cells: bool_t = ..., encoding: lib.NoDefault = ..., inf_rep: str = ..., verbose: lib.NoDefault = ..., freeze_panes: Union[tuple[int, int], None] = ..., storage_options: StorageOptions = ...) -> None: ...
    def to_json(self, path_or_buf: Union[FilePath, WriteBuffer[bytes], WriteBuffer[str], None] = ..., orient: Union[str, None] = ..., date_format: Union[str, None] = ..., double_precision: int = ..., force_ascii: bool_t = ..., date_unit: str = ..., default_handler: Union[Callable[[Any], JSONSerializable], None] = ..., lines: bool_t = ..., compression: CompressionOptions = ..., index: bool_t = ..., indent: Union[int, None] = ..., storage_options: StorageOptions = ...) -> Union[str, None]: ...
    def to_hdf(self, path_or_buf: Union[FilePath, HDFStore], key: str, mode: str = ..., complevel: Union[int, None] = ..., complib: Union[str, None] = ..., append: bool_t = ..., format: Union[str, None] = ..., index: bool_t = ..., min_itemsize: Union[int, dict[str, int], None] = ..., nan_rep: Incomplete | None = ..., dropna: Union[bool_t, None] = ..., data_columns: Union[Literal[True], list[str], None] = ..., errors: str = ..., encoding: str = ...) -> None: ...
    def to_sql(self, name: str, con, schema: Union[str, None] = ..., if_exists: str = ..., index: bool_t = ..., index_label: IndexLabel = ..., chunksize: Union[int, None] = ..., dtype: Union[DtypeArg, None] = ..., method: Union[str, None] = ...) -> Union[int, None]: ...
    def to_pickle(self, path: Union[FilePath, WriteBuffer[bytes]], compression: CompressionOptions = ..., protocol: int = ..., storage_options: StorageOptions = ...) -> None: ...
    def to_clipboard(self, excel: bool_t = ..., sep: Union[str, None] = ..., **kwargs) -> None: ...
    def to_xarray(self): ...
    @overload
    def to_latex(self, buf: None = ..., columns: Union[Sequence[Hashable], None] = ..., col_space: Union[ColspaceArgType, None] = ..., header: Union[bool_t, Sequence[str]] = ..., index: bool_t = ..., na_rep: str = ..., formatters: Union[FormattersType, None] = ..., float_format: Union[FloatFormatType, None] = ..., sparsify: Union[bool_t, None] = ..., index_names: bool_t = ..., bold_rows: bool_t = ..., column_format: Union[str, None] = ..., longtable: Union[bool_t, None] = ..., escape: Union[bool_t, None] = ..., encoding: Union[str, None] = ..., decimal: str = ..., multicolumn: Union[bool_t, None] = ..., multicolumn_format: Union[str, None] = ..., multirow: Union[bool_t, None] = ..., caption: Union[str, tuple[str, str], None] = ..., label: Union[str, None] = ..., position: Union[str, None] = ...) -> str: ...
    @overload
    def to_latex(self, buf: Union[FilePath, WriteBuffer[str]], columns: Union[Sequence[Hashable], None] = ..., col_space: Union[ColspaceArgType, None] = ..., header: Union[bool_t, Sequence[str]] = ..., index: bool_t = ..., na_rep: str = ..., formatters: Union[FormattersType, None] = ..., float_format: Union[FloatFormatType, None] = ..., sparsify: Union[bool_t, None] = ..., index_names: bool_t = ..., bold_rows: bool_t = ..., column_format: Union[str, None] = ..., longtable: Union[bool_t, None] = ..., escape: Union[bool_t, None] = ..., encoding: Union[str, None] = ..., decimal: str = ..., multicolumn: Union[bool_t, None] = ..., multicolumn_format: Union[str, None] = ..., multirow: Union[bool_t, None] = ..., caption: Union[str, tuple[str, str], None] = ..., label: Union[str, None] = ..., position: Union[str, None] = ...) -> None: ...
    @overload
    def to_csv(self, path_or_buf: None = ..., sep: str = ..., na_rep: str = ..., float_format: Union[str, Callable, None] = ..., columns: Union[Sequence[Hashable], None] = ..., header: Union[bool_t, list[str]] = ..., index: bool_t = ..., index_label: Union[IndexLabel, None] = ..., mode: str = ..., encoding: Union[str, None] = ..., compression: CompressionOptions = ..., quoting: Union[int, None] = ..., quotechar: str = ..., lineterminator: Union[str, None] = ..., chunksize: Union[int, None] = ..., date_format: Union[str, None] = ..., doublequote: bool_t = ..., escapechar: Union[str, None] = ..., decimal: str = ..., errors: str = ..., storage_options: StorageOptions = ...) -> str: ...
    @overload
    def to_csv(self, path_or_buf: Union[FilePath, WriteBuffer[bytes], WriteBuffer[str]], sep: str = ..., na_rep: str = ..., float_format: Union[str, Callable, None] = ..., columns: Union[Sequence[Hashable], None] = ..., header: Union[bool_t, list[str]] = ..., index: bool_t = ..., index_label: Union[IndexLabel, None] = ..., mode: str = ..., encoding: Union[str, None] = ..., compression: CompressionOptions = ..., quoting: Union[int, None] = ..., quotechar: str = ..., lineterminator: Union[str, None] = ..., chunksize: Union[int, None] = ..., date_format: Union[str, None] = ..., doublequote: bool_t = ..., escapechar: Union[str, None] = ..., decimal: str = ..., errors: str = ..., storage_options: StorageOptions = ...) -> None: ...
    def take(self, indices, axis: int = ..., is_copy: Union[bool_t, None] = ..., **kwargs) -> NDFrameT: ...
    def xs(self, key: IndexLabel, axis: Axis = ..., level: IndexLabel = ..., drop_level: bool_t = ...) -> NDFrameT: ...
    def __getitem__(self, item) -> None: ...
    def __delitem__(self, key) -> None: ...
    def get(self, key, default: Incomplete | None = ...): ...
    def reindex_like(self, other, method: Union[str, None] = ..., copy: bool_t = ..., limit: Incomplete | None = ..., tolerance: Incomplete | None = ...) -> NDFrameT: ...
    @overload
    def drop(self, labels: IndexLabel = ..., *, axis: Axis = ..., index: IndexLabel = ..., columns: IndexLabel = ..., level: Union[Level, None] = ..., inplace: Literal[True], errors: IgnoreRaise = ...) -> None: ...
    @overload
    def drop(self, labels: IndexLabel = ..., *, axis: Axis = ..., index: IndexLabel = ..., columns: IndexLabel = ..., level: Union[Level, None] = ..., inplace: Literal[False] = ..., errors: IgnoreRaise = ...) -> NDFrameT: ...
    @overload
    def drop(self, labels: IndexLabel = ..., *, axis: Axis = ..., index: IndexLabel = ..., columns: IndexLabel = ..., level: Union[Level, None] = ..., inplace: bool_t = ..., errors: IgnoreRaise = ...) -> Union[NDFrameT, None]: ...
    def add_prefix(self, prefix: str) -> NDFrameT: ...
    def add_suffix(self, suffix: str) -> NDFrameT: ...
    @overload
    def sort_values(self, *, axis: Axis = ..., ascending=..., inplace: Literal[False] = ..., kind: str = ..., na_position: str = ..., ignore_index: bool_t = ..., key: ValueKeyFunc = ...) -> NDFrameT: ...
    @overload
    def sort_values(self, *, axis: Axis = ..., ascending=..., inplace: Literal[True], kind: str = ..., na_position: str = ..., ignore_index: bool_t = ..., key: ValueKeyFunc = ...) -> None: ...
    @overload
    def sort_values(self, *, axis: Axis = ..., ascending=..., inplace: bool_t = ..., kind: str = ..., na_position: str = ..., ignore_index: bool_t = ..., key: ValueKeyFunc = ...) -> Union[NDFrameT, None]: ...
    @overload
    def sort_index(self, *, axis: Axis = ..., level: IndexLabel = ..., ascending: Union[bool_t, Sequence[bool_t]] = ..., inplace: Literal[True], kind: SortKind = ..., na_position: NaPosition = ..., sort_remaining: bool_t = ..., ignore_index: bool_t = ..., key: IndexKeyFunc = ...) -> None: ...
    @overload
    def sort_index(self, *, axis: Axis = ..., level: IndexLabel = ..., ascending: Union[bool_t, Sequence[bool_t]] = ..., inplace: Literal[False] = ..., kind: SortKind = ..., na_position: NaPosition = ..., sort_remaining: bool_t = ..., ignore_index: bool_t = ..., key: IndexKeyFunc = ...) -> NDFrameT: ...
    @overload
    def sort_index(self, *, axis: Axis = ..., level: IndexLabel = ..., ascending: Union[bool_t, Sequence[bool_t]] = ..., inplace: bool_t = ..., kind: SortKind = ..., na_position: NaPosition = ..., sort_remaining: bool_t = ..., ignore_index: bool_t = ..., key: IndexKeyFunc = ...) -> Union[NDFrameT, None]: ...
    def reindex(self, *args, **kwargs) -> NDFrameT: ...
    def filter(self, items: Incomplete | None = ..., like: Union[str, None] = ..., regex: Union[str, None] = ..., axis: Incomplete | None = ...) -> NDFrameT: ...
    def head(self, n: int = ...) -> NDFrameT: ...
    def tail(self, n: int = ...) -> NDFrameT: ...
    def sample(self, n: Union[int, None] = ..., frac: Union[float, None] = ..., replace: bool_t = ..., weights: Incomplete | None = ..., random_state: Union[RandomState, None] = ..., axis: Union[Axis, None] = ..., ignore_index: bool_t = ...) -> NDFrameT: ...
    def pipe(self, func: Union[Callable[..., T], tuple[Callable[..., T], str]], *args, **kwargs) -> T: ...
    def __finalize__(self, other, method: Union[str, None] = ..., **kwargs) -> NDFrameT: ...
    def __getattr__(self, name: str): ...
    def __setattr__(self, name: str, value) -> None: ...
    @property
    def values(self) -> None: ...
    @property
    def dtypes(self): ...
    def astype(self, dtype, copy: bool_t = ..., errors: IgnoreRaise = ...) -> NDFrameT: ...
    def copy(self, deep: Union[bool_t, None] = ...) -> NDFrameT: ...
    def __copy__(self, deep: bool_t = ...) -> NDFrameT: ...
    def __deepcopy__(self, memo: Incomplete | None = ...) -> NDFrameT: ...
    def infer_objects(self) -> NDFrameT: ...
    def convert_dtypes(self, infer_objects: bool_t = ..., convert_string: bool_t = ..., convert_integer: bool_t = ..., convert_boolean: bool_t = ..., convert_floating: bool_t = ...) -> NDFrameT: ...
    @overload
    def fillna(self, value: Union[Hashable, Mapping, Series, DataFrame] = ..., *, method: Union[FillnaOptions, None] = ..., axis: Union[Axis, None] = ..., inplace: Literal[False] = ..., limit: Union[int, None] = ..., downcast: Union[dict, None] = ...) -> NDFrameT: ...
    @overload
    def fillna(self, value: Union[Hashable, Mapping, Series, DataFrame] = ..., *, method: Union[FillnaOptions, None] = ..., axis: Union[Axis, None] = ..., inplace: Literal[True], limit: Union[int, None] = ..., downcast: Union[dict, None] = ...) -> None: ...
    @overload
    def fillna(self, value: Union[Hashable, Mapping, Series, DataFrame] = ..., *, method: Union[FillnaOptions, None] = ..., axis: Union[Axis, None] = ..., inplace: bool_t = ..., limit: Union[int, None] = ..., downcast: Union[dict, None] = ...) -> Union[NDFrameT, None]: ...
    @overload
    def ffill(self, *, axis: Union[None, Axis] = ..., inplace: Literal[False] = ..., limit: Union[None, int] = ..., downcast: Union[dict, None] = ...) -> NDFrameT: ...
    @overload
    def ffill(self, *, axis: Union[None, Axis] = ..., inplace: Literal[True], limit: Union[None, int] = ..., downcast: Union[dict, None] = ...) -> None: ...
    @overload
    def ffill(self, *, axis: Union[None, Axis] = ..., inplace: bool_t = ..., limit: Union[None, int] = ..., downcast: Union[dict, None] = ...) -> Union[NDFrameT, None]: ...
    pad: Incomplete
    @overload
    def bfill(self, *, axis: Union[None, Axis] = ..., inplace: Literal[False] = ..., limit: Union[None, int] = ..., downcast: Union[dict, None] = ...) -> NDFrameT: ...
    @overload
    def bfill(self, *, axis: Union[None, Axis] = ..., inplace: Literal[True], limit: Union[None, int] = ..., downcast: Union[dict, None] = ...) -> None: ...
    @overload
    def bfill(self, *, axis: Union[None, Axis] = ..., inplace: bool_t = ..., limit: Union[None, int] = ..., downcast: Union[dict, None] = ...) -> Union[NDFrameT, None]: ...
    backfill: Incomplete
    @overload
    def replace(self, to_replace=..., value=..., *, inplace: Literal[False] = ..., limit: Union[int, None] = ..., regex: bool_t = ..., method: Union[Literal['pad', 'ffill', 'bfill'], lib.NoDefault] = ...) -> NDFrameT: ...
    @overload
    def replace(self, to_replace=..., value=..., *, inplace: Literal[True], limit: Union[int, None] = ..., regex: bool_t = ..., method: Union[Literal['pad', 'ffill', 'bfill'], lib.NoDefault] = ...) -> None: ...
    @overload
    def replace(self, to_replace=..., value=..., *, inplace: bool_t = ..., limit: Union[int, None] = ..., regex: bool_t = ..., method: Union[Literal['pad', 'ffill', 'bfill'], lib.NoDefault] = ...) -> Union[NDFrameT, None]: ...
    def interpolate(self, method: str = ..., axis: Axis = ..., limit: Union[int, None] = ..., inplace: bool_t = ..., limit_direction: Union[str, None] = ..., limit_area: Union[str, None] = ..., downcast: Union[str, None] = ..., **kwargs) -> Union[NDFrameT, None]: ...
    def asof(self, where, subset: Incomplete | None = ...): ...
    def isna(self) -> NDFrameT: ...
    def isnull(self) -> NDFrameT: ...
    def notna(self) -> NDFrameT: ...
    def notnull(self) -> NDFrameT: ...
    def clip(self, lower: Incomplete | None = ..., upper: Incomplete | None = ..., axis: Union[Axis, None] = ..., inplace: bool_t = ..., *args, **kwargs) -> Union[NDFrameT, None]: ...
    def asfreq(self, freq: Frequency, method: Union[FillnaOptions, None] = ..., how: Union[str, None] = ..., normalize: bool_t = ..., fill_value: Hashable = ...) -> NDFrameT: ...
    def at_time(self, time, asof: bool_t = ..., axis: Incomplete | None = ...) -> NDFrameT: ...
    def between_time(self, start_time, end_time, include_start: Union[bool_t, lib.NoDefault] = ..., include_end: Union[bool_t, lib.NoDefault] = ..., inclusive: Union[IntervalClosedType, None] = ..., axis: Incomplete | None = ...) -> NDFrameT: ...
    def resample(self, rule, axis: Axis = ..., closed: Union[str, None] = ..., label: Union[str, None] = ..., convention: str = ..., kind: Union[str, None] = ..., loffset: Incomplete | None = ..., base: Union[int, None] = ..., on: Level = ..., level: Level = ..., origin: Union[str, TimestampConvertibleTypes] = ..., offset: Union[TimedeltaConvertibleTypes, None] = ..., group_keys: Union[bool_t, lib.NoDefault] = ...) -> Resampler: ...
    def first(self, offset) -> NDFrameT: ...
    def last(self, offset) -> NDFrameT: ...
    def rank(self, axis: int = ..., method: str = ..., numeric_only: Union[bool_t, None, lib.NoDefault] = ..., na_option: str = ..., ascending: bool_t = ..., pct: bool_t = ...) -> NDFrameT: ...
    def compare(self, other, align_axis: Axis = ..., keep_shape: bool_t = ..., keep_equal: bool_t = ..., result_names: Suffixes = ...): ...
    def align(self, other: NDFrameT, join: Literal['outer', 'inner', 'left', 'right'] = ..., axis: Union[Axis, None] = ..., level: Level = ..., copy: bool_t = ..., fill_value: Hashable = ..., method: Union[FillnaOptions, None] = ..., limit: Union[int, None] = ..., fill_axis: Axis = ..., broadcast_axis: Union[Axis, None] = ...) -> NDFrameT: ...
    @overload
    def where(self, cond, other=..., *, inplace: Literal[False] = ..., axis: Union[Axis, None] = ..., level: Level = ..., errors: Union[IgnoreRaise, lib.NoDefault] = ..., try_cast: Union[bool_t, lib.NoDefault] = ...) -> NDFrameT: ...
    @overload
    def where(self, cond, other=..., *, inplace: Literal[True], axis: Union[Axis, None] = ..., level: Level = ..., errors: Union[IgnoreRaise, lib.NoDefault] = ..., try_cast: Union[bool_t, lib.NoDefault] = ...) -> None: ...
    @overload
    def where(self, cond, other=..., *, inplace: bool_t = ..., axis: Union[Axis, None] = ..., level: Level = ..., errors: Union[IgnoreRaise, lib.NoDefault] = ..., try_cast: Union[bool_t, lib.NoDefault] = ...) -> Union[NDFrameT, None]: ...
    @overload
    def mask(self, cond, other=..., *, inplace: Literal[False] = ..., axis: Union[Axis, None] = ..., level: Level = ..., errors: Union[IgnoreRaise, lib.NoDefault] = ..., try_cast: Union[bool_t, lib.NoDefault] = ...) -> NDFrameT: ...
    @overload
    def mask(self, cond, other=..., *, inplace: Literal[True], axis: Union[Axis, None] = ..., level: Level = ..., errors: Union[IgnoreRaise, lib.NoDefault] = ..., try_cast: Union[bool_t, lib.NoDefault] = ...) -> None: ...
    @overload
    def mask(self, cond, other=..., *, inplace: bool_t = ..., axis: Union[Axis, None] = ..., level: Level = ..., errors: Union[IgnoreRaise, lib.NoDefault] = ..., try_cast: Union[bool_t, lib.NoDefault] = ...) -> Union[NDFrameT, None]: ...
    def shift(self, periods: int = ..., freq: Incomplete | None = ..., axis: Axis = ..., fill_value: Hashable = ...) -> NDFrameT: ...
    def slice_shift(self, periods: int = ..., axis: int = ...) -> NDFrameT: ...
    def tshift(self, periods: int = ..., freq: Incomplete | None = ..., axis: Axis = ...) -> NDFrameT: ...
    def truncate(self, before: Incomplete | None = ..., after: Incomplete | None = ..., axis: Incomplete | None = ..., copy: bool_t = ...) -> NDFrameT: ...
    def tz_convert(self, tz, axis: int = ..., level: Incomplete | None = ..., copy: bool_t = ...) -> NDFrameT: ...
    def tz_localize(self, tz, axis: int = ..., level: Incomplete | None = ..., copy: bool_t = ..., ambiguous: str = ..., nonexistent: str = ...) -> NDFrameT: ...
    def describe(self, percentiles: Incomplete | None = ..., include: Incomplete | None = ..., exclude: Incomplete | None = ..., datetime_is_numeric: bool_t = ...) -> NDFrameT: ...
    def pct_change(self, periods: int = ..., fill_method: str = ..., limit: Incomplete | None = ..., freq: Incomplete | None = ..., **kwargs) -> NDFrameT: ...
    def any(self, axis: Axis = ..., bool_only: Union[bool_t, None] = ..., skipna: bool_t = ..., level: Union[Level, None] = ..., **kwargs) -> Union[DataFrame, Series, bool_t]: ...
    def all(self, axis: Axis = ..., bool_only: Union[bool_t, None] = ..., skipna: bool_t = ..., level: Union[Level, None] = ..., **kwargs) -> Union[Series, bool_t]: ...
    def cummax(self, axis: Union[Axis, None] = ..., skipna: bool_t = ..., *args, **kwargs): ...
    def cummin(self, axis: Union[Axis, None] = ..., skipna: bool_t = ..., *args, **kwargs): ...
    def cumsum(self, axis: Union[Axis, None] = ..., skipna: bool_t = ..., *args, **kwargs): ...
    def cumprod(self, axis: Union[Axis, None] = ..., skipna: bool_t = ..., *args, **kwargs): ...
    def sem(self, axis: Union[Axis, None] = ..., skipna: bool_t = ..., level: Union[Level, None] = ..., ddof: int = ..., numeric_only: Union[bool_t, None] = ..., **kwargs) -> Union[Series, float]: ...
    def var(self, axis: Union[Axis, None] = ..., skipna: bool_t = ..., level: Union[Level, None] = ..., ddof: int = ..., numeric_only: Union[bool_t, None] = ..., **kwargs) -> Union[Series, float]: ...
    def std(self, axis: Union[Axis, None] = ..., skipna: bool_t = ..., level: Union[Level, None] = ..., ddof: int = ..., numeric_only: Union[bool_t, None] = ..., **kwargs) -> Union[Series, float]: ...
    def min(self, axis: Union[Axis, None, lib.NoDefault] = ..., skipna: bool_t = ..., level: Union[Level, None] = ..., numeric_only: Union[bool_t, None] = ..., **kwargs): ...
    def max(self, axis: Union[Axis, None, lib.NoDefault] = ..., skipna: bool_t = ..., level: Union[Level, None] = ..., numeric_only: Union[bool_t, None] = ..., **kwargs): ...
    def mean(self, axis: Union[Axis, None, lib.NoDefault] = ..., skipna: bool_t = ..., level: Union[Level, None] = ..., numeric_only: Union[bool_t, None] = ..., **kwargs) -> Union[Series, float]: ...
    def median(self, axis: Union[Axis, None, lib.NoDefault] = ..., skipna: bool_t = ..., level: Union[Level, None] = ..., numeric_only: Union[bool_t, None] = ..., **kwargs) -> Union[Series, float]: ...
    def skew(self, axis: Union[Axis, None, lib.NoDefault] = ..., skipna: bool_t = ..., level: Union[Level, None] = ..., numeric_only: Union[bool_t, None] = ..., **kwargs) -> Union[Series, float]: ...
    def kurt(self, axis: Union[Axis, None, lib.NoDefault] = ..., skipna: bool_t = ..., level: Union[Level, None] = ..., numeric_only: Union[bool_t, None] = ..., **kwargs) -> Union[Series, float]: ...
    kurtosis: Incomplete
    def sum(self, axis: Union[Axis, None] = ..., skipna: bool_t = ..., level: Union[Level, None] = ..., numeric_only: Union[bool_t, None] = ..., min_count: int = ..., **kwargs): ...
    def prod(self, axis: Union[Axis, None] = ..., skipna: bool_t = ..., level: Union[Level, None] = ..., numeric_only: Union[bool_t, None] = ..., min_count: int = ..., **kwargs): ...
    product: Incomplete
    def mad(self, axis: Union[Axis, None] = ..., skipna: bool_t = ..., level: Union[Level, None] = ...) -> Union[Series, float]: ...
    def rolling(self, window: Union[int, timedelta, BaseOffset, BaseIndexer], min_periods: Union[int, None] = ..., center: bool_t = ..., win_type: Union[str, None] = ..., on: Union[str, None] = ..., axis: Axis = ..., closed: Union[str, None] = ..., step: Union[int, None] = ..., method: str = ...) -> Union[Window, Rolling]: ...
    def expanding(self, min_periods: int = ..., center: Union[bool_t, None] = ..., axis: Axis = ..., method: str = ...) -> Expanding: ...
    def ewm(self, com: Union[float, None] = ..., span: Union[float, None] = ..., halflife: Union[float, TimedeltaConvertibleTypes, None] = ..., alpha: Union[float, None] = ..., min_periods: Union[int, None] = ..., adjust: bool_t = ..., ignore_na: bool_t = ..., axis: Axis = ..., times: Union[str, np.ndarray, DataFrame, Series, None] = ..., method: str = ...) -> ExponentialMovingWindow: ...
    def __iadd__(self, other) -> NDFrameT: ...
    def __isub__(self, other) -> NDFrameT: ...
    def __imul__(self, other) -> NDFrameT: ...
    def __itruediv__(self, other) -> NDFrameT: ...
    def __ifloordiv__(self, other) -> NDFrameT: ...
    def __imod__(self, other) -> NDFrameT: ...
    def __ipow__(self, other) -> NDFrameT: ...
    def __iand__(self, other) -> NDFrameT: ...
    def __ior__(self, other) -> NDFrameT: ...
    def __ixor__(self, other) -> NDFrameT: ...
    def first_valid_index(self) -> Union[Hashable, None]: ...
    def last_valid_index(self) -> Union[Hashable, None]: ...
