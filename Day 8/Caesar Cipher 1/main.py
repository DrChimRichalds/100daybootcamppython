alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
original_letter =''

# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
def encrypt(original_text, shift_amount):
    original_text_lower = original_text.lower()

# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.
    new_text = ""
    new_letter= ""
    old_letter_pos = 0
    shift_letter_pos = 0
    for i in range(len(original_text)):
        original_letter = original_text[i]
        old_letter_pos = alphabet.index(original_letter)
        shift_letter_pos= old_letter_pos + shift_amount
        if shift_letter_pos > len(alphabet):
            shift_letter_pos = len(alphabet)
            shift_letter = alphabet[shift_letter_pos]
            new_text += shift_letter
            print(new_text)
        else:
            shift_letter = alphabet[shift_letter_pos]
            new_text += shift_letter
            print(new_text)


# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.
encrypt(text,shift)

