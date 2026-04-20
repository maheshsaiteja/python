n = int(input("Enter seconds: "))

class Time:
    def convert(self, n):
        self.hours = n // 3600
        self.minutes = (n % 3600) // 60
        self.seconds = n % 60

    def display(self):
        print("Hours:", self.hours)
        print("Minutes:", self.minutes)
        print("Seconds:", self.seconds)

t = Time()
t.convert(n)
t.display()