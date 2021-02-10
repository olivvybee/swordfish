from enum import Enum


class Status (Enum):
    OFFLINE = 1
    CONNECTED = 2
    PRINTING = 3
    PAUSED = 4


class Swordfish (object):
    def __init__(self, width, height, use_emulator=False):
        self._width = width
        self._height = height
        self._use_emulator = use_emulator
        self._status = Status.OFFLINE
        self._filename = ''
        self._progress = -1
        self._time_remaining = -1
        self._current_layer = -1
        self._total_layers = -1
        self._extruder_temp = -1
        self._bed_temp = -1

    def status_change(self, status):
        self._status = status
        self._draw()

    def print_started(self, filename, time_remaining, total_layers=-1):
        self._status = Status.PRINTING
        self._filename = filename
        self._time_remaining = time_remaining
        self._total_layers = total_layers
        self._current_layer = 1 if total_layers > 0 else -1
        self._draw()

    def print_finished(self):
        self._status = Status.CONNECTED
        self._filename = ''
        self._progress = -1
        self._time_remaining = -1
        self._current_layer = -1
        self._total_layers = -1
        self._draw()

    def progress_update(self, progress, time_remaining, current_layer=-1):
        self._progress = progress
        self._time_remaining = time_remaining
        self._current_layer = current_layer
        self._draw()

    def _draw(self):
        pass
