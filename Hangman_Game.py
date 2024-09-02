
import random

words = ("arfa", "faheem", "python", "orange", "codealpha")

definitions = {"arfa": "Name of owner", "faheem": "Father's name", "python": "Programming language",
               "orange": "Fruit", "codealpha": "Company"}

hangman = {0: ("    ",
               "    ",
               "    "),
           1: (" o  ",
               "    ",
               "    "),
           2: (" o  ",
               " |  ",
               "    "),
           3: (" o  ",
               "/|  ",
               "    "),
           4: (" o  ",
               "/|\\ ",
               "    "),
           5: (" o  ",
               "/|\\ ",
               "/   "),
           6: (" o  ",
               "/|\\ ",
               "/ \\ ")}

def display_hangman(wrong_guess):
    for i in hangman[wrong_guess]:
        print(i)
def display_line(line):
    print(" ".join(line))

def display_answer(answer):
    print(" ".join(answer))


def main():
    answer = random.choice(words)
    wrong_guess = 0
    g_letters = set()
    line = ["_"] * len(answer)

    print("Welcome to the Hangman Game!")
    running = True

    while running:
        display_hangman(wrong_guess)
        display_line(line)
        enter= input("Guess a letter :)").lower()

        if len(enter)!= 1 or not enter.isalpha():
            print("Invalid input.")
            continue

        if enter in g_letters:
            print(enter + " is already guessed.")
            continue
        g_letters.add(enter)

        if enter in answer:
            for i in range(len(answer)):
                if answer[i] == enter:
                    line[i] = enter
        else:
            wrong_guess += 1


        if "_" not in line:
            display_hangman(wrong_guess)
            display_answer(answer)
            print("Congrats, You WIN!")
            print("The definition of " + answer + " is " + definitions[answer])
            running= False

        elif wrong_guess>= len(hangman) - 1:
            display_hangman(wrong_guess)
            display_answer(answer)
            print("Oops, You LOSE!")
            print("The definition of " + answer + " is " + definitions[answer])
            running = False

if __name__ == "__main__":
    main()

playagain= True
while playagain:

    print("Do you want to try again?")
    char = input("Enter yes/no:")

    if char == "yes":
        main()
    elif char == "no":
        print("Have a nice day! See you again.")
        playagain=False
    else:
        print("Enter valid input.")















