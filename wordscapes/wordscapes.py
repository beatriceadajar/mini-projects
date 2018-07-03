import itertools
import re
from nltk.corpus import wordnet


def play():
	# run this line of code only the first time the code is run on the system
	# nltk.download('wordnet')

    print('----------------------------------------------')
    print('1. Generate all words given a length')
    print('2. Generate a word given a pattern of letters')
    print('----------------------------------------------')

    choice = input('\nChoose an option from the menu above (1/2): ')

    if choice == '1':
        alphabet = input('Enter the alphabet (abcde): ')
        length = int(input('Enter the length of the word (4): '))
        permutations = list(itertools.permutations(list(alphabet), length))
        answers = set(''.join(word).lower() for word in permutations
                      if wordnet.synsets(''.join(word).lower()))

        print('\nAnswers:')
        print(*answers, sep='\n')

    elif choice == '2':
        alphabet = input('Enter the alphabet (abcde): ')
        pattern = input(
            'Enter the pattern. Use \'.\' in place of blanks (.e.d.): ')
        length = len(pattern)
        permutations = list(itertools.permutations(list(alphabet), length))
        pattern = re.compile(pattern)

        answers = set(''.join(word).lower() for word in permutations
                      if re.match(pattern, ''.join(word).lower()) and
                      wordnet.synsets(''.join(word).lower()))

        print('\nAnswers:')
        print(*answers, sep='\n')

    else:
        print('Invalid choice. Try again.\n')
        play()


if __name__ == '__main__':
    play()
