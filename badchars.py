from flask import Flask
import binascii
import re

app = Flask(__name__)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def main(path):
    hex_chars = re.findall(r"x([a-fA-F0-9]{2})", path)
    badchars = [f"{x}" for x in hex_chars]

    chars = generate_chars(badchars)
    print(chars)
    return chars


def generate_chars(badchars: [str]) -> bytes:
    """
    generate all chars after filtering out badchars
    :param badchars: ["0a", "0d"]
    :return: "0102.."

    Credit https://github.com/the-c0d3r/buffer-overflow/
    """
    char_str = ""
    print(badchars)

    for x in range(1, 256):
        current_char = '{:02x}'.format(x)

        if current_char not in badchars:
            char_str += current_char

        else:
            print(current_char)

    return binascii.unhexlify(char_str)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
