class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        m = len(num1)
        n = len(num2)
        result = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1 , -1):

                digit1 = ord(num1[i]) - ord("0")
                digit2 = ord(num2[j]) - ord("0")

                product = digit1 * digit2

                one_position = i + j + 1
                ten_position = i + j

                total = product + result[one_position]
                
                result[one_position] = total % 10
                result[ten_position] += total // 10

        if result[0] == 0:
            result = result[1:]

        return "".join(str(digit) for digit in result)