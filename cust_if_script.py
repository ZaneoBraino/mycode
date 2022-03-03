#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   if, elif, else - A simple program using conditionals to make a decision."""


message = 'Your grade is  '

# wrap connection in a float() to accept decimals as numbers
grade = float(input("What is you grade percentage without inputing the %"))

# if input value was higher or equal to 25
if 100 >= grade >= 90:
    message = message + 'an A'
elif 90 > grade >= 80:
    message = message + 'a B'
elif 80 > grade >= 70:
    message = message + 'a C'
elif 70 > grade >= 60:
    message = message + 'a D'

elif 60 > grade:
    message = message + 'a F'
elif grade > 100:
    message = message + 'Over an A?  Did you do extra credit?'
else:
    message = message + 'Seems like you dont have any grades.'
print(message)

