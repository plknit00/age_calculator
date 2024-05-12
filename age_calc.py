from birthday import Birthday

#Reads and returns user input of birthday as one string
def birthday_input():
    date_string = input("Input birthday mm/dd/yyyy: ")
    # Maybe do some validation here? I.e. did they input something that looks
    # like mm/dd/yyyy?
    return date_string

#Splits the date_string into mdy into three integers
# Give this a better name. String parse just means "extracting some information
# from a string". Try to be more specific.
def stringParse(date_string):
    # new_string is also not descriptive. Maybe date_components or something?
    new_string = date_string.split("/")
    # Should validate that new_string has 3 elements before accessing them. If
    # date_string = "02/01", then new_string[2] won't exist.
    # Also, look up what will happen if int() receives a string that doesn't
    # parse to an integer. Probably want to handle this case somehow.
    month = int(new_string[0])
    day = int(new_string[1])
    year = int(new_string[2])

    return month, day, year

def main():
    birthday = birthday_input()
    # Maybe want to do tuple unpacking here (a nice python trick):
    # month, day, year = stringParse(birthday)
    int_birthday = stringParse(birthday)
    
    birthday1 = Birthday(int_birthday[0],int_birthday[1],int_birthday[2])
    print(birthday1.month)
    print(birthday1.day)
    print(birthday1.year)

main()
