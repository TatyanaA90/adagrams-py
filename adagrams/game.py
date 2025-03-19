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
        for i in letter * count:
            letters_list.append(i)
    return letters_list

def draw_letters():
    draw_letters_list = convert_letter_pool_to_list(LETTER_POOL)
    result_letters = []
    #for i in range(10):
    counter = 0
    while counter < 10:
        index = randint(0, len(draw_letters_list) - 1)  
        letter = draw_letters_list[index]  
        result_letters.append(letter)
        draw_letters_list.pop(index)
        counter += 1

    return result_letters

def uses_available_letters(word, letter_bank):
#word - user input
#letter_bank - random set of letter given to user from letter_pool,array of 10 
    word = word.upper()
    letter_bank_copy = list(letter_bank)
    for char_set in word:
        if char_set not in letter_bank_copy:
            return False
        letter_bank_copy.remove(char_set)
        #for index, found_letter in letter_bank:
        #for index in range(0,len(letter_bank_copy) -1): #don't use range
        #    if letter_bank_copy[index] == char_set:
        #        letter_bank_copy.pop(index) #remove

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
    
    # if len(word) in [7,8,9,10]:
    #    total_points += 8

    if len(word) >= 7 and len(word) <= 10:
        total_points += 8
    
#iterate each letter from word 
    for char in word:
        letter_score = score_chart[char]
        total_points += letter_score

    return total_points



def get_highest_word_score(word_list):
    total_word_score = []
    max_score = 0
    #hight_word_score = []
    tie_with_max_score = []
    # get each word from word_list  
    for word in word_list:
        # get score for each word from sore_word function
        word_score = score_word(word)
        total_word_score.append({word: word_score})
    #output of total_word_score = [ {"DOG": 5}, {"Apple": 7}]

    # find max score and winner word (word first than its score)
    for score in total_word_score:
        # score =  {"DOG": 5}
        for score_key, score_value in score.items():
            #word_score_value.append(hight_word_score)
            # the word_score_value = 7
            word_score_value =  score_value
            # the word_score_key = DOG
            word_score_key = score_key

        if max_score < word_score_value:
            max_score = word_score_value

            #hight_word_score = [word_score_key, word_score_value]

    # create and fuind list wirh tie max score
    #output of total_word_score = [ {"DOG": 5}, {"ApplW": 7}, {"Apple": 7}]
    for word_score_dict in total_word_score:
        # word = {"DOG": 5}
        max_word_score_value = ""
        max_word_score_key = ""

        # the the total_word_score was list of lists 
        # max_word_score_key =  word_score_dict[0]
        # max_word_score_value = word_score_dict[1]

        #unpack dictionary into key, value
        for key, value in word_score_dict.items():
            max_word_score_value =  value
            max_word_score_key = key

        if max_score == max_word_score_value:
            tie_with_max_score.append([max_word_score_key, max_word_score_value])
    # tie_with_max_score = [["ApplW": 7],["Apple": 7]]
        
    # find the shortest tie word
    for word in tie_with_max_score:   # word = ["ApplW": 7]
        #unless one word has 10 letters. If the top score is tied between multiple words and one is 10 letters long, choose the one with 10 letters over the one with fewer tiles
        if len(word[0]) >= 10:
            return tuple(word)

#If the there are multiple words that are the same score and the same length, pick the first one in the supplied list
    max_word_len = len(tie_with_max_score[0][0])
    is_all_word_has_same_leght = True
    for word in tie_with_max_score: 
        if max_word_len != len(word[0]):
            is_all_word_has_same_leght = False 
    if is_all_word_has_same_leght:
        return tuple(tie_with_max_score[0])
        
# prefer the word with the fewest letters...
    min_word_len = len(tie_with_max_score[0][0])
    min_word_score = []
    for word in tie_with_max_score: 
        # 4 < 3
        if len(word[0]) <= min_word_len:
            min_word_len = len(word[0])
            min_word_score = list(word)
    print(min_word_score)
    return tuple(min_word_score)



    #return hight_word_score

    





    # get_highest_word_tie_prefers_shorter_word