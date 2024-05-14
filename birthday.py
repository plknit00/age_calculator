class Birthday:
    #init construtor
    def __init__(self, month, day, year):
        self.month = month
        self.day = day
        self.year = year

    def leapDayCheck(self):
        if (((self.year % 4) == 0) and (self.day == 29) 
            and (self.month == 2)):
            print("This person is a Leap Day baby!")

    def printAge(self):
        age = 0 
        #if statement that checks if it is before Dec 25 or after
        if (self.month < 12) or ((self.month == 12) and (self.day <=25)):
            age = 2050 - self.year
        else:
            age = 2049 - self.year
        print("This person will be " +str(age) + " years old!" )

        if age > 100:
            print("This person is unlikely to celebrate this Christmas...")

        #reference function that outputs leap day/year birthday
        self.leapDayCheck()


