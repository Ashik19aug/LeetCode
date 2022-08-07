value = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
roman = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

class Solution:
    def intToRoman(self, number: int) -> str:
        output = ''
        for i in range(13):
            while number >= value[i]:
                output = output + roman[i]
                number = number - value[i]
        return output
