class Solution(object):
    def mergeAlternately(self, word1, word2):
        new_word = []
        index1 = 0
        index2 = 0

        while index1 < len(word1) and index2 < len(word2):
            new_word.append(word1[index1])
            new_word.append(word2[index2])
            index1 += 1
            index2 += 1
        new_word.append(word1[index1:])
        new_word.append(word2[index2:])
        return "".join(new_word)
