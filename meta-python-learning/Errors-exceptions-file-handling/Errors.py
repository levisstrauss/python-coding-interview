def divide_by(a, b):
    return a / b


try:
    ans = divide_by(40, 0)
except ZeroDivisionError as e:
    print(e, "we cannot divide by zero")
except Exception as e:
    print(e, "Something went wrong")

#------------------
# Starter code
items = [1, 2, 3, 4, 5]
try:
    item = items[6]
    print(item)
except IndexError as e:
    print(e)


#--------------------
# Starter code
def divide_by(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 0
    except Exception as e:
        print(e, 'Something went wrong!')


ans = divide_by(10, 0)
print(ans)

# --------------- File ------------
try:
    with open('file_does_not_exist.txt', 'r') as file:
        print(file.read())
except:
    print("Unable to locate file")

# -------------------------------
try:
    item = items[6]
    print(item)
except:
    print("The index does not exist in the list.")
