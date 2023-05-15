def encrypt_decrypt(message, shift, mode):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    if mode == "encode":
        for letter in message:
            if letter in alphabet:
                position = alphabet.index(letter)
                new_position = (position + shift) % 26
                result += alphabet[new_position]
            else:
                result += letter
    elif mode == "decode":
        for letter in message:
            if letter in alphabet:
                position = alphabet.index(letter)
                new_position = (position - shift) % 26
                result += alphabet[new_position]
            else:
                result += letter
    return result


while True:
    choice = input("Do you want to encode or decode a message? (encode/decode) ").lower()
    if choice == "encode" or choice == "decode":
        while True:
            message = input("Enter the message or type 'stop' to quit and change mode: ").lower()
            if message.lower() == "stop":
                break
            shift = int(input("Enter the shift amount: "))
            result = encrypt_decrypt(message, shift, choice)
            print(f"Your {choice}d message is:", {result})
    else:
        print("Invalid choice. Please enter either 'encode' or 'decode'.")
