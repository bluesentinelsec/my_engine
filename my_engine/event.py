import uuid

import event_manager


class Event():

    def __init__(self, event_type: str) -> None:

        self.event_type: str = event_type
        self.guid: str = str(uuid.uuid4())
        self.event_manager_ptr: "event_manager.EventManager" = event_manager.EventManager()

    def get_guid(self) -> str:
        return self.guid

    def get_type(self) -> str:
        return self.event_type

    def emit_event(self):
        self.event_manager_ptr.queue_event(event=self)
