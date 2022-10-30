from flask import Flask
import binascii

app = Flask(__name__)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def main(path):
    badchars = [f"\\{x}" for x in path.split("/")]

    return generate_chars(badchars)


def generate_chars(badchars: [str]) -> bytes:
    """
    generate all chars after filtering out badchars
    :param badchars: ["\\x0a", "\\x0d"]
    :return: "0102.."

    Credit https://github.com/the-c0d3r/buffer-overflow/
    """
    char_str = ""

    for x in range(1, 256):
        current_char = "\\x" + '{:02x}'.format(x)

        if current_char not in badchars:
            char_str += current_char[2:]
            # remove the leading "\x"
    return binascii.unhexlify(char_str)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
