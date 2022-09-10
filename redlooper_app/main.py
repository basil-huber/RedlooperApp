import pygame

from redlooper_app.looper_osc import Looper
from redlooper_app.pypedal import PyPedal
from threading import Event
import logging
import sys

from redlooper_app.gui.looper_widget import LooperWidget, State

SCREEN_RES = (480, 320)
CENTER = (int(SCREEN_RES[0] / 2), int(SCREEN_RES[1] / 2))
FPS = 10


def main():
    logging.basicConfig(filename='redlooper_app.log', level=logging.DEBUG, format='%(asctime)s %(message)s')
    logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))
    logging.info('------------- Starting ---------------')

    try:
        pygame.init()
        pygame.mouse.set_visible(False)
        screen = pygame.display.set_mode(SCREEN_RES, 0, 32)
        lpw = LooperWidget(screen, color=(255, 0, 0), center=CENTER, radius=100, linewidth=20)

        looper_connected_event = Event()
        def looper_connected():
            looper_connected_event.set()
            logging.info('Looper connected')

        pedal = PyPedal()

        with Looper(on_connected=looper_connected) as looper:
            #######################################
            # wait for looper and pedal connected #
            #######################################
            looper_connected_event.wait()

            ###########################
            # Connect buttons to looper #
            ###########################
            def button_left_released():
                print('left released')
                # looper_state = looper.get_state()
                # if looper_state in [Looper.State.MUTED_OFF, Looper.State.OFF, Looper.State.UNKNOWN,
                #                     Looper.State.RECORDING]:
                looper.record()
                # else:
                #     looper.multiply()

            def button_left_released_long():
                print('left released LONG')
                looper.undo()

            def button_right_released():
                print('right released')
                looper.mute()

            def button_right_released_long():
                print('right released LONG')
                looper.reset()

            def state_changed_callback(state):
                if state in [Looper.State.RECORDING, Looper.State.OVERDUBBING, Looper.State.MULTIPLYING,
                             Looper.State.INSERTING, Looper.State.REPLACING, Looper.State.ONESHOT, Looper.State.SUBSTITUTE]:
                    lpw.set_state(State.RECORDING)
                elif state in [Looper.State.PLAYING, Looper.State.MUTED]:
                    lpw.set_state(State.PLAYING)
                else:
                    lpw.set_state(State.PAUSED)
                # if state == Looper.State.RECORDING:
                #     lpw.set_mode(lpw.Mode.PULSING)
                # else:
                #     lpw.set_mode(lpw.Mode.FILLING)

            pedal.button_left.set_callback_released(button_left_released)
            pedal.button_left.set_callback_released_long(button_left_released_long)
            pedal.button_right.set_callback_released(button_right_released)
            pedal.button_right.set_callback_released_long(button_right_released_long)

            looper.set_loop_position_update_callback(lpw.set_loop_position)
            looper.set_loop_length_update_callback(lpw.set_loop_length)
            looper.set_state_callback(state_changed_callback)

            ###########################
            #       Main loop         #
            ###########################
            lpw.run(FPS)
    except:
        logging.exception('Exception')
        pass


if __name__ == '__main__':
    main()

