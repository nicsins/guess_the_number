import random

correct = 'you guessed correctly!'
too_low = 'too low'
too_high = 'too high'
guess_counter = 0

def configure_range():
    '''Set the high and low values for the random number'''
    return 1, 10

def count_guesses():
    global guess_counter 
    guess_counter += 1
    counter = str(guess_counter)
    print('Guess ' + counter)
    #return guess_counter
    

def generate_secret(low, high):
    '''Generate a secret number for the user to guess'''
    return random.randint(low, high)


def get_guess():
    '''get user's guess'''
    return int(input('Guess the secret number? '))


def check_guess(guess, secret):
    '''compare guess and secret, return string describing result of comparison'''
    if guess == secret:
        return correct
    if guess < secret:
        return too_low
    if guess > secret:
        return too_high


def main():

    (low, high) = configure_range()
    secret = generate_secret(low, high)

    while True:
        count_guesses()
        guess = get_guess()
        result = check_guess(guess, secret)
        print(result)
        

        if result == correct:
            break


if __name__ == '__main__':
    main()
