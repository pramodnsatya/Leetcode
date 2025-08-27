class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #By using count function over a set
        if len(s) != len(t):
            return False

        for char in set(t):
            s_count = s.count(char)
            t_count = t.count(char)
            if s_count != t_count:
                return False
        return True