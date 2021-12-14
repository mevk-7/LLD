""""
Trie which holds following thing - > LetterMap, count , top common words with suffix
"""


class TrieNode:

    __slots__ = ["_charMap", "_count", "_top_words", "_num_top_common_word", "word"]

    def __init__(self, num_top_common_word):
        self.word = ""
        self._charMap = {}
        self._count = 0
        self._top_words = []
        self._num_top_common_word = num_top_common_word

    def add_word(self, word, count, idx=0):
        if idx == len(word):
            return self.increase_count(count, word)
        if word[idx] not in self._charMap:
            self._charMap[word[idx]] = TrieNode(self._num_top_common_word)
        arr = self._charMap[word[idx]].add_word(word, count, idx+1)
        self.merge_common_words(arr)
        return self._top_words

    def increase_count(self, count, word):
        self.count += count
        self.word = word
        for w in self._top_words:
            if w[0] == word:
                w[1] += count
                return self._top_words
        self._top_words.append([word, self.count])
        self._top_words = sorted(self._top_words, key=lambda x: -x[1])
        return self._top_words

    def get_top_suggestion(self, word, idx=0):
        if len(word) == idx:
            return self._top_words
        if word[idx] not in self._charMap:
            return []
        return self._charMap[word[idx]].get_top_suggestion(word, idx+1)

    @staticmethod
    def _is_present( word, array):
        for w in array:
            if w[0] == word:
                return True
        return False

    def append_to_end(self, words, array, idx,  second_idx):
        while idx < self._num_top_common_word and second_idx < len(array):
            if self._is_present(array[second_idx][0], words):
                second_idx += 1
                continue
            words.append(array[second_idx])
            second_idx += 1
            idx += 1
        return idx

    def merge_common_words(self, child_common_word):
        first_idx, second_idx, idx = 0, 0, 0
        words = []
        while idx < self._num_top_common_word and first_idx < len(self._top_words) and \
                second_idx < len(child_common_word):
            if self._is_present(child_common_word[second_idx][0], words):
                second_idx += 1
                continue
            elif self._is_present(self._top_words[first_idx][0], words):
                first_idx += 1
                continue
            elif self._top_words[first_idx][1] >= child_common_word[second_idx][1]:
                words.append(self._top_words[first_idx])
                first_idx += 1
            else:
                words.append(child_common_word[second_idx])
                second_idx += 1
            idx += 1
        idx = self.append_to_end(words, self._top_words, idx, first_idx)
        idx = self.append_to_end(words, child_common_word, idx, second_idx)
        self._top_words = words

    @property
    def common_words(self):
        return [self._top_words[i][0] for i in range(len(self._top_words))]

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, num):
        if num < 0:
            print("Cannot add -ve no")
            return
        self._count += num

    def add_char(self, char):
        if char not in self._charMap:
            self._charMap[char] = TrieNode(self._num_top_common_word)

    def is_char_present(self, char):
        return char in self._charMap

    def next_node(self, char):
        if char in self._charMap:
            return self._charMap[char]


class TypeAhead:

    __slots__ = ["root", "_num_top_common_word"]

    def __init__(self, num_top_common_word):
        self._num_top_common_word = num_top_common_word
        self.root = TrieNode(self._num_top_common_word)

    def add_word(self, word, count=1):
        self.root.add_word(word, count, 0)

    def get_top_suggestion(self, word):
        return self.root.get_top_suggestion(word, 0)






