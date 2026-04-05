class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        for string in strs:
            sorted_string = ''.join(sorted(string))
            if sorted_string in hashMap:
                hashMap[sorted_string].append(string)
            else:
                hashMap[sorted_string] = [string]

        return list(hashMap.values())