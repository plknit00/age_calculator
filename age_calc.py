from birthday import Birthday

#Snake case is underscore separating words no capital letters
#Camel case is capital letters and no underscores (first word is lowercase)

#Checks birthday input format mm/dd/yyyy
def checkBD_string(date_string):
    if (len(date_string) != 10):
        print("Incorrect Format, try again!")
        return False
    if ((date_string[2] != '/') or (date_string[5] != '/')):
        print("Incorrect Format, try again!")
        return False
        #does not catch a dash case

    return True
    
#Function checks to make sure the date is made up of integers 
def checkBD_Int(date_string):
    if not date_string[0:2].isnumeric():
        print("Input an integer.")
        return False
    if not date_string[3:5].isnumeric():
        print("Input an integer.")
        return False
    if not date_string[6:].isnumeric():
        print("Input an integer.")
        return False

    return True

#Function checks to make sure the integer values are valid
def check_bd_month(month):
    if (month < 1) or (month > 12):
        print("Month input does not make sense, try again!")
        return False
    return True

def check_bd_year(year):
    if (year < 0) or (year > 2050):
        print("Year must be between 0 and 2050.")
        return False
    return True

#months 1,3,5,7,8,10, and 12 have 31 days, 2 can have 28 or 29, rest have 30
def check_bd_day(month,day,self):
    #February check
    if (month == 2):
        if (self.leapDayCheck()):
            return True
        elif (day > 0) and (day < 29):
            return True
        print("Invalid date for February")
        return False
    #Months with 31 days check
    elif ((month == range(1,8,2)) or (month == range(8,13,2))):
        if (day > 0) and (day < 32):
            return True
        print("Invalid: Month does not have 31 days.")
        return False
    #Months with 30 days check
    else:
        if (day > 0) and (day < 31):
            return True
        print("Invalid: Month does not have 30 days")
        return False
    



#Reads and returns user input of birthday as one string
def birthday_input():
    date_string = input("Input birthday mm/dd/yyyy: ")
    
    return date_string

#Splits the date_string into mdy into three integers
def dateInt(date_string):
    date_components = date_string.split("/")
    month = int(date_components[0])
    day = int(date_components[1])
    year = int(date_components[2])

    return month, day, year

def check_conditions(birthday):
    count = 0
    #Checks if the string is the correct date format of MM/DD/YYYY
    if (checkBD_string(birthday) == True):
        count += 1
    else:
        return count
    
    #Checks if the strings is comprised of integers
    if (checkBD_Int(birthday) == True):
        count += 1 
    else:
        return count

    #int_birthday = dateInt(birthday) may have to revert back to if m, d, y doesn't work
    month, day, year = dateInt(birthday)

    #Check if the month is within a reasonable range
    if (check_bd_month(month) == True):
        count += 1
    else:
        return count

    #Check if the year is within a reasonable range
    if (check_bd_year(year) == True):
        count += 1
    else:
        return count

    birthday1 = Birthday(month, day, year)

    #Checks if the day is within a reasonable range
    if (check_bd_day(month, day, birthday1) == True):
        count += 1
    
    return count

    



def main():
    birthday = birthday_input()
    count = check_conditions(birthday)

    while (count < 5):
        birthday = birthday_input()
        count = check_conditions(birthday)
    
    month, day, year = dateInt(birthday)
    birthday1 = Birthday(month, day, year)
    #birthday1 = Birthday(int_birthday[0],int_birthday[1],int_birthday[2]) 
    birthday1.printAge()




main()