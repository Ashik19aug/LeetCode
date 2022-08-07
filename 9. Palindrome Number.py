class Solution:
    def isPalindrome(self, number: int) -> bool:
        if number < 0:
            return False
        checkNmuber = number
        checkPlindrome = 0
        while number > 0:
            checkPlindrome = checkPlindrome * 10 + number % 10
            number //= 10
        return checkNmuber == checkPlindrome
