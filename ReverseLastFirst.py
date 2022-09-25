print("Hello! I'm going to write your first and last name backwards!")
print("What is your first name?")

first_name = input()

print("Excellent! What is your last name?")

last_name = input()

print("It's a pleasure to meet you", first_name, last_name, "!")

print("Now, I'm going to write your name backwards! ")

full_name = str(first_name + ' ' + last_name)
strlength = len(full_name)
slicedString = full_name[strlength::-1]
print(slicedString)