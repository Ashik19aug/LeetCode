romanToInt = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


class Solution:
    def romanToInt(self, romanNumber: str) -> int:
        integerNumber: int = 0
        for i in range(len(romanNumber) - 1, -1, -1):
            num = romanToInt[romanNumber[i]]
            if 4 * num < integerNumber:
                integerNumber -= num
            else:
                integerNumber += num
        return integerNumber
