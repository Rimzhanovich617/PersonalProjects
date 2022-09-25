
birthdays_dictionary = {"Jonathan Larson": "February 4th, 1960", "Jim Carrey" : "January 17th, 1962",
                        "Malcolm Gladwell" : "September 3rd, 1963"}

print("Hello and welcome to the Birthday Dcitionary!")
print("I know the Birthday's of: Jonathan Larson, Jim Carrey, and Malcolm Gladwell.")
print("Which one would you like to see? Write below: ")
users_guess = input()

if users_guess in birthdays_dictionary:
    print(birthdays_dictionary[users_guess])

else:
    print("Sorry that's not available!")
    exit()











