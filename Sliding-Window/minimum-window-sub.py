# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. 
# If there is no such substring, return the empty string "".
# The testcases will be generated such that the answer is unique.
from collections import Counter


class Solution(object):
    def minWindow(self, s, t):
        if not t or not s:
            return ""
        
        need = Counter(t)
        have = 0
        need_count = len(need)

        res = [-1, -1]
        res_len = float("inf")

        left = 0

        for right in range(len(s)):
            char = s[right]
            if char in need:
                need[char] -= 1
                if need[char] == 0:
                    have += 1
            
            while have == need_count:
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1
                
                left_char = s[left]
                if left_char in need:
                    need[left_char] += 1
                    if need[left_char] > 0:
                        have -= 1
                left += 1

        
        l, r = res
        return s[l:r+1] if res_len != float("inf") else ""
                




