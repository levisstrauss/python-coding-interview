"""

List, dictionary, tuple and set. These are all considered non-primitive data structures, meaning they are
classed as objects, this will be explored later in the course.
"""

# ----------------- list ------------------

list1 = [1, 2, 3, 4, 5]
# index, number
list1.insert(len(list1), 14)
list1.append(15)
list1.extend([12, 14])
list1.pop(4)

del list1[2]

print(list1, sep=" ")

# ----------------- tuple ------------------
# immutable
mu_tuple = (1, 'string', 4, 5)
print(mu_tuple.count('string'))
print(mu_tuple.index('string'))
for i in mu_tuple:
    print(i)
print(type(mu_tuple))

# ----------------- set() ------------------
# No duplicate unordered items
set_a = {1, 2, 3, 5}
set_a.add(45)
set_a.remove(2)
set_a.discard(2)  # Same
set_b = {1, 2, 3, 5}
# Union
print(set_a.union(set_b))
print(set_a | set_b)
# intersection
print(set_a.intersection(set_b))
print(set_a & set_b)

# Set a not in set b = difference
print(set_a.difference(set_b))  # using -
print(set_a - set_b)

# Symmetric In set a or b not both
print(set_a.symmetric_difference(set_b))
print(set_a ^ set_b)

# ----------------- Dictionary ---------------
# Note duplicate key
my_d = {1: "test", 'name': 'jim'}
print(my_d[1])
my_d[2] = 'Test 2'
del my_d[1]

for key, value in my_d.items():
    print(key + " : " + value)


# ----------------- args ------------------
# We can pass multiple value here as a parameters
def sum_of(*args):
    sum = 0
    for x in args:
        sum += x
    return sum


print(sum_of(4, 5, 6))


# ----------------- kwargs ------------------
def sum_of(*kwargs):
    sum = 0
    for K, V in kwargs.items():
        sum += V
    return round(sum, 2)


print(sum_of(4, 5, 6))

#----------------------------------- dict-------------

employee_list = [(12345, "John", "Kitchen"), (12458, "Paul", "House Floor")]


def get_employee(id):
    for employee in employee_list:
        if employee[0] == id:
            return {"id": employee[0], "name": employee[1], "department": employee[2]}


print(get_employee(12458))

employee_dict = {
    12345: {
        "id": "12345",
        "name": "John",
        "department": "Kitchen"
    },
    12458: {
        "id": "12458",
        "name": "Paul",
        "department": "House Floor"
    }
}


def get_employee_from_dict(id):
    return employee_dict[id];


print(get_employee_from_dict(12458));
