# Anthony L. Pilla Checker.py
# The first six print statements are the welcome message and explanation of the program.

print("Hello, Today we are going to be labeling a chessboard.")
print("The first thing we need to know is that the rows across will be labeled A-H and the columns going up will be labeled 1-8.")
print("That means, A1 is in the bottom left corner and H8 is in the upper right corner.")
print("What I'll need from you is a letter and a number.")
print("Then I'll tell you whether your combined letter and number is either on a white or black square.")
print("Let's begin!")

# Let's get a letter and number combination from the user.

print("So, Lets get a letter A-H and a number 1-8: ")

# The following data set are lists are labeled all possible combinations of spaces on a chess board.
# Each list will contain a number 1-8.
# For those numbers they correspond to the rows.
# The data set runs from line 28-35.
# The variable on the left corresponds to the users input.
# The following are 9 If, Elif, Else statements to cross-reference from line 13 to the data sets in line 28-35.
# If the users input is in the data sets from line , then program output should read: "That combination is on the board!".
# If the users input is not in the data sets from line , then the programs output should read: "That combination is not on the board!".
# The Data sets for line  classifies the corresponding space to match a color (i.e. a1 = black space).
# The user input in line  will automatically respond here.
# The Data sets for line  are available to read both upper and lower case.
# When the user inputs response in line , the program will run the data sets then close immediately.

white_spaces_lower_abcd = ["a2", "a4", "a6", "a8", "b1", "b3", "b5", "b7", "c2", "c4", "c6", "c8", "d1", "d3", "d5", "d7"]
white_spaces_lower_efgh = ["e2", "e4", "e6", "e8", "f1", "f3", "f5", "f7", "g2", "g4", "g6", "g8", "h1", "h3", "h5", "h7"]
white_spaces_upper_ABCD = ["A2", "A4", "A6", "A8", "B1", "B3", "B5", "B7", "C2", "C4", "C6", "C8", "D1", "D3", "D5", "D7"]
white_spaces_upper_EFGH = ["E2", "E4", "E6", "E8", "F1", "F3", "F5", "F7", "G2", "G4", "G6", "G8", "H1", "H3", "H5", "H7"]
black_spaces_lower_abcd = ["a1", "a3", "a5", "a7", "b2", "b4", "b6", "b8", "c1", "c3", "c5", "c7", "d2", "d4", "d6", "d8"]
black_spaces_lower_efgh = ["e1", "e3", "e5", "e7", "f2", "f4", "f6", "f8", "g1", "g3", "g5", "g7", "h2", "h4", "h6", "h8"]
black_spaces_upper_ABCD = ["A1", "A3", "A5", "A7", "B2", "B4", "B6", "B8", "C1", "C3", "C5", "C7", "D2", "D4", "D6", "D8"]
black_spaces_upper_EFGH = ["E1", "E3", "E5", "E7", "F2", "F4", "F6", "F8", "G1", "G3", "G5", "G7", "H2", "H4", "H6", "H8"]
combined_letters_numbers = str(input())
if combined_letters_numbers in white_spaces_lower_abcd:
    print("That combination is on the board!")
    print()
    print("You are on a White Space!")
elif combined_letters_numbers in white_spaces_lower_efgh:
    print("That combination is on the board!")
    print()
    print("You are on a White Space!")
elif combined_letters_numbers in white_spaces_upper_ABCD:
    print("That combination is on the board!")
    print()
    print("You are on a White Space!")
elif combined_letters_numbers in white_spaces_upper_EFGH:
    print("That combination is on the board!")
    print()
    print("You are on a White Space!")
elif combined_letters_numbers in black_spaces_lower_abcd:
    print("That combination is on the board!")
    print()
    print("You are on a Black Space!")
elif combined_letters_numbers in black_spaces_lower_efgh:
    print("That combination is on the board!")
    print()
    print("You are on a Black Space!")
elif combined_letters_numbers in black_spaces_upper_ABCD:
    print("That combination is on the board!")
    print()
    print("You are on a Black Space!")
elif combined_letters_numbers in black_spaces_upper_EFGH:
    print("That combination is on the board!")
    print()
    print("You are on a Black Space!")
else:
    print("That combination is not on the board")
    print()
    print("Thank you for playing!")
    exit()



