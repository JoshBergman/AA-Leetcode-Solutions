# There is a solution where you reverse the string and compare it to the original string
# but it felt too cheaty


def isPalindrome(self, s: str) -> bool:
    def isValidChar(char):
        if char.isdigit() or char.isalpha():
            return True
        else:
            return False

    sLength = len(s) - 1
    head = 0
    tail = sLength

    while head <= tail:
        headChar = s[head].lower()
        tailChar = s[tail].lower()

        if not isValidChar(headChar):
            if head < sLength:
                head += 1
                continue

        if not isValidChar(tailChar):
            if tail > 0:
                tail -= 1
                continue

        if not headChar == tailChar:
            return False
        head += 1
        tail -= 1

    return True
