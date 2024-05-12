from age_calculator import birthday

#Reads and returns user input of birthday as one string
def birthday_input():
    date_string = input("Input birthday mm/dd/yyyy: ")
    return date_string

#Splits the date_string into mdy into three integers
def stringParse(date_string):
    new_string = date_string.split("/")
    month = int(new_string[0])
    day = int(new_string[1])
    year = int(new_string[2])

    return month, day, year

def main():
    birthday = birthday_input()
    int_birthday = stringParse(birthday)
    
    birthday1 = Birthday(int_birthday[0],int_birthday[1],int_birthday[2])
    print(birthday1.month)
    print(birthday1.day)
    print(birthday1.year)

main()