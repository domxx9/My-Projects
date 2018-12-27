import datetime as da
from datetime import timedelta as td

import flex_calc

def login():
    a = input("Please enter your name: ")
    print("Hello " + a)
    return a


def time_stamp():
    date = da.datetime.now().strftime("%d""-""%m""-""%Y"" ""%H"":""%M")
    return date



def in_or_out(a):
    if a == "in":
        b = time_stamp()+", IN"
    elif a == "out":
        b = time_stamp()+", OUT"
    else:
        exit("Seriously its not hard. Type in/out:")
    return b


def interface():
    a = login()
    print("Enter 1 to go to the flex calculator;")
    print("Enter 2 to view your flex;")
    print("Enter 3 to clock \"IN\".")
    print("Enter 4 to clock \"OUT\".")
    b = input("Please choose from the above options : ")
    if b == "3" or b == "4":
        db_value, filename = get_file_info(a, b)
        open_add_file(db_value, filename)
    elif b == "1":
        flex_calc.flex_calc()
    elif b == "2":
        print("not done yet")
    else:
        print("why have you done this")


def open_add_file(db_value, filename):
    f = open(filename, "a+")
    f.write(db_value + "\n")
    f.close()


def get_file_info(a, b):
    db_value = str(a + ", " + in_or_out(b))
    filename = str(a + da.datetime.now().strftime("%d""%m""%y") + ".txt")
    return db_value, filename

interface()
