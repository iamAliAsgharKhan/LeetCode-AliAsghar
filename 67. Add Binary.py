class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        result = []
        i, j = len(a) - 1, len(b) - 1
        while i >= 0 or j >= 0:
            x = int(a[i]) if i >= 0 else 0
            y = int(b[j]) if j >= 0 else 0
            s = x + y + carry
            result.append(str(s % 2))
            carry = s // 2
            i, j = i - 1, j - 1
        if carry:
            result.append(str(carry))
        return "".join(result[::-1])