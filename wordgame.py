from lib2to3.pytree import LeafPattern


def all_alpha(word):
    word = word.lower()
    list_word = split(word)
    listlen = len(list_word)
    pos = 0
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    while listlen > 0:
        if list_word[pos] in alphabet:
            listlen = listlen - 1
            pos = pos + 1
            continue
        else:
            return False
    return True
#must be string or fails

def indexall(pattern,word):
    return [index for index, value in enumerate(word) if value == pattern]
    #retrieved from stackoverflow.com

def split(word):
    return [char for char in word]
        #obtained from poopcode.com

def replace_clouded_letter(letter,answer,cloud):
    index_list = indexall(letter,answer)
    index_list_length = len(index_list)
    pos = 0
    while index_list_length > 0:
        cloud = split(cloud)
        cloud[index_list[pos]] = letter
        cloud = ''.join(cloud)
        index_list_length = index_list_length - 1
    return cloud


hidden_word = "kitty"
guesses = 7
def make_dashed_word(word):
    wordlen = len(word)
    emlist = []
    while wordlen > 0:
        emlist.append("-")
        wordlen = wordlen - 1
    dashed_word = ''.join(emlist)
    return dashed_word

clouded_word = make_dashed_word(hidden_word)

def word_game(answer):
    word_clouded = make_dashed_word(answer)
    answer = answer.lower()
    guesses_remaining = 7
    stored_guesses = []
    while guesses_remaining > 0:
        input_prompt = 'Guess either a letter, or the final word. Your word so far is ' + word_clouded + '. You have ' + str(guesses_remaining) + ' guesses remaining. Good luck! Guess: '
        player_input = str(input(input_prompt))
        player_input = player_input.lower()
        if not all_alpha(player_input):
            print('guesses must only use letters')
        elif len(player_input) == 1:
            word_clouded2 = replace_clouded_letter(player_input,answer,word_clouded)
            if word_clouded2 != word_clouded:
                word_clouded = word_clouded2
                #continue
            elif word_clouded2 == word_clouded:
                guesses_remaining = guesses_remaining - 1
        elif len(player_input) > 1:
            if player_input == answer:
                print("You win, Congradulations! The word was \"" + answer + "\"!")
                break
            elif player_input != answer:
               guesses_remaining = guesses_remaining - 1 
    print('Game Over')

#word_clouded = '----'
#guesses_remaining = 7
#input_prompt = 'Your word so far is ' + word_clouded + '. You have ' + str(guesses_remaining) + ' guesses remaining. Good luck! Guess: '
#player_input = input(input_prompt)
#print(player_input)

#make a function that returns a boolean for if an answer contains non-letter


word_game('hero')

#print(replace_clouded_letter('lulz','house','-----'))

#leaf = 'maple'
#leaf = split(leaf)
#leaf[0] = 'p'
#leaf = ''.join(leaf)
#print(leaf)

