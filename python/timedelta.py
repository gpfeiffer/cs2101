class Time:
    """a class for time measurements"""

    def __init__(self, hours, minutes, seconds):
        self.hours = int(hours)
        self.minutes = int(minutes)
        self.seconds = round(float(seconds), 3)

    def __repr__(self):
        return f"Time({self.hours}, {self.minutes}, {self.seconds})"

    def __float__(self):
        return (self.hours * 60 + self.minutes) * 60 + self.seconds

    @staticmethod
    def hms(seconds):
        mins, secs = divmod(seconds, 60)
        return *divmod(mins, 60), secs

    def __add__(self, other):
        return Time(*Time.hms(float(self) + float(other)))

    def __rmul__(self, other):
        return Time(*Time.hms(other * float(self)))

    def __neg__(self):
        return -1 * self

    def __sub__(self, other):
        return self + -other
