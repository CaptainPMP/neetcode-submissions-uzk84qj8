class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        # make all lowercase
        s = s.lower()


        # forbidden string
        # forbidden = "!@#$%^&*()_+,./<>?"
        # for forbidden_letter in forbidden:
        #     if forbidden_letter in s:
        #         s.replace(forbidden_letter, "")

        # allowed character
        allowed_char = "qwertyuiopasdfghjklzxcvbnm1234567890"

        # if s letter is not in allowed_char then replace with ""
        for letter in s:
            if letter not in allowed_char:
                s = s.replace(letter, "")

        print(s)

        while len(s) > 1:
            if s[0] == s[-1]:
                s = s[1:-1]
            else:
                return False
        return True