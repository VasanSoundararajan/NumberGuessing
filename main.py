import random

def main():
    # Generate a random number between 1 and 100
    ran = random.randint(1, 100)
    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("You have to guess the number in as few attempts as possible based on the level.")
    level = input("Choose a level (easy(10), medium(5), hard(3)): ")
    if level == "1":
        print("you have choose easy level")
        max_attempts = 10
    elif level == "2":
        print("you have choose medium level")
        max_attempts = 5
    elif level == "3":
        print("you have choose hard level")
        max_attempts = 3
    for i in range(max_attempts):
        guess = int(input("Enter your Guess "))
        if guess < ran:
            print("The number is less than ", guess)
        elif guess > ran:
            print("The number is greater than ", guess)
        else:
            print("Congratulations, you guessed the number in", i+1, "attempts!")
            break

if __name__ == '__main__':
    main()