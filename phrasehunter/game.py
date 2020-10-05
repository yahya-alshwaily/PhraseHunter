from phrasehunter.phrase import Phrase
import random

class Game:

    def __init__(self):
        self.missed = 0
        self.phrases = [
            'Life is like a box of chocolates',
            'Easy come easy go',
            'Vici Veni Vidi',
            'Carpe Diem',
            'what it really means to live life golden'
        ]
        self.active_phrase = self.get_random_phrase()
        self.guesses = [' ']
        
    def welcome(self):
        print("""
        ============================
          Welcome to Phrase Hunter
        ============================
        """)

    def start(self):

        self.welcome()
        print(f'Number missed: {self.missed}')

        while self.missed <= 5 and Phrase(self.active_phrase).check_complete(self.guesses):
            Phrase(self.active_phrase).display(self.guesses)
            user_guess = self.get_guess()

            if Phrase(self.active_phrase).check_guess(user_guess):
                print('YAY')
                self.guesses.append(user_guess)

            if not Phrase(self.active_phrase).check_guess(user_guess):
                print('Bummer!')
                self.missed +=1
            
            print(f'Number missed: {self.missed}')
        self.game_over()
        self.reset()

    def get_random_phrase(self):

        random_phrase = random.choice(self.phrases)
        random_phrase = Phrase(random_phrase)
        return random_phrase.phrase

    def get_guess(self):
        while True:
            user_guess = input("\nEnter a letter: ")
            if user_guess not in "abcdefghijklmnopqrstuvwxyz" and len(user_guess)>1:
                print('Please enter one letter of the alphabet')
                continue
            else:
                break

        return user_guess

    def game_over(self):

        if self.missed == 5:
            print("Game Over! You Lost!")
        else:
            print("Congratulations you won!")

    def reset(self):
        del self.guesses[1:len(self.guesses)]
        self.missed = 0