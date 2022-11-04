from flask import Flask
import binascii
import re
import argparse

app = Flask("badchttp")


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def main(path):
    hex_chars = re.findall(r"x([a-fA-F0-9]{2})", path)
    badchars = [f"{x}" for x in hex_chars]

    print(f"Skipping chars: {''.join(badchars)}")
    chars = generate_chars(badchars)
    return chars


def generate_chars(badchars: [str]) -> bytes:
    """
    generate all chars after filtering out badchars
    :param badchars: ["0a", "0d"]
    :return: "0102.."

    Credit https://github.com/the-c0d3r/buffer-overflow/
    """
    char_str = ""

    for x in range(1, 256):
        current_char = '{:02x}'.format(x)

        if current_char not in badchars:
            char_str += current_char

    return binascii.unhexlify(char_str)


def entrypoint():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", help="Port to listen on", default=5000, type=int)
    parser.add_argument("-l", "--listen", help="IP address to listen on (default 0.0.0.0)",
                        default="0.0.0.0")
    parser.add_argument("--debug", help="Turns debug mode off", action="store_false")
    args = parser.parse_args()

    app.run(host=args.listen, debug=args.debug, port=args.port)


if __name__ == "__main__":
    entrypoint()
