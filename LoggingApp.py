from kivy.app import App
from kivy.clock import Clock
from kivy.uix.label import Label
import logging
import threading
import time


def my_thread(log):
    for i in range(2 ** 20):
        time.sleep(1)
        log.info("WOO %s", i)


class MyLabelHandler(logging.Handler):

    def __init__(self, label, level=logging.NOTSET):
        logging.Handler.__init__(self, level=level)
        self.label = label

    def emit(self, record):
        """using the Clock module for thread safety with kivy's main loop"""

        def f(dt=None):
            self.label.text = self.format(record)  # "use += to append..."

        Clock.schedule_once(f)


class LoggingApp(App):
    def build(self):
        label = Label(text="showing the log here")
        log = logging.getLogger("MyLogger")
        log.level = logging.DEBUG
        log.addHandler(MyLabelHandler(label, logging.DEBUG))
        thread = threading.Thread(target=my_thread, args=(log,))
        thread.start()
        return label


if __name__ == '__main__':
    LoggingApp().run()
