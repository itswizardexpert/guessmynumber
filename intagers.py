import random


# Write a program that creates a random integer between 1 - 100
# Write code that attempts to guess the random number. It cannot know the random number it’s guessing, unless the number matches. 
# The code you write that guesses the number may check if the number guessed is too high or too low. 
# For each number the computer “guess” add the number to a list(or array or set... depending on what fits you language and program the best - your choice)
# Have the program guess another number, that is not in the list, until it guesses the correct number.
# Once the program guesses the correct number, output/display the correct number, the # of guesses, and the list(set, array…) of the incorrect numbers it attempted.

answers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22","23", "24","25", "26", "27", "28", "29", "30", "31", "32","33", "34","35", "36", "37", "38", "39", "40", "41", "42", "43", "44","45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61", "62", "63", "64", "65", "66", "67", "68", "69", "70", "71", "72","73", "74","75", "76", "77", "78", "79", "80", "81", "82","83", "84"," 85", "86", "87", "88", "89", "90", "91", "92", "93", "94","95", "96", "97", "98", "99", "100",]
choice = input("")

Responses = ("Yes", "YEs", "YeS", "YES", "yES", "yEs","yes", "Ya", "YA", "ya", "Nope", "NOPE", "N0pe", "NOPe", "NoPe", "NOpE", "NoPE", "nOPE", "noPE","nOpe", "noPe", "nopE", "nope", "No", "no", "NO", "N0", "YEAH", "yEAh", "yeaH", "YEah", "YeAH", "YEAh", "YeaH", "Yeah", "yEAH", "yeah", "yEah", "yeAh")


'''
Main code
'''

def intagers():
    hope = print(random.choice(answers))
    if (19):
        print("Is "+hope+" the right number?")
        input("")
    elif(18):
        print(random.choice(answers))
        print(" Am I closer?")
        input("")
    else:
        print("it was fun trying to guess your number")
intagers()