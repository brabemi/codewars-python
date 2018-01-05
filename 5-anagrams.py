def anagram_match(dict_word, word):
    for c in word:
        if c not in dict_word.keys():
            return False
        dict_word[c] -= 1
    for key, value in dict_word.items():
        if value != 0:
            return False
    return True

def anagrams(word, words):
    dict_word = {}
    for c in word:
        if c not in dict_word.keys():
            dict_word[c] = 0
        dict_word[c] += 1
    return [w for w in words if anagram_match(dict_word.copy(), w)]
    #your code here

print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
