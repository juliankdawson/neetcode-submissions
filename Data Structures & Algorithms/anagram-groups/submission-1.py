class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # common key
        # sort string of characters
        # key: string, value: strs[]

        # one pass if key -> store, if not new key => store
        # return values in array called res
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
