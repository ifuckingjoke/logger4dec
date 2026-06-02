from typing import Any, Callable, TypeVar

_F = TypeVar("_F", bound=Callable[..., Any])

class Logger:
    foreground: int
    style: int
    background: int

    def __init__(
        self,
        *,
        foreground: int = ...,
        style: int = ...,
        background: int = ...,
    ) -> None: ...

    def log(self, text: str) -> Callable[[_F], _F]: ...