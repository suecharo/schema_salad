from typing import Any

def list2set(seq): ...
def first(seq): ...
def uniq(sequence, strip: int = ...): ...
def more_than(sequence, number): ...
def to_term(s, default: Any | None = ...): ...
def from_n3(s: str, default: Any | None = ..., backend: Any | None = ..., nsm: Any | None = ...): ...
def check_context(c) -> None: ...
def check_subject(s) -> None: ...
def check_predicate(p) -> None: ...
def check_object(o) -> None: ...
def check_statement(triple) -> None: ...
def check_pattern(triple) -> None: ...
def date_time(t: Any | None = ..., local_time_zone: bool = ...): ...
def parse_date_time(val): ...
def guess_format(fpath, fmap: Any | None = ...): ...
def find_roots(graph, prop, roots: Any | None = ...): ...
def get_tree(graph, root, prop, mapper=..., sortkey: Any | None = ..., done: Any | None = ..., dir: str = ...): ...
