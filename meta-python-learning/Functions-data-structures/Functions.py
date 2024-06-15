def get_total(a, b):
    #local variable declared inside a function
    total = a + b;
    return total


print(get_total(5, 2))

# Accessing variable outside of the function:

special = 5


def get_total(a, b):
    #enclosed scope variable declared inside a function
    total = a + b
    print(special)

    def double_it():
        #local variable
        double = total * 2
        print(special)

    double_it()

    return total
