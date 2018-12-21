# --------------------Imports--------------------#
from datetime import timedelta as td
import datetime as da
import calendar as ca


# --------------------Functions--------------------#

def lunch_func(t):  # Determines the amount of time is given as lunch
    if t == "1":
        return str("0030")
    elif t == "2":
        return str("0045")
    elif t == "3":
        return str("0100")
    elif t == "4":
        return str("0130")
    else:
        exit("Please enter a valid lunch option!")


def time_func(a):  # Converts HHMM string in to timedelta
    user_hours = int(a[:2])
    user_minute = int(a[2:5])
    b = td(hours=user_hours, minutes=user_minute)
    return b


def if_func(b, c):  # This is what enable you to check flex before 1:45 and 9am
    if c.hour < 9:
        afternoon_time = td(hours=int(7), minutes=int(30))
    else:
        afternoon_time = td(hours=int(3), minutes=int(45))
    balance = b
    lunch = lunch_func(input("Set time amount for lunch: '1' = 30 min, '2' = 45 min, '3' = 1 hr, '4' = 1 hr 30 min:"))
    flav = time_func(flex) + time_func(lunch) + afternoon_time
    balance = balance + time_func(lunch) + afternoon_time
    return lunch, flav, balance


def custom_time_func():  # This allows a custom time to be used for debugging purposes .
    q = input("Do you want to enter a custom time Y/N : ")
    if q == "y" or q == "Y":
        a = input("Enter a custom time in HHMM format : ")
        user_hours = int(a[:2])
        user_minute = int(a[2:5])
        diff = 60 * 60 * 24
        now = da.datetime(
            *da.datetime.fromtimestamp(ca.timegm(da.datetime.today().utctimetuple()) - diff).utctimetuple()[:3],
            hour=int(user_hours), minute=int(user_minute))
        return now
    else:
        now = da.datetime.now()
        return now


# --------------------Code and Variables--------------------#


now = custom_time_func()
flex = input("Enter your flex amount in HHMM:")
static_time = ["1600", "1700", "1730", "1800"]
static_flex = ["0200", "0100", "0030"]
lunch = 0
balance = now + time_func(flex)
now_hour_min = td(hours=now.hour, minutes=now.minute)
balance = td(hours=balance.hour, minutes=balance.minute)
flav = time_func(flex)


if ((now.hour <= 13 and now.minute <= 44) or (now.hour <= 12 and now.minute >= 45)) and now.hour >= 9:
    lunch, flav, balance = if_func(balance, now)

# --------------------Code and Printing--------------------#

print("Time when balance at 00:00 : " +str(balance))

if lunch != 0:
    print("Estimated Lunch time: "+str(lunch))

print("Date/Time of run: "+str(now))

if now.hour <= 16 :
    print("Balance at 4:00 pm : "+str(flav - (time_func(static_time[0]) - now_hour_min)))
if now.hour <= 17 :
    print("Balance at 5:00 pm : "+str(flav - (time_func(static_time[1]) - now_hour_min)))
if (now.hour <= 17 and now.minute <= 30) or (now.hour <= 16 and now.minute >= 31):
    print("Balance at 5:30 pm : "+str(flav - (time_func(static_time[2]) - now_hour_min)))
if now.hour <= 18 :
    print("Balance at 6:00 pm : "+str(flav - (time_func(static_time[3]) - now_hour_min)))

print("Time when at +2:00 : "+str(balance + time_func(static_flex[0])))
print("Time when at +1:00 : "+str(balance + time_func(static_flex[1])))
print("Time when at +0:30 : "+str(balance + time_func(static_flex[2])))
print("Time when at -0:30 : "+str(balance - time_func(static_flex[2])))
print("Time when at -1:00 : "+str(balance - time_func(static_flex[1])))
print("Time when at -2:00 : "+str(balance - time_func(static_flex[0])))
