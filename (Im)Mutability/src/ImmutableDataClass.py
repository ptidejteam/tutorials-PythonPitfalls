from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class ImmutableDataClass:
    a: Any
    b: Any


@dataclass(frozen=True)
class ImmutableClass:
    a: Any
    b: Any

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def foo(self):
        self.a += 1
