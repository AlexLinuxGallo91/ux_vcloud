import time
import datetime


class Timer:
    initial_time = 0.0
    ended_time = 0.0

    @staticmethod
    def get_actual_time():
        return time.time()

    @staticmethod
    def get_diff_total_time(ended_time: float, initial_time: float):
        return ended_time - initial_time

    @staticmethod
    def start_time():
        Timer.initial_time = time.time()

    @staticmethod
    def stop_time():
        Timer.ended_time = time.time()

    @staticmethod
    def get_time_in_seconds_float():
        return round(Timer.ended_time - Timer.initial_time, 2)

    @staticmethod
    def get_string_datetime():
        return str(datetime.timedelta(
            seconds=int(Timer.get_time_in_seconds_float())))
