http_status = 500

if http_status == 200 or http_status == 201:
    print('Success')
elif http_status == 400:
    print('Bad request')
elif http_status == 404:
    print('Not Found')
elif http_status == 500 or http_status == 501:
    print('server Error')
else:
    print('Unknown')

# ---- Doing the same using match ------
match http_status:
    case 200 | 201:
        print('Success')
    case 400:
        print()

    case _:
        print('Unknown')

# ------------- Loop----------------------
favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

for i in range(10):
    print('Looping...', i)

for idx, item in enumerate(favorites):
    print(idx, item)

count = 0

while count < len(favorites):
    print('I like this desert', favorites[count])
    count += 1

#Starter Code
favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

for dessert in favorites:
    if dessert == 'Pudding':
        print('Yes one of my favorite desserts is', dessert)
    else:
        print('No sorry, that dessert is not on my list')

#Starter Code
favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

for dessert in favorites:
    if dessert == 'Churros':
        continue
    print('Other desserts I like are', dessert)

#Starter Code
favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

for dessert in favorites:
    if dessert == 'Churros':
        pass
    print('Other desserts I like are', dessert)

# Nested loop -------------------------------

for i in range(10):
    # inner loop
    for j in range(10):
        print(0, end=' ')
    print()

import time

start_time = time.time()

# outer loop
for i in range(100):
    for j in range(100):
        print(0, end=' ')
    print()
print(round((time.time() - start_time), 2))

num_list = [33, 42, 5, 66, 77, 22, 16, 79, 36, 62, 78, 43, 88, 39, 53, 67, 89, 11]

for num in num_list:
    print(num)

num_list = [33, 42, 5, 66, 77, 22, 16, 79, 36, 62, 78, 43, 88, 39, 53, 67, 89, 11]

for num in num_list:
    if num > 45:
        print(num)

num_list = [33, 42, 5, 66, 77, 22, 16, 79, 36, 62, 78, 43, 88, 39, 53, 67, 89, 11]

for num in num_list:
    if num > 45:
        print('Over 45')
    else:
        print('Under 45')

num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]

for x,num in enumerate(num_list):
    if num == 36:
        print('Number found at ', x)



num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]

count = 0

for x,num in enumerate(num_list):
    count += 1
    if num == 36:
        print('Number found at ', x)

print(count)

num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]

count = 0

for x,num in enumerate(num_list):
    count += 1
    if num == 36:
        print('Number found at ', x)
        break

print(count)
