class Phrase:
    
    def __init__(self, phrase):
        self.phrase = phrase.lower()

    def display(self, guesses):
        self.guesses = guesses
        for letters in self.phrase:
            if letters in guesses:
                print(letters, end=' ') #to keep it from printing the letters on new lines
            else:
                print('_', end=' ')

    def check_guess(self, guess):
        self.guess = guess
        if guess in self.phrase:
            return True
        else:
            return False

    def check_complete(self, guesses):
        self.guesses = guesses
        for letter in self.phrase:
            if letter not in guesses:
                return True
        else:
            return False
    