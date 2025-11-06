#### Xavier Nazario
#### Student ID 2512208
##  Pseudocode
## Step 1 Import math module as m
## Step 2 Import cirfunc mod as cf
####        Main Function
## Step 1 Get radius of circle as float
## Step 2 Call area of circle function, using radius
##  as argument, format/display to 4 decimal places.
## Step 3 Call circumference function, using radius
##  as argument, format/display to 3 decimal places.
####        Area of Circle function (value returning
## Step 1 Define area(radius) with the formula to
##  calculate the area of circle. Use math module's
##  pi value.
## Step 2 Format/display area to 4 decimal.
####        Circumference Function (void func)
## Step 1 Define circum(radius) with formula to calculate
##  circumference of a circle.
## Step 2 Display/format results to 3 decimal places.

##  Code for program5_2.py

import math as m

def main():

# Get radius of circle then call both area/circumfernce functions
    radius = float(input('Enter radius of circle '))
    area = a(radius)
    print(f'The area of a circle with {radius} is {area:,.4f}')
    circum(radius)

def a(radius):
    return m.pi * radius **2
    
def circum(radius):
    c = 2 * m.pi * radius
    print(f'The circumference is {c:,.3f}')

if __name__ == '__main__':
    main()

####### I worked on this by myself

