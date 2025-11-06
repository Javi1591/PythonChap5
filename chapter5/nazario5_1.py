#### Xavier Nazario
#### Student ID 2512208
## Pseudocode for program5_1.py
###         Main Function
# Step 1 Import subtotal.py module
# Step 2 Get number of items being bought.
# Step 3 In a for loop, get item(s) description, price,
#   and quantity based off users input than call subtotal
#   module.
# Step 4 Calculate total by adding all the subtotals and
#   display/format accordingly.


## Code

# Import module
import subtotal as sb

# Define main function and get number of items then loop
def main():
    num_items = int(input('How many different items are '
                          'being purchased? '))
    for item_num in (1,num_items):
        item = input(f'Enter description of item {item_num} ')
        price = float(input(f'Enter price of item {item_num} '))
        quant = int(input(f'Enter the quantity for item {item_num} '))
        print(sb.subtotal(item, price, quant))
    print()
# Calculate total order
   
##      print(f'Your total is ${total:,.2f}')
if __name__ == '__main__'
    main()
## Colloboration Statement: I worked on this by myself.
