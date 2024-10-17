# import time
# from datetime import datetime
# print(datetime.now())
# print(time.strftime('%c'))  # day month date time year
# print(time.strftime('%x'))  # date
# print(time.strftime('%X'))  # time

import time
# %d for day
# %m for month
# %Y for year
# %H for hours(24-hour)
# %I for hours(12-hour)
# %M for minutes
# %S for second
# %p for AM/PM indicator


# date
a = time.strftime('%d/%m/%Y')
print("\nDate of today :", a)

# 24-hour format
# print(time.strftime('%H:%M:%S'))

# 12-hour format
b = time.strftime('%I:%M:%S %p')
print("Time now      :", b)

'''
hour = int(time.strftime('%I'))
am_pm = (time.strftime('%p'))

if (am_pm == "AM" and 0 < hour < 12):
    print("Good Morning.")
elif (am_pm == "PM" and (hour == 12 or 1 <= hour < 5)):
    print("Good Afternoon.")
elif (am_pm == "PM" and 5 <= hour < 7):
    print("Good Evening.")
else:
    print("Good Night.")

'''

hour = int(time.strftime('%H'))
if (0 < hour < 12):
    print("Good Morning.")
elif (12 <= hour < 18):
    print("Good Afternoon.")
elif (18 <= hour < 21):
    print("Good Evening.")
else:
    print("Good Night.")


