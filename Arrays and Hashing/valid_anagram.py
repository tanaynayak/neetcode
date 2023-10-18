class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        for i in set(s):
            if s.count(i) != t.count(i):
                return False
        return True
    
        # if len(s) != len(t):   # Early exit if lengths are different
        #     return False

        # hashmap = {}
        # for letter in s:
        #     if letter in hashmap:
        #         hashmap[letter] += 1
        #     else:
        #         hashmap[letter] = 1
        
        # for letter in t:
        #     if letter in hashmap:
        #         hashmap[letter] -= 1
        #         if hashmap[letter] == 0:   # Removing the key for efficiency
        #             del hashmap[letter]
        #     else:
        #         return False
        
        # return len(hashmap) == 0   # hashmap should be empty if s and t are anagrams