class Time:
    def __init__(self, hour, minute, second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def __add__(self, other):
        total_seconds = (
            self.__hour * 3600 + self.__minute * 60 + self.__second +
            other.__hour * 3600 + other.__minute * 60 + other.__second
        )

        hour = total_seconds // 3600
        minute = (total_seconds % 3600) // 60
        second = total_seconds % 60

        return Time(hour, minute, second)

    def display(self):
        print(self.__hour, ":", self.__minute, ":", self.__second)



t1 = Time(2, 30, 40)
t2 = Time(1, 40, 30)


t3 = t1 + t2

print("First Time:")
t1.display()

print("Second Time:")
t2.display()

print("Sum of Two Times:")
t3.display()

