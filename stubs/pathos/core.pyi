from _typeshed import Incomplete

def copy(source, destination: Incomplete | None = ..., **kwds): ...
def execute(command, host: Incomplete | None = ..., bg: bool = ..., **kwds): ...
def kill(pid, host: Incomplete | None = ..., **kwds): ...
def getpid(target: Incomplete | None = ..., host: Incomplete | None = ..., all: bool = ..., **kwds): ...
def getppid(pid: Incomplete | None = ..., host: Incomplete | None = ..., group: bool = ...): ...
def getchild(pid: Incomplete | None = ..., host: Incomplete | None = ..., group: bool = ...): ...
def randomport(host: Incomplete | None = ...): ...
def connect(host, port: Incomplete | None = ..., through: Incomplete | None = ...): ...
def serve(server, host: Incomplete | None = ..., port: Incomplete | None = ..., profile: str = ...): ...
