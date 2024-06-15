menu = ['expresso', 'mocha', 'latte', 'cappuccino']


def find_coffee(coffee):
    if coffee[0] == 'c':
        return coffee


#----- Map which take all the objects in list and applies a function
map_coffee = map(find_coffee, menu)
print(map_coffee)
for x in map_coffee:
    print(x)

# Filter-------------- do the same but return a new list with the true value
filter_coffee = filter(find_coffee, menu)
print(filter_coffee)
for x in filter_coffee:
    print(x)

#------------ list comprehension---------------
data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

# Ex1: List comprehension: updating the same list
data = [x + 3 for x in data]
print("Updating the list: ", data)

# Ex2: List comprehension: creating a different list with updated values
new_data = [x * 2 for x in data]
print("Creating new list: ", new_data)

# Ex3: With an if-condition: Multiples of four:
fourx = [x for x in new_data if x % 4 == 0]
print("Divisible by four", fourx)

# Ex4: Alternatively, we can update the list with the if condition as well
fourxsub = [x - 1 for x in new_data if x % 4 == 0]
print("Divisible by four minus one: ", fourxsub)

# Ex5: Using range function:
nines = [x for x in range(100) if x % 9 == 0]
print("Nines: ", nines)

# List comprehension:
data = [x + 3 for x in data]

# Regular for loop:
for x in range(len(data)):
    data[x] = data[x] + 3

# ---------- Set comprehension -------------

# Using range() function and no input list
usingrange = {x: x * 2 for x in range(12)}
print("Using range(): ", usingrange)

# Lists
months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Using one input list
numdict = {x: x ** 2 for x in number}
print("Using one input list to create dict: ", numdict)

# Using two input lists
months_dict = {key: value for (key, value) in zip(number, months)}
print("Using two lists: ", months_dict)

#------------- Set comprehension----------
set_a = {x for x in range(10, 20) if x not in [12, 14, 16]}
print(set_a)


#---------------- Generator comprehension----------
data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
gen_obj = (x for x in data)
print(gen_obj)
print(type(gen_obj))
for items in gen_obj:
    print(items, end=" ")
