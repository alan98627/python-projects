def caesar(text, shift, encrypt=True):
    # Validate shift type
    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    # Validate shift range
    if shift < 1 or shift > 25:
        return 'Shift must be between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    # If decrypting, reverse shift
    if not encrypt:
        shift = -shift

    shifted_alphabet = alphabet[shift:] + alphabet[:shift]

    translation_table = str.maketrans(
        alphabet + alphabet.upper(),
        shifted_alphabet + shifted_alphabet.upper()
    )

    return text.translate(translation_table)


def encrypt(text, shift):
    return caesar(text, shift, encrypt=True)


def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)


def main():
    print("=== Caesar Cipher Tool ===")

    text = input("Enter text: ")
    action = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()

    try:
        shift = int(input("Enter shift (1-25): "))
    except ValueError:
        print("Invalid shift value. Must be a number.")
        return

    if action == 'e':
        result = encrypt(text, shift)
        print("Encrypted text:", result)

    elif action == 'd':
        result = decrypt(text, shift)
        print("Decrypted text:", result)

    else:
        print("Invalid option. Use 'e' or 'd'.")


if __name__ == "__main__":
    main()