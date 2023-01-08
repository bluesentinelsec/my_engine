from typing import List

import my_engine.event as event
import my_engine.observer as observer
import my_engine.singleton as singleton


class EventManager(metaclass=singleton.SingletonMeta):

    def __init__(self) -> None:
        self.queued_events: List["event.Event"] = []
        self.observers: List["observer.Observer"] = []

    def subscribe_event(self, target, event_name, call_back, arguments):
        observer_i = observer.Observer()
        observer_i.target = target
        observer_i.event_name = event_name
        observer_i.call_back = call_back
        observer_i.arguments = arguments
        self.observers.append(observer_i)

    def unsubscribe_event(self, target, event_name):
        for obsrv in self.observers:
            if target == obsrv.target and event_name == obsrv.event_name:
                self.observers.remove(obsrv)

    def queue_event(self, event: "event.Event"):
        self.queued_events.append(event)

    def update_observers(self):

        # return early if there are no queued events
        if len(self.queued_events) <= 0:
            return

        # iterate over each queued event
        # and notify observers
        for event in self.queued_events:

            # for each observer
            for obsrv in self.observers:

                # does observer care about this event?
                if event.get_type() == obsrv.event_name:

                    # execute observer callback
                    obsrv.call_back(obsrv.arguments)

        # pop event from the queue
        self.queued_events.remove(event)
