class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_map = {}
        res = []
        for word in strs:
            letters = list(word)
            letters.sort()
            key = ''.join(letters)

            if key in str_map:
                str_map[key].append(word)
            else:
                str_map[key] = [word]

        return [x for x in str_map.values()]
