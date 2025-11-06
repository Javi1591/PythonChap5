#### Xavier Nazario
## Student ID 2512205
####    Pseudocode
## Step 1 Import nazario5_2 mod as n
####    Main Function
## Step 1 Get radius as float
## Step 2 Call functions from nazario5_2 and set area
## Step 3 Format/display accordingly.

##  Code for program5_3.py

import nazario5_2 as n

def main():

# Get radius, set area, call functions, and display
    radius = float(input('Enter radius of circle '))
    area = n.a(radius)
    print(f'The area of a circle with {radius} is {area:,.4f}')
    n.circum(radius)
main()

###### I worked on this by myself.
