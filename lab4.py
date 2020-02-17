def main():
    print("Python Guessing Game")
    x=20

    while x==20:
        a=input("I'm thinking of an animal, can you guess which one?")
        p="jaguar"

        if p==a:
            x=1
            print("Congratulations, you've guessed my animal!")

        else:
            print("Sorry, guess again")

main()
