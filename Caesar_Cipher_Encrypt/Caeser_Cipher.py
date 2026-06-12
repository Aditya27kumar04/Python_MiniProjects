import art

print(art.logo)

alphabet = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z'
]

def caesar(original_text, shift_amount, encode_or_decode):
    if encode_or_decode == "decode":
        shift_amount *= -1

    output_text = ""

    for letter in original_text.lower():
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + shift_amount) % len(alphabet)
            output_text += alphabet[new_position]
        else:
            output_text += letter

    print(f"Here is the {encode_or_decode}d result: {output_text}")


while True:
    direction = input(
        "Type 'encode' to encrypt or 'decode' to decrypt:\n"
    ).lower()

    text = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))

    caesar(
        original_text=text,
        shift_amount=shift,
        encode_or_decode=direction
    )

    restart = input(
        "Type 'yes' if you want to go again. Otherwise type 'no':\n"
    ).lower()

    if restart == "no":
        print("Goodbye!")
        break