class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1 = {}
        map2 = {}
        for i in s:
            map1[i] = map1.get(i, 0) + 1
        for j in t:
            map2[j] = map2.get(j, 0) + 1
        print(f"{map1} \n {map2}")
        return map1 == map2