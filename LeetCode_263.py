"""
LeetCode 263 -- Easy

Write a program to check whether a given number is an ugly number.
Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
"""

class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """"
        if num <= 0:
            return False
        
        ugly_factors = [2,3,5]
        
        if num in ugly_factors + [1]:
            return True

        for factor in ugly_factors:
            if not num%factor:
                return self.isUgly(num/factor)
        
        return False
