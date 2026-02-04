import argparse


def caesar_cipher(text, shift, decrypt=False):
    result = []
    shift = shift % 26

    if decrypt:
        shift = -shift

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result.append(chr((ord(char) - base + shift) % 26 + base))
        else:
            result.append(char)

    return ''.join(result)


def main():
    parser = argparse.ArgumentParser(
        description="Caesar Cipher CLI Tool (Windows)"
    )

    parser.add_argument(
        "-t", "--text",
        required=True,
        help="Text to encrypt or decrypt"
    )

    parser.add_argument(
        "-s", "--shift",
        type=int,
        required=True,
        help="Shift value"
    )

    parser.add_argument(
        "-d", "--decrypt",
        action="store_true",
        help="Decrypt instead of encrypt"
    )

    args = parser.parse_args()
    print(caesar_cipher(args.text, args.shift, args.decrypt))


if __name__ == "__main__":
    main()
