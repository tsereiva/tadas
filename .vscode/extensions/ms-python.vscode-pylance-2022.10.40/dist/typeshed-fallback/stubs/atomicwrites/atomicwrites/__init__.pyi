from _typeshed import StrOrBytesPath
from collections.abc import Callable
from contextlib import AbstractContextManager
from typing import IO, Any, AnyStr
from typing_extensions import Literal

PY2: Literal[False]
DEFAULT_MODE: Literal["w"]

def replace_atomic(src: AnyStr, dst: AnyStr) -> None: ...
def move_atomic(src: AnyStr, dst: AnyStr) -> None: ...

class AtomicWriter:
    def __init__(self, path: StrOrBytesPath, mode: str = ..., overwrite: bool = ...) -> None: ...
    def open(self) -> AbstractContextManager[IO[Any]]: ...
    def _open(self, get_fileobject: Callable[..., IO[AnyStr]]) -> AbstractContextManager[IO[AnyStr]]: ...
    def get_fileobject(
        self, suffix: str = ..., prefix: str = ..., dir: StrOrBytesPath | None = ..., **kwargs: Any
    ) -> IO[Any]: ...
    def sync(self, f: IO[Any]) -> None: ...
    def commit(self, f: IO[Any]) -> None: ...
    def rollback(self, f: IO[Any]) -> None: ...

def atomic_write(
    path: StrOrBytesPath, writer_cls: type[AtomicWriter] = ..., **cls_kwargs: object
) -> AbstractContextManager[IO[Any]]: ...
