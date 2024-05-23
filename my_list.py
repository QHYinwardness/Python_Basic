## add elements to list
## list.append()
motorcycles = ["honda", "yamada", "suzuki"]

motorcycles.append("ducati")
print(motorcycles)

## common scenario

motorcycles_list = []
motorcycles_list.append("honda")
motorcycles_list.append("honda")
motorcycles_list.append("honda")

print(motorcycles_list)


## insert elements
# list.insert(position, value)

motorcycles.insert(0, "first")
motorcycles.insert(1, "second")
print(motorcycles)


## delect elements
## 1. del
## 2. pop() if you want to use the delected value later

## delect the first element from the list
del motorcycles[0]

print(motorcycles)

## delect the second element from the list

del motorcycles[1]
print(motorcycles)

## list.pop()  delect the end element
my_motorcycles = ["honda", "yamaha", "suzuki"]

popped_motorcycles = my_motorcycles.pop()

print(my_motorcycles)


## list.pop(0)
## delect the first element
my_motorcycles.pop(0)
print(my_motorcycles)

## how to choose whether to use del or pop function
## if you won't use it anymore, use del; if you want to use the delected element later use pop

## remove when you only know the value of the element

my_motorcycles_remove = ["honda", "yamaha", "suzuki"]

my_motorcycles_remove.remove("yamaha")

print(my_motorcycles_remove)


## sort list

my_motorcycles_remove.append("a")
my_motorcycles_remove.append("b")
my_motorcycles_remove.append("c")

## 反转元素的排列顺序
my_motorcycles_remove.sort(reverse=True)

## 这些都是python list internal functions 都没有需要赋值
## my_motorcycles_remove = my_motorcycles_remove.pop()

## sorted : only for displaying

sorted(my_motorcycles_remove)


## use range() to create list - range(first,last,step)

numbers = list(range(1, 6, 2))

squares = []

for value in range(1, 11):
    squares.append(value**2)

print(squares)


## list comprehension
##
my_squares = [value**2 for value in range(1, 14)]

## new_list = [expression for member in iterable (if conditional)]
original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
prices = [i if i > 0 else 0 for i in original_prices]

## copy list

## copy the values not the index of the list

my_foods = ["pizza", "falafel", "carrot cake"]

## copy only the value of the list
# friend_foods = my_foods[:]

## friend_foods and my_foods point to the same memory
## so the value of both friend_foods and my_foods are the same
## and they will affect each other
friend_foods = my_foods


print(my_foods)
print(friend_foods)

my_foods.append("cannoli")
friend_foods.insert(1, "ice_cream")

print(my_foods)
print(friend_foods)

friend_foods.insert(0, "test")

print(my_foods)
print(friend_foods)

## tuple () : the elements in tuple couldn't be changed
## but the variable of the tuple could be reset

dimension = (200, 50)

print(dimension[0])

print(dimension[1])

# dimension[0] = 300

dimension = (400, 100)


print(dimension[0])

print(dimension[1])


unconfirmed_users = ["alice", "brian", "candace"]
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user)
    confirmed_users.append(current_user)

print("\n The following users have been confirmed")

for confirmed_user in confirmed_users:
    print(confirmed_user.title())

while "alice" in confirmed_users:
    confirmed_users.remove("alice")

print(confirmed_users)


## function arguments :

## 1. changeable argument :

## 2. unchangeable argument :

## 3. passing the index when you cannot confirm  how many arguments will be passed
unprinted_design = ["iphone case", "robot pendant", "dodecahedron"]
completed_models = []

# while unprinted_design:
#     current_designed = unprinted_design.pop()
#     completed_models.append(current_designed)

#     print("\n" + "print model : " + current_designed)

# for model in completed_models:
#     print(model.title())


def print_models(unprinted_design, completed_models):
    while unprinted_design:
        current_designed = unprinted_design.pop()
        completed_models.append(current_designed)
        print("\n" + "print model : " + current_designed)


def show_completed_models(completed_models):
    print("\n" + "the following models have been printed")
    for completed_model in completed_models:
        print(completed_model.title())


# print_models(unprinted_design, completed_models)
# show_completed_models(completed_models)

# print(len(unprinted_design))
# print(len(completed_models))

## cause you are passing the original list to the arguments but the copy of
## the original list so any actions inside the function
## will also change the value of those passing lists
## unprinted_design has been changed
## completed models has been changed


## nothing has changed in this situation cause we are passing the copy of the lists
# print_models(unprinted_design[:], completed_models[:])
# show_completed_models(completed_models[:])

# print(unprinted_design)
# print(completed_models)

## normally, we will definitely use the original which will save memory and time


# def make_pizza(*toppings):
#     print(toppings)


# make_pizza("pepperoni")
# make_pizza("mushrooms", "green peppers", "extra cheese")


# def make_pizza(size, *toppings):
#     print("\n making a " + str(size) + "-inch pizza with the following toppings")

#     for topping in toppings:
#         print("-" + topping)


# make_pizza(16, "pepperoni")
# make_pizza(8, "mushrooms", "green peppers", "extra cheese")


def built_profile(first, last, **info):
    customer_info = {}
    customer_info["first_name"] = first
    customer_info["last_name"] = last

    for key, value in info.items():
        customer_info[key] = value

    return customer_info


customer = built_profile("QIU", "Chris", gender="female", age=28)
print(customer)
