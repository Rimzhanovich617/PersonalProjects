import pygame


print("Welcome landlubbers!", "\n")
print("I'm Captain Longshivers and this is the prized possession of the ocean, the ship Persphone.")
print("Type your name and hit enter.")
landlubber = input("And who may you be: ")

print("Welcome aboard", landlubber,"!", "\n")

print("I'm on the look out for a Narwal or Octopus. Do you want to help me, yes or no?")
print("Please type all in lowercase for the answers and hit enter.")

answer1 = input()


if answer1 == ("yes"):
    print("Excellent! Let's get ready to sail!", "\n")
elif answer1 == ("no"):
    print("Aw, to Davy Jones with ye then!")
    exit()
else:
    print("I'm afraid that doesn't work, sorry matey")
    exit()

print("Before we set sail, I want you to know a few things.",)
print("First where we are now is called Origin Zero.", "Somewhere out there is a Narwal and an Octopus.")
print("Our mission today is see if we can sight one of these fantastic beasts.", "\n")

print("Alright, now we can go in several directions: North, Northeast, East, Southeast, South, Southwest, West, and Northwest")
print("I'll be abbreviating these to: N, NE, E, SE, S, SW, W, NW.")
print("We will also be traveling in miles, tides move fast out here on the high seas!", "\n")


print("Now I'll teach you how to set sail of the ship Persphone.")
print("You can go in any direction by 1 mile increments.")
print("The max you can go is in a 5 mile radius from the Origin Point")
print("When we set sail you can jump to any point on the grid by using the below instructions.")
print("You have to chose North/South first then West/East second")
print("I.E. sailing 3 miles north and 2 miles east would land you on a square of NE32")
print("So SW 54 is South 5 miles and West 4 Miles.")

print("Alrighty matey! Let's set sail!")
print("Where shall we go, remember type N/S first then W/E then their corresponding miles.")




prompt  = "\nWhere shall we go: "
prompt += "\nEnter 'quit' and hit enter to end the program."

message = ""
while message != 'quit':
    message = input(prompt)
    N0 = ["N1", "N2", "N3", "N4", "N5"]
    n0 = ["n1", "n2", "n3", "n4", "n5"]
    NW1 = ["NW11", "NW12", "NW13", "NW14", "NW15"]
    nw1 = ["nw11", "nw12", "nw13", "nw14", "nw15"]
    NW2 = ["NW24", "NW25"]
    nw2 = ["nw24", "nw25"]
    NW3 = ["NW34", "NW35"]
    nw3 = ["nw34", "nw35"]
    NW4 = ["NW44", "NW45"]
    nw4 = ["nw44", "nw45"]
    NW5 = ["NW51", "NW52", "NW53", "NW54", "NW5"]
    nw5 = ["nw51", "nw52", "nw53", "nw54", "nw55"]
    E0 = ["N1", "N2", "N3", "N4", "N5"]
    e0 = ["n1", "n2", "n3", "n4", "n5"]
    NE1 = ["NE11", "NE12", "NE13", "NE14", "NE15"]
    ne1 = ["ne11", "ne12", "ne13", "ne14", "ne15"]
    NE2 = ["NE21", "NE22", "NE23", "NE24", "NE25"]
    ne2 = ["ne21", "ne22", "ne23", "ne24", "ne25"]
    NE3 = ["NE31", "NE32", "NE33", "NE34", "NE35"]
    ne3 = ["ne31", "ne32", "ne33", "ne34", "ne35"]
    NE4 = ["NE41", "NE42", "NE43", "NE4", "NE45"]
    ne4 = ["ne41", "ne42", "ne43", "ne44", "ne45"]
    NE5 = ["NE51", "NE52", "NE53", "NE54", "NE5"]
    ne5 = ["ne51", "ne52", "ne53", "ne54", "ne55"]
    S0 = ["S1", "S2", "S3", "S4", "S5"]
    s0 = ["s1", "s2", "s3", "s4", "s5"]
    SW1 = ["SW11", "SW12", "SW13", "SW14", "SW15"]
    sw1 = ["sw11", "sw12", "sw13", "sw14", "sw15"]
    SW2 = ["SW21", "SW22", "SW23", "SW24", "SW25"]
    sw2 = ["sw21", "sw22", "sw23", "sw24", "sw25"]
    SW3 = ["SW31", "SW32", "SW33", "SW34", "SW35"]
    sw3 = ["sw31", "sw32", "sw33", "sw34", "sw35"]
    SW4 = ["SW41", "SW42", "SW43", "SW44", "SW45"]
    sw4 = ["sw41", "sw42", "sw43", "sw44", "sw45"]
    SW5 = ["SW51", "SW52", "SW53", "SW54", "SW5"]
    sw5 = ["sw51", "sw52", "sw53", "sw54", "sw55"]
    W0 = ["W1", "W2", "W3", "W4", "W5"]
    w0 = ["w1", "w2", "w3", "w4", "w5"]
    SE1 = ["SE11", "SE12", "SE13", "SE14", "SE15"]
    se1 = ["se11", "se12", "se13", "se14", "se15"]
    SE2 = ["SE21", "SE22", "SE23", "SE24", "SE25"]
    se2 = ["se21", "se22", "se23", "se24", "se25"]
    SE3 = ["SE31", "SE35"]
    se3 = ["se31", "se35"]
    SE4 = ["SE41", "SE45"]
    se4 = ["se41", "se45"]
    SE5 = ["SE51", "SE55"]
    se5 = ["se51", "se55"]

    open_seas_map_N = [N0, NE1, NE2, NE3, NE4, NE5, NW1, NW2, NW3, NW4, NW5]
    open_seas_map_n = [n0, ne1, ne2, ne3, ne4, ne5, nw1, nw2, nw3, nw4, nw5]
    open_seas_map_S = [S0, SE1, SE2, SE3, SE4, SE5, SW1, SW2, SW3, SW4, SW5]
    open_seas_map_s = [s0, se1, se2, se3, se4, se5, sw1, sw2, sw3, sw4, sw5]

    open_seas_map = [open_seas_map_s, open_seas_map_S, open_seas_map_n, open_seas_map_N]

    close_narwal = ["NW21", "nw21", "NW 22", "nw22", "NW23", "nw23", "NW33", "nw33", "NW43", "nw43", "NW42", "nw42",
                    "NW41", "nw41", "NW31", "nw31"]
    narwal_location = ["NW32", "nw32"]

    close_octopus = ["SE32", "se32", "SE33", "se33", "SE34", "se34", "SE44", "se44", "SE54", "se54", "SE53", "se53",
                    "SE52", "se52", "SE42", "se42"]
    octopus_location = ["SE43", "se43"]

    if message in narwal_location:
        print("You've found Narwal!")
        print("Now let's find the Octopus!")

    elif message in close_narwal:
        print("You're getting close! I can see the Narwal on the horizon!")

    elif message in close_octopus:
        print(" You're getting close! I can see the Octopus on the horizon!")

    elif message in octopus_location:
        print("You've found the Octopus!")

    elif message not in open_seas_map:
        print("Nothing but blue seas out here matey! Let's try again!")

    elif message == 'quit':
        print("Thanks for playing!")
        exit()




