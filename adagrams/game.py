from random import randint
LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}

def convert_letter_pool_to_list(letter_pool):
    letters_list =[]
    
    for letter, count in letter_pool.items():
            letters_list.append(list(letter) * count)
    return letters_list

def draw_letters():
    draw_letters_list = convert_letter_pool_to_list(LETTER_POOL)
    result_letters = []
    counter = 0
    while counter < 10:
        index = randint(0, len(draw_letters_list) - 1)  
        letter = draw_letters_list.pop(index)
        result_letters.append(letter)
        counter += 1

    return result_letters

def uses_available_letters(word, letter_bank):
    word = word.upper()
    letter_bank_copy = list(letter_bank)
    for charset in word:
        if charset not in letter_bank_copy:
            return False
        letter_bank_copy.remove(charset)
    return True



def score_word(word):
    score_chart = {
        'A': 1, 
        'B': 3, 
        'C': 3, 
        'D': 2, 
        'E': 1, 
        'F': 4, 
        'G': 2, 
        'H': 4, 
        'I': 1, 
        'J': 8, 
        'K': 5, 
        'L': 1, 
        'M': 3, 
        'N': 1, 
        'O': 1, 
        'P': 3, 
        'Q': 10, 
        'R': 1, 
        'S': 1, 
        'T': 1, 
        'U': 1, 
        'V': 4, 
        'W': 4, 
        'X': 8, 
        'Y': 4, 
        'Z': 10
    }
    word = word.upper()
    total_points = 0

    if len(word) == 0:
        return total_points
    
    # extra 8 points if the length of the word is 7, 8, 9, or 10,
    if len(word) >= 7 and len(word) <= 10:
        total_points += 8

    for charset in word:
        total_points += score_chart[charset]

    return total_points


def get_max_score(calculated_words_score):
    max_score = 0

    for word_score in calculated_words_score:
        # word_score[0] - word
        # word_score[1] - score
        if max_score < word_score[1]:
            max_score = word_score[1]

    return max_score


def get_words_by_score(calculated_words_score, score):
    tie_with_max_score = []

    for word_score in calculated_words_score:
        # word_score[0] - word
        # word_score[1] - score

        if score == word_score[1]:
            tie_with_max_score.append([word_score[0], word_score[1]])

    return tie_with_max_score


def get_winner_same_lenght_score(tie_with_max_score):
    """
    if the there are multiple words that are the same score and the same length,
    pick the first one 
    """
    #tie_with_max_score[0][0] - word
    max_word_len = len(tie_with_max_score[0][0])

    # Check if all words has same length
    for word_score in tie_with_max_score: 
        if max_word_len != len(word_score[0]):
            return []

    return tie_with_max_score[0]


def get_winner_fewest_letters(tie_with_max_score):
    # prefer the word with the fewest letters...
    min_word_len = len(tie_with_max_score[0][0])
    result = []

    for word_score in tie_with_max_score: 
        if len(word_score[0]) <= min_word_len:
            min_word_len = len(word_score[0])
            result = word_score 

    return result


def get_highest_word_score(word_list):
    calculated_words_score = []

    for word in word_list:
        score = score_word(word)
        calculated_words_score.append([word, score])

    max_score = get_max_score(calculated_words_score)
    tie_with_max_score = get_words_by_score(calculated_words_score, max_score)

    # find the shortest tie word, unless one word has 10 letters
    for word_score in tie_with_max_score:
        if len(word_score[0]) >= 10:
            return tuple(word_score)

    same_lenght_score_winner = get_winner_same_lenght_score(tie_with_max_score)    
    if same_lenght_score_winner:
        return tuple(same_lenght_score_winner)
    
    fewest_letters_winner = get_winner_fewest_letters(tie_with_max_score)
    if fewest_letters_winner:
        return tuple(fewest_letters_winner)
