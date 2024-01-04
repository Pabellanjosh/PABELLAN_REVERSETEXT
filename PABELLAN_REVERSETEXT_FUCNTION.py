def reverse_word():
    user_input = input("Enter a word: ")

    if user_input.isalpha():
        reversed_word = user_input[::-1]
        print(f"Reversed word: {reversed_word}")
    else:
        print("Error! Please input a text.")
        reverse_word()


reverse_word()