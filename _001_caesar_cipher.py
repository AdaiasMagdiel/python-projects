import re


def encode(string: str, route: int = 3) -> str:
    encoded = ''

    for char in str(string):
        if re.match(r'\W', char):
            encoded += char
            continue

        encoded += chr(ord(char) - route)

    return encoded


def decode(string: str, route: int = 3) -> str:
    decoded = ''

    for char in str(string):
        if re.match(r'\W', char):
            decoded += char
            continue

        decoded += chr(ord(char) + route)

    return decoded


if __name__ == '__main__':
    mode = ''

    while not (mode.startswith('d') or mode.startswith('e')):
        mode = input('Mode -> decode (d) or encode (e): ').lower()

        if mode[0] not in ['d', 'e']:
            print('Invalid option, try again!')

    mode = 'encode' if mode.startswith('e') else 'decode'

    string = input(f'Text to {mode}: ')

    print(globals()[mode](string))
