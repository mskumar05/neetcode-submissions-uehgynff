class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            length = len(s)
            result += str(length)
            result += '#'
            result += s

        return result

    def decode(self, s: str) -> List[str]:
        i = 0
        result = []
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            newstr = s[j+1 : j+1+length]
            result.append(newstr)
            i = j + 1 + length
        return result