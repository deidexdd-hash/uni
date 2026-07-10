from collections.abc import Callable
from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class DomainEvent:
    name: str
    payload: dict[str, Any] = field(default_factory=dict)


EventHandler = Callable[[DomainEvent], None]


class EventBus:
    def __init__(self) -> None:
        self._handlers: dict[str, list[EventHandler]] = {}

    def subscribe(self, event_name: str, handler: EventHandler) -> None:
        self._handlers.setdefault(event_name, []).append(handler)

    def publish(self, event: DomainEvent) -> None:
        for handler in self._handlers.get(event.name, []):
            handler(event)
