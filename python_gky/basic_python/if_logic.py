import datetime
import datetime

a = int(input("Enter number : "))

if a > 2:
    print("yes")
else:
    print("no")


#to show a multi-way decision based on several condition , we use if elif statement

#if elif statement 

a = 30
b = 20
if a > b:
    print("a is greater then b  ")
elif a ==b:
    print("a is equal to b")
elif b > a:
    print('b is greater than a')


#if elif else statement 
day = datetime.datetime.now().strftime("%A").lower()

days_of_week = {
    "monday": "monday",
    "tuesday": "tuesday",
    "wednesday": "wednesday",
    "thursday": "thursday",
    "friday": "friday",
    "saturday": "saturday",
    "sunday": "sunday"
}

if day in days_of_week:
    print(days_of_week[day])
else:
    print("invalid day")



import unittest
import datetime
from if_logic import days_of_week

class TestIfLogic(unittest.TestCase):

    def test_valid_day(self):
        for day in days_of_week:
            self.assertEqual(days_of_week[day], days_of_week[day.lower()])

    def test_invalid_day(self):
        invalid_day = "InvalidDay"
        self.assertEqual("invalid day", days_of_week.get(invalid_day.lower(), "invalid day"))

if __name__ == '__main__':
    unittest.main()


