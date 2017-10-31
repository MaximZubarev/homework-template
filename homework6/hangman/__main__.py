import json
import random
import string


class Game(object):
    def __init__(self, random_word):
        self.random_word = random_word
        self.unsolved_word = ['_'] * len(self.random_word)
        self.hangman = ['|', 'O', '/', '|', '\\', '/', ' ', '\\']

    def draw_hangman(self, n):
        """
        Draw the hangman
        :param n: amount of mistakes
        :return: none
        """
        if n <= 3:
            print('_' * 3)
            for m in range(0, n):
                print(''.join(self.hangman[m].center(3, ' ')))
        elif 3 < n < 6:
            self.draw_hangman(2)
            print(''.join(self.hangman[2:n]))
        else:
            self.draw_hangman(5)
            print(''.join(self.hangman[5:n + 1]))

    def check_letter(self, letter, random_word):
        """
        This method checks if there is a letter in the word
        :param letter: letter which the user printed
        :param random_word: right word
        :return: unsolved word with the letters
        """
        if letter in random_word:
            for k in range(0, len(random_word)):
                if self.unsolved_word[k] == '_':
                    self.unsolved_word[k] = letter if\
                        random_word[k] == letter else '_'
            return ''.join(self.unsolved_word)

    def is_game_finished(self, word):
        """
        This method checks if the game is finished
        :param word: unsolved word
        :return: True if the game is finished, False otherwise
        """
        if '_' not in word:
            return True

    def ask_letter(self):
        """
        ask user to print a letter
        :return: letter which user printed
        """
        letter = ' '
        while letter not in string.ascii_lowercase:
            letter = input('Write a letter:\n')
            letter.lower()

        return letter

    def send_result(self, attempts, winner):
        """
        Send result of game
        :param attempts:
        :param winner:
        :return: list with attempts, winner, amount of right letters
        """
        result = [attempts, len([i for i in self.unsolved_word if
                                 i != '_']), winner]
        return result

    def perform(self):
        """
        This method call other methods
        :return: result of the game
        """
        i = 1
        attempts = 0

        while i < 8:
            letter = self.ask_letter()
            result = self.check_letter(letter, self.random_word)
            attempts += 1
            if result:
                print(result)
                if self.is_game_finished(result):
                    print('\nYou`re win!')
                    winner = 1
                    return self.send_result(attempts, winner)
                    break
            else:
                self.draw_hangman(i)
                i += 1
            if i == 8:
                print('\nYou`re lose')
                winner = 2
                return self.send_result(attempts, winner)


def print_result(attempts, letters):
    """
    Print the results of the part
    :param attempts: Attempts
    :param letters: Right letters
    :return: results of the part
    """
    print('Attempts in this party: {}'.format(attempts))
    print('Right letters in this party: {}'.format(letters))


def print_final_result(amount_attempts, right_letters):
    """
    Print the final results of the game
    :param amount_attempts: Final attempts
    :param right_letters: Final right letters
    :return: final results of the game
    """
    print('Amount of your attempts in the game: {}'.format(amount_attempts))
    print('Amount of your right letters in game: {}'.format(right_letters))


def player_game():
    player1 = 0
    player2 = 0
    turn = 2
    amount_attempts = 0
    right_letters = 0

    while player1 < 2 and player2 < 2:
        word = ''
        while all(map(lambda c: c not in string.ascii_letters, word)):
            try:
                word = str(input('Player {} - write a word:\n'.format(turn)))
                word.lower()
                word.strip()
            except ValueError:
                print('Write a word!')

        result = Game(word).perform()
        amount_attempts += result[0]
        right_letters += result[1]
        if result[2] == 1 and turn == 2:
            player1 += 1
            turn = 1
        elif result[2] == 2 and turn == 2:
            player2 += 1
            turn = 1
        elif result[2] == 1 and turn == 1:
            player2 += 1
            turn = 2
        else:
            player1 += 1
            turn = 2

        print_result(result[0], result[1])
        print('Player 1 {} - {} Player 2'.format(player1, player2))
        print_final_result(amount_attempts, right_letters)


def pc_game():
    with open('words.json', 'r', encoding='utf-8') as fh:
        words = json.load(fh)

    player_win = 0
    pc_win = 0
    amount_attempts = 0
    right_letters = 0

    while player_win < 2 and pc_win < 2:
        random_word = tuple(random.choice(words['words']))
        result = Game(random_word).perform()
        amount_attempts += result[0]
        right_letters += result[1]
        if result[2] == 1:
            player_win += 1
        else:
            pc_win += 1
        print_result(result[0], result[1])

    if player_win == 2:
        print('\nYou`re win the game! Congratulations!\n')
    else:
        print('\nYou`re lose the game\n')

    print_final_result(amount_attempts, right_letters)


def main():
    """
    The main method. It stars when the program is called.
    It also calls other methods.
    :return: None
    """
    choice = None
    while choice not in [1, 2]:
        try:
            choice = int(input('Play with?\n1. '
                               'Player\n2. Computer\nWrite a number:\n'))
            player_game() if choice == 1 else pc_game()
        except ValueError:
            print('Write a number!\n')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print('Shutting down, bye!')
