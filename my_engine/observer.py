import typing


class Observer:
    def __init__(self) -> None:
        self.target: typing.Any = None
        self.event_name: str = ""
        self.call_back: "typing.Callable" = None
        self.arguments = []
