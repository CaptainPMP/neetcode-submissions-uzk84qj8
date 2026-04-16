class Solution:
    def encode(self, strs: List[str]) -> str:
        strs_encoded = ""
        for element in strs:
            strs_encoded += f"{str(len(element))}#{element}"
        print(strs_encoded)
        return strs_encoded


    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])

            i = j + 1

            ans.append(s[i: i + length])

            i += length

        
        print(ans)
        return ans
