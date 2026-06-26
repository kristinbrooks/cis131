"""
    script: timewithproperties.py
    action: modification of the textbook's Time class to store time as seconds since midnight
    author: Kristin Brooks
    date:   06/25/26
"""

class Time:
    """Class Time with read-write properties."""

    def __init__(self, hour=0, minute=0, second=0):
        """Initialize."""
        self._total_seconds = 0
        self.hour = hour
        self.minute = minute
        self.second = second

    @property
    def hour(self):
        """Return the hour."""
        hour = self._total_seconds // 3600
        return hour

    @hour.setter
    def hour(self, hour):
        """Set the hour."""
        if not (0<= hour <= 23):
            raise ValueError(f'Hour ({hour}) must be 0 - 23')

        self._total_seconds = hour * 3600 + self.minute * 60 + self.second

    @property
    def minute(self):
        """Return the minute."""
        minute_and_second = self._total_seconds % 3600
        minute = minute_and_second // 60
        return minute

    @minute.setter
    def minute(self, minute):
        """Set the minute."""
        if not (0<= minute <= 59):
            raise ValueError(f'Minute ({minute}) must be 0 - 59')

        self._total_seconds = self.hour * 3600 + minute * 60 + self.second

    @property
    def second(self):
        """Return the second."""
        minute_and_second = self._total_seconds % 3600
        second = minute_and_second % 60
        return second

    @second.setter
    def second(self, second):
        """Set the second."""
        if not (0<= second <= 59):
            raise ValueError(f'Second ({second}) must be 0 - 59')

        self._total_seconds = self.hour * 3600 + self.minute * 60 + second

    def set_time(self, hour=0, minute=0, second=0):
        """Set the values of hour, minute, and second."""
        self.hour = hour
        self.minute = minute
        self.second = second

    def __repr__(self):
        """Return Time string for repr()."""
        return (f'Time(hour={self.hour}, minute={self.minute}, second={self.second})')

    def __str__(self):
        """Print Time in 12-hour clock format."""
        return (('12' if self.hour in (0,12) else str(self.hour % 12)) +
                f':{self.minute:0>2}:{self.second:0>2}' +
                (' AM' if self.hour < 12 else ' PM'))
