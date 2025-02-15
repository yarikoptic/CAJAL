from typing import ChainMap

class DeepChainMap(ChainMap[_KT, _VT]):
    def __setitem__(self, key: _KT, value: _VT) -> None: ...
    def __delitem__(self, key: _KT) -> None: ...
