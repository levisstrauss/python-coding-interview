""""
Instruction

Lab Instructions: Functions, loops and data structures
In this lab you will be presented with a menu ordering system which will allow users to
input three choices for a select menu. You are tasked with completing the menu system so
that it returns and calculates the final bill for the user.


Tips: Before you Begin
To view your code and instructions side-by-side, select the following in your VSCode toolbar:
View -> Editor Layout -> Two Columns
To view this file in Preview mode, right click on this README.md file and Open Preview
Select your code file in the code tree, which will open it up in a new VSCode tab.
Drag your assessment code files over to the second column.
Great work! You can now see instructions and code at the same time.
Questions about using VSCode? Please see our support resources here.
To run your Python code
Select your Python file in the Visual Studio Code file tree
You can right click the file and select "Run Python File in Terminal" or run the file using the smaller
play button in the upper right-hand corner of VSCode.
(Select "Run Python File in Terminal" in the provided button dropdown)
Alternatively, you can follow lab instructions which use python3 commands to run your code in terminal.

There are three main objectives of this activity:
Create new functions to solve specific problems.
Gain experience of using for loops to iterate over different data collections.
Create and use data structures to store, retrieve and loop over data.

Exercise Instructions
Open the script ordering_system.py present inside the project folder.

Run the script and, when requested, enter in the three products of your choice based on the menu - 1 = espresso, 2 = coffee etc.

To run the script, open terminal and execute the following command.

python3 ordering_system.py
Extend the script to have a new function called calculate_subtotal.
It should accept one argument which is the order list and return the sum
of the prices of the items in the order list.

Implement calculate_tax() which calculates the tax of the subtotal.
The tax percentage is 15% of overall bill.

Implement summarize_order() which returns a list of the names of the items
that the customer ordered and the total amount (including tax) that they have to pay.
The orders should show the name and price.


Final Step: Let's submit your code!
Nice work! To complete this assessment:

Save your file through File -> Save
Select "Submit Assignment" in your Lab toolbar.
Your code will be autograded and return feedback shortly on the "Grades" tab.
You can also see your score in your Programming Assignment "My Submission" tab

"""

menu = {
    1: {"name": 'espresso',
        "price": 1.99},
    2: {"name": 'coffee',
        "price": 2.50},
    3: {"name": 'cake',
        "price": 2.79},
    4: {"name": 'soup',
        "price": 4.50},
    5: {"name": 'sandwich',
        "price": 4.99}
}


def calculate_subtotal(order):
    """ Calculates the subtotal of an order

    [IMPLEMENT ME]
        1. Add up the prices of all the items in the order and return the sum

    Args:
        order: list of dicts that contain an item name and price

    Returns:
        float = The sum of the prices of the items in the order
    """
    print('Calculating bill subtotal...')
    ### WRITE SOLUTION HERE
    subtotal = sum(item['price'] for item in order)
    return round(subtotal, 2)
    raise NotImplementedError()


def calculate_tax(subtotal):
    """ Calculates the tax of an order

    [IMPLEMENT ME]
        1. Multiply the subtotal by 15% and return the product rounded to two decimals.

    Args:
        subtotal: the price to get the tax of

    Returns:
        float - The tax required of a given subtotal, which is 15% rounded to two decimals.
    """
    print('Calculating tax from subtotal...')
    ### WRITE SOLUTION HERE
    tax = round(subtotal * 0.15, 2)
    return tax
    raise NotImplementedError()


def summarize_order(order):
    """ Summarizes the order

    [IMPLEMENT ME]
        1. Calculate the total (subtotal + tax) and store it in a variable named total (rounded to two decimals)
        2. Store only the names of all the items in the order in a list called names
        3. Return names and total.

    Args:
        order: list of dicts that contain an item name and price

    Returns:
        tuple of names and total. The return statement should look like

        return names, total

    """
    print_order(order)
    ### WRITE SOLUTION HERE
    subtotal = calculate_subtotal(order)
    tax = calculate_tax(subtotal)
    total = round(subtotal + tax, 2)
    names = [item['name'] for item in order]
    return names, total
    raise NotImplementedError()


# This function is provided for you, and will print out the items in an order
def print_order(order):
    print('You have ordered ' + str(len(order)) + ' items')
    items = []
    items = [item["name"] for item in order]
    print(items)
    return order


# This function is provided for you, and will display the menu
def display_menu():
    print("------- Menu -------")
    for selection in menu:
        print(f"{selection}. {menu[selection]['name'] : <9} | {menu[selection]['price'] : >5}")
    print()


# This function is provided for you, and will create an order by prompting the user to select menu items
def take_order():
    display_menu()
    order = []
    count = 1
    for i in range(3):
        item = input('Select menu item number ' + str(count) + ' (from 1 to 5): ')
        count += 1
        order.append(menu[int(item)])
    return order


'''
Here are some sample function calls to help you test your implementations.
Feel free to change, uncomment, and add these as you wish.
'''


def main():
    order = take_order()
    print_order(order)

    subtotal = calculate_subtotal(order)
    print("Subtotal for the order is: " + str(subtotal))

    tax = calculate_tax(subtotal)
    print("Tax for the order is: " + str(tax))

    items, total = summarize_order(order)
    print("Items ordered:", items)
    print("Total cost (including tax): $" + str(total))


if __name__ == "__main__":
    main()
