# Junmao Lin
# string manipulation

def is_palindrome(s):
    new_word = ""
    #ignore the spacing
    #only the letters and numbers matter
    for char in s: 
        if char.isdigit() or char.isalpha():
            new_word = new_word + char
    for i in range (0, int(len(new_word)/2)):
        if new_word[i] != new_word[len(new_word)-1-i]:
            return False
    return True


if __name__ == "__main__":
    test1 = is_palindrome("racecar")
    print("is_palindrome(\"racecar\") is:", test1)
    print()
    test2 = is_palindrome("raceboat")
    print("is_palindrome(\"raceboat\") is:", test2)
    print()
    test3 = is_palindrome("a man a plan a canal panama")
    print("is_palindrome(\"a man a plan a canal panama\") is:", test3)
    print()
    test4 = is_palindrome("a place to call up")
    print("is_palindrome(\"a place to call up\") is:", test4)
    print()
    test5 = is_palindrome("deified")
    print("is_palindrome(\"deified\") is:", test5)
    print()

