def string_reverser(our_string):

    """
    Reverse the input string

    Args:
       our_string(string): String to be reversed
    Returns:
       string: The reversed string
    """
    
    # TODO: Write your solution here
    index = len(our_string)
    reversed = ""
    while index > 0:
        index -= 1
        reversed += our_string[index]
    return reversed

def anagram_checker(str1, str2):

    """
    Check if the input strings are anagrams of each other

    Args:
       str1(string),str2(string): Strings to be checked
    Returns:
       bool: Indicates whether strings are anagrams
    """
    # Clean strings and convert to lower case
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Compare the length of both strings
    if len(str1) == len(str2):
        # Sort each string and compare
        if sorted(str1) == sorted(str2):
            return True

    return False

def word_flipper(our_string):

    """
    Flip the individual words in a sentence

    Args:
       our_string(string): String with words to flip
    Returns:
       string: String with words flipped
    """
    
    # TODO: Write your solution here
    reversed_sentence = []
    words = our_string.split(" ")
    # print(words)
    for idx in range(len(words)):
        # print(words[idx][::-1])
        words[idx] = words[idx][::-1]
    return " ".join(words)

def hamming_distance(str1, str2):

    """
    Calculate the hamming distance of the two strings

    Args:
       str1(string),str2(string): Strings to be used for finding the hamming distance
    Returns:
       int: Hamming Distance
    """
    if len(str1) != len(str2):
        return None

    h_dist = 0
    for char in range(len(str1)):
        if str1[char] != str2[char]:
            h_dist += 1
    return h_dist


# print ("Pass" if not (anagram_checker('water','waiter')) else "Fail")
# print ("Pass" if anagram_checker('Dormitory','Dirty room') else "Fail")
# print ("Pass" if anagram_checker('Slot machines', 'Cash lost in me') else "Fail")
# print ("Pass" if not (anagram_checker('A gentleman','Elegant men')) else "Fail")
# print ("Pass" if anagram_checker('Time and tide wait for no man','Notified madman into water') else "Fail")
# print ("Pass" if ('retaw' == string_reverser('water')) else "Fail")
# print ("Pass" if ('!noitalupinam gnirts gnicitcarP' == string_reverser('Practicing string manipulation!')) else "Fail")
# print ("Pass" if ('3432 :si edoc esuoh ehT' == string_reverser('The house code is: 2343')) else "Fail")
# print ("Pass" if ('retaw' == word_flipper('water')) else "Fail")
# print ("Pass" if ('sihT si na elpmaxe' == word_flipper('This is an example')) else "Fail")
# print ("Pass" if ('sihT si eno llams pets rof ...' == word_flipper('This is one small step for ...')) else "Fail")
print ("Pass" if (10 == hamming_distance('ACTTGACCGGG','GATCCGGTACA')) else "Fail")
print ("Pass" if  (1 == hamming_distance('shove','stove')) else "Fail")
print ("Pass" if  (None == hamming_distance('Slot machines', 'Cash lost in me')) else "Fail")
print ("Pass" if  (9 == hamming_distance('A gentleman','Elegant men')) else "Fail")
print ("Pass" if  (2 == hamming_distance('0101010100011101','0101010100010001')) else "Fail")