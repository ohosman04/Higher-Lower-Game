import random

def game(min,max):
    i = 1
    while i > 0:
        first_number  = random.randint(min,max)
        prompt = input(f"Is {first_number} the number you're thinking of? (Y/N): ").lower()
        if prompt in ['y','n']:
            if prompt == 'n':
                q2 = input("Is the number smaller or bigger? (S/B): ").lower()
                if q2 in ['s','b']:
                    if q2 == 's':
                        game(min,first_number-1)  
                    else:
                        game(first_number+1,max)
                else:
                    print("Wrong Choice. You had two options. bye bye!")
                    i = 0
            if prompt == 'y':
                i = 0
        return True

if __name__ == "__main__":
    print("Welcome to the number guesser game pt2. This time I will try to guess the number in your head by asking but a few questions!")
    min_range = int(input("Please indicate your range: (min number): "))
    max_range = int(input("Please indicate your range: (max number): "))
    result = game(min_range,max_range)
    if result ==  True:
        print("WOOOOO I WIN!!!!!!!!!!!!")