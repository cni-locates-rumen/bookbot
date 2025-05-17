import sys
from stats import get_num_words, count_symbols, list_sorted_symbols

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_location = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_location}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(get_book_text(book_location))} total words")
    print("--------- Character Count -------")
    sorted_list = list_sorted_symbols(count_symbols(get_book_text(book_location)))
    for item in sorted_list:
        print(f"{item['char']}: {item['num']}")

if __name__ == "__main__":
    main()

