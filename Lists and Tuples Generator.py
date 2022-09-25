print("Hello, we are going to create a List and Tuple Generator.")
print("What I need from you is a few numbers.")
print("These numbers will be formatted as a List and a Tuple: Let's Go!")

print("What numbers do you want, type them below with spaces to separate the numbers.")

users_numbers = input()

print("Now let's generate those numbers into a List and Tuple!")

users_list = users_numbers.split()
users_tuple = tuple(int(val) for val in users_numbers.split())
print("List: ", users_list)
print("Tuple: ", users_tuple)