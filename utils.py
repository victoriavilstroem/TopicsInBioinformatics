from functools import cmp_to_key

class SuffixArray:
    def __init__(self, text):
        self.text = text

    def suffix_array(self):
        s = self.text
        n = len(s)

        def cmp_suffix(i, j):
            while i < n and j < n:
                if s[i] < s[j]:
                    return -1
                elif s[i] > s[j]:
                    return 1
                i += 1
                j += 1
            if i == n and j == n:
                return 0
            elif i == n:
                return -1
            elif j == n:
                return 1
        return sorted(range(n), key = cmp_to_key(cmp_suffix))