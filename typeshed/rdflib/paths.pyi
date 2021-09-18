from rdflib.term import Node as Node, URIRef as URIRef
from typing import Any, Callable, Union

ZeroOrMore: str
OneOrMore: str
ZeroOrOne: str

class Path:
    __or__: Callable[[Path, Union[URIRef, Path]], AlternativePath]
    __invert__: Callable[[Path], InvPath]
    __neg__: Callable[[Path], NegatedPath]
    __truediv__: Callable[[Path, Union[URIRef, Path]], SequencePath]
    __mul__: Callable[[Path, str], MulPath]
    def eval(self, graph, subj: Any | None = ..., obj: Any | None = ...) -> None: ...
    def __hash__(self): ...
    def __eq__(self, other): ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __ne__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...

class InvPath(Path):
    arg: Any
    def __init__(self, arg) -> None: ...
    def eval(self, graph, subj: Any | None = ..., obj: Any | None = ...) -> None: ...
    def n3(self): ...

class SequencePath(Path):
    args: Any
    def __init__(self, *args) -> None: ...
    def eval(self, graph, subj: Any | None = ..., obj: Any | None = ...): ...
    def n3(self): ...

class AlternativePath(Path):
    args: Any
    def __init__(self, *args) -> None: ...
    def eval(self, graph, subj: Any | None = ..., obj: Any | None = ...) -> None: ...
    def n3(self): ...

class MulPath(Path):
    path: Any
    mod: Any
    zero: bool
    more: bool
    def __init__(self, path, mod) -> None: ...
    def eval(self, graph, subj: Any | None = ..., obj: Any | None = ..., first: bool = ...) -> None: ...
    def n3(self): ...

class NegatedPath(Path):
    args: Any
    def __init__(self, arg) -> None: ...
    def eval(self, graph, subj: Any | None = ..., obj: Any | None = ...) -> None: ...
    def n3(self): ...

class PathList(list): ...

def path_alternative(self, other): ...
def path_sequence(self, other): ...
def evalPath(graph, t): ...
def mul_path(p, mul): ...
def inv_path(p): ...
def neg_path(p): ...
