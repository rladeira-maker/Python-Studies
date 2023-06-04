class Time:
    def __init__(self, hour, minutes):
        self.hour = hour
        self.minutes = minutes
     
    def normalize(self):
        hour = self.hour
        minutes = self.minutes
         
        quotient = minutes / 60
        if quotient > 0:
            hour += quotient
            minutes = minutes % 60
         
        self.hour = hour
        self.minutes = minutes
         
        return self
     
    def __add__(self, t):
        """add two times (sum)"""
        hour = self.hour + t.hour
        minutes = self.minutes + t.minutes
        res = Time(hour, minutes)
        res.normalize()
        return res
     
    def __mul__(self, k):
        """multiply a time and an integer constant k (product)"""
        hour = self.hour * k
        minutes = self.minutes * k
        res = Time(hour, minutes)
        res.normalize()
        return res
     
    def __lt__(self, t):
        """less than"""
        if self.hour < t.hour or (self.hour == t.hour and self.minutes < t.minutes):
            return True
        else:
            return False
     
    def __eq__(self, t):
        """equal"""
        if self.hour == t.hour and self.minutes == t.minutes:
            return True
        else:
            return False
     
    def __le__(self, t):
        """less or equal"""
        return self < t or self == t
     
    def __gt__(self, t):
        """greater than"""
        return not self <= t
     
    def __ge__(self, t):
        """greater or equal"""
        return self > t or self == t
     
    def __ne__(self, t):
        """not equal"""
        return not self == t
     
    def __str__(self):
        hour = fill(str(self.hour), 2, '0')
        minutes = fill(str(self.minutes), 2, '0')
        return '%s:%s' % (hour, minutes)

def fill(s, size, c=' ', position='before'):
    """s: string; c: char"""
    if position == 'before':
        s = c * (size - len(s)) + s
    elif position == 'after':
        s += c * (size - len(s))
    return s

def generate_timetable(start_time, interval=Time(0, 15), times=5, end_time=None):
    timetable = []
     
    if end_time is None:
        end_time = start_time + interval*times
     
    time = start_time
    while time < end_time:
        timetable.append(tuple([time, time + interval]))
        time += interval
     
    return timetable

def main():
    start_time = Time(8, 0)
    end_time = Time(18, 15)
    for start, end in generate_timetable(start_time, end_time=end_time):
    print '%s-%s' % (start, end)
if __name__ == '__main__':
    main()
