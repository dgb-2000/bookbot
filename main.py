from stats import get_num_words, get_char_count, get_report
import sys


def get_book_text(path):
    with open(path) as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path = sys.argv[1]
        text = get_book_text(path)
        num_words = get_num_words(text)
        char_dict = get_char_count(text)
        char_report = get_report(char_dict)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for char in char_report:
            if char["char"].isalpha():
                print(f"{char['char']}: {char['num']}")
        print("============= END ===============")


main()
