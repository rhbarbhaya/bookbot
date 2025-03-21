from stats import pretty_print
import sys


def get_book_test(filepath):
    with open(filepath) as file:
        contents = file.read()
        return contents


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    book = get_book_test(filepath)
    pretty_print(book, filepath)


main()
