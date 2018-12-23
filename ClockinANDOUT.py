import datetime as da
from datetime import timedelta as td

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
    b = input("Do you want to clock in or out")
    db_value = str(a + ", " + in_or_out(b))
    filename = str(a + da.datetime.now().strftime("%d""%m""%y") + ".txt")
    return db_value, filename


def open_add_file(db_value, filename):
    f = open(filename, "a+")
    f.write(db_value + "\n")
    f.close()


db_value, filename = interface()

open_add_file(db_value, filename)
print(db_value)
print(filename)
print(time_stamp())
x = "in"

print(in_or_out(x))
y = "out"
print(in_or_out(y))
