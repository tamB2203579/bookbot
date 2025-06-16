from stats import *
import sys

def get_book_text(filepath):
    print(f"Analyzing book found at {filepath}...")
    with open(filepath) as f:
        content = f.read()
    return content

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    content = get_book_text(sys.argv[1])
    print("----------- Word Count ----------")
    num_words = get_num_words(content)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    dict = count_characters(content)
    report = sorted(dict)
    for item in report:
        if item['char'].isalpha():
            print(f"{item["char"]}: {item["num"]}")
    
main()