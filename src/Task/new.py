num_input = int(input("Check wether number is palindrome or not"))

rev_num = int(str(num_input)[::-1])


if num_input == rev_num:
    print("Yay! It's a palindrome")
else:
    print("Yay! It is not a palindrome")


