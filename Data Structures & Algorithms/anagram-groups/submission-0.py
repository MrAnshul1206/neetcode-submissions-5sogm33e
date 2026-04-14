class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grp = {}

        for word in strs:
            sort = "".join(sorted(word))  # word ko sort kar diya

            if sort not in grp:
                grp[sort] = []

            grp[sort].append(word)

        return list(grp.values())