import json

celebrities_birthdays = {

    "Jonathan Larson": "February 4th, 1960",
    "Jim Carrey" : "January 17th, 1962",
    "Malcolm Gladwell" : "September 3rd, 1963"
}

with open("Birthday Part II.py.json", "w") as f:
    json.dump(celebrities_birthdays, f)

print("Hello and welcome to the Birthday Dcitionary!")
print("I know the Birthday's of: Jonathan Larson, Jim Carrey, and Malcolm Gladwell.")
print("Which one would you like to see? Write below: ")
users_guess = input()

if users_guess in celebrities_birthdays:
    print(celebrities_birthdays[users_guess])

else:
    print("Your new celebrity birthday has been added")



