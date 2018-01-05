class Dictionary:
    def __init__(self,words):
        self.words=words

    def __levenshtein(self, s1, s2):
        ''' https://en.wikibooks.org/wiki/Algorithm_Implementation/Strings/Levenshtein_distance#Python '''
        if len(s1) < len(s2):
            return self.__levenshtein(s2, s1)

        # len(s1) >= len(s2)
        if len(s2) == 0:
            return len(s1)

        previous_row = range(len(s2) + 1)
        for i, c1 in enumerate(s1):
            current_row = [i + 1]
            for j, c2 in enumerate(s2):
                insertions = previous_row[j + 1] + 1 # j+1 instead of j since previous_row and current_row are one character longer
                deletions = current_row[j] + 1       # than s2
                substitutions = previous_row[j] + (c1 != c2)
                current_row.append(min(insertions, deletions, substitutions))
            previous_row = current_row

        return previous_row[-1]

    def find_most_similar(self,term):
        word = None
        diff = len(term)
        for w in self.words:
            tmp_diff = self.__levenshtein(term, w)
            # print(term, w, tmp_diff, tmp_diff < diff)
            if tmp_diff < diff:
                diff = tmp_diff
                word = w
        return word

words=['cherry', 'peach', 'pineapple', 'melon', 'strawberry', 'raspberry', 'apple', 'coconut', 'banana']
test_dict=Dictionary(words)
print(test_dict.find_most_similar('strawbery'),'strawberry')
print(test_dict.find_most_similar('berry'),'cherry')
print(test_dict.find_most_similar('aple'),'apple')
