
# TC : O(N) , SC : O(N) due to recursive stack
def is_palindrome_recursive(s: str) -> bool:
    def check(left: int, right: int) -> bool:
        if left >= right:
            return True

        if s[left] != s[right]:
            return False

        return check(left + 1, right - 1)

    return check(0, len(s) - 1)


# Driver code
val = input("Enter the string: ").strip()

if is_palindrome_recursive(val):
    print("The given string is a palindrome")
else:
    print("The given string is not a palindrome")
