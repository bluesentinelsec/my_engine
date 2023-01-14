import logging

import pygame
import my_engine.event as event_t
import my_engine.event_manager as ev
import my_engine.keyboard


class Subscriber:
    def __init__(self) -> None:
        # create event manager singleton
        self.event_manager_ptr = ev.EventManagerSingleton()

    def subscribe_pushed_space(self):
        self.event_manager_ptr.subscribe_event(
            target=self, event_name="pushed_space", call_back=self.on_pushed_space, arguments=["one", "two", "three"])

    def on_pushed_space(self, arguments):
        logging.info("We observed a 'pushed_space' event!")
        print(f"Arguments: {arguments}")


def main():
    logging.basicConfig(level=logging.INFO,
                        format='%(levelname)s (%(filename)s:%(lineno)s) %(message)s')

    pygame.init()
    screen = pygame.display.set_mode((320, 200))
    kb = my_engine.keyboard.KeyBoard()

    # create an event manager
    # this object notifies subscribers/observers
    # of events they care about
    event_manager = ev.EventManagerSingleton()

    # create a new event: 'pushed_space'
    # our observer will subscribe to this event
    pushed_space_event = event_t.Event("pushed_space")

    # create the observer/subscriber
    ent = Subscriber()

    # subscribe to the 'pushed_space' event
    ent.subscribe_pushed_space()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        # emit 'pushed_space' event when space bar is pressed
        if kb.is_key_pressed_once(pygame.K_SPACE):
            pushed_space_event.emit_event()

        screen.fill((0, 0, 0))

        # notify observers/subscribers of any pending events
        # this will cause our Subscriber entity to execute
        # the call back function, 'on_pushed_space'
        event_manager.update_observers()

        pygame.display.update()


if __name__ == "__main__":
    main()
