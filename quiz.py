from random import shuffle

def game():
    score = 0
    shuffle(questions)
    asking = questions[0:6]
    for question in asking:
        answer = input(question[0] + '\n')
        if (answer.lower() == question[1].lower()):
            score += 1
            print("Congrats, that's right")
        else:
            print(f"That's incorrect... The answer is \"{question[1]}\"")
        input("Press any key to continue")
    did_good = ''
    if score == 6:
        did_good = "Perfect Score!!!"
    elif score >= 3:
        did_good = "Well Done."
    else:
        did_good = "Better Luck Next Time..."
    
    print(f"Your Final Score is {score} out of {len(asking)}. {did_good}")
    try_again()

def try_again():
    go_again = input("Do you wish to try again? (y/n)\n")
    if go_again == "y":
        game()
    elif go_again == "n":
        print("Thank you for playing. See you later!")
    else:
        print("Sorry, I didn't catch that.")
        try_again()


def prompt():
    proceed = input("Do you wish to continue to the quiz? (y/n)\n")
    if proceed == "y":
        print("Let's start the quiz!")
        game()
    elif proceed == "n":
        print("Alright, see you later...")
    else:
        print("Hi, I'm sorry, I didn't quite catch that. Can you repeat that again?")
        prompt()

questions = [
    ("How many bones are there in a human body?", "206"),
    ("What is mitochondria?", "The powerhouse of the cell"),
    ("How many days does it take for the Earth to orbit the Sun?", "365"),
    ("What year was the World Wide Web invented?", "1990"),
    ("Which mountain range is the Mount Everest located in?", "The Himalayas"),
    ("Which country has the largest population?", "China"),
    ("Who is known as the fastest man in the world?", "Usain Bolt"),
    ("Which chemical element is represented by the symbol \"C\" in the periodic table of elements?", "Carbon"),
    ("What is the smallest prime number greater than 10?", "11"),
    ("In Greek Mythology, who is the goddess of wisdom and warfare?", "Athena"),
    ("Where is the Taj Mahal located?", "India"),
    ("What is your body's largest organ?", "Skin")
]

print(f"Welcome to my quiz game.\nThis is a quick quiz game I made in python to get familiar with it.")
prompt()