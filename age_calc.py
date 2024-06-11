from birthday import Birthday

#Checks birthday input format mm/dd/yyyy
def checkBD_string(date_string):
    if (len(date_string) != 10):
        return False
    if ((date_string[2] != '/') or (date_string[5] != '/')):
        return False
        #does not catch a dash case

    return True
    
#Function checks to make sure the date is made up of integers 
def checkBD_Int(date_string):
    if not date_string[0:2].isnumeric():
        return False
    if not date_string[3:5].isnumeric():
        return False
    if not date_string[6:].isnumeric():
        return False

    return True

#Function checks to make sure the integer values are valid


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

def main():
    birthday = birthday_input()
    while (checkBD_string(birthday) == False):
        birthday = birthday_input()
    
    while (checkBD_Int(birthday) == False):
        birthday = birthday_input()


    #check mdy function while loop
    int_birthday = dateInt(birthday)
    
    birthday1 = Birthday(int_birthday[0],int_birthday[1],int_birthday[2])
    birthday1.printAge()
    birthday1.leapDayCheck()




main()