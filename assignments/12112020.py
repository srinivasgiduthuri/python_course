# Create two more properties one is seconds and the other is minutes, then create a property called total_seconds
# which is a read-only property. Also create a one more property called value which must return hh:mm:ss AM/PM. Also
# create a one more property called value_24 which must return hh:mm:ss
class Time:
    def __init__(self, hours, minutes, seconds):
        self.__h = hours
        self.__m = minutes
        self.__s = seconds

    @property
    def hours(self):
        return self.__h

    @hours.setter
    def hours(self, value):
        if 0 <= value <= 23:
            self.__h = value
        else:
            raise ValueError("Invalid hours")

    @property
    def minutes(self):
        return self.__m

    @minutes.setter
    def minutes(self, value):
        if 0 <= value <= 59:
            self.__m = value
        else:
            raise ValueError("Invalid minutes")

    @property
    def seconds(self):
        return self.__s

    @seconds.setter
    def seconds(self, value):
        if 0 <= value <= 59:
            self.__s = value
        else:
            raise ValueError("Invalid seconds")

    @property
    def total_seconds(self):
        return (self.__h * 60 * 60) + (self.__m * 60) + self.__s

    @property
    def value(self):
        if 0 <= self.__h < 12:
            return f"{self.__h}:{self.__m}:{self.__s} A.M."
        else:
            return f"{self.__h - 12}:{self.__m}:{self.__s} P.M."

    @property
    def value_24(self):
        return f"{self.__h}:{self.__m}:{self.__s}"


t1 = Time(10, 35, 45)
print(t1.total_seconds)
print(t1.value)
print(t1.value_24)
t1.hours = 18
print(t1.total_seconds)
print(t1.value)
print(t1.value_24)


class Cricketer:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def print(self):
        print(self.name)
        print(self.country)


class Batsmen(Cricketer):
    def __init__(self, name, country, runs):
        super().__init__(name, country)
        self.runs = runs

    def print(self):
        super().print()
        print(self.runs)

    def get_points(self):
        return self.runs / 50


class Bowler(Cricketer):
    def __init__(self, name, country, wickets):
        super().__init__(name, country)
        self.wickets = wickets

    def print(self):
        super().print()
        print(self.wickets)

    def get_points(self):
        return self.wickets / 2


batsmen = Batsmen("Steve", "Country1", 410)
batsmen.print()
print(batsmen.get_points())
bowler = Bowler("Mark", "Country2", 25)
bowler.print()
print(bowler.get_points())
# How much am I ready for taking the Django course on Udemy? Do I meet the required pre-requisite to start it?
