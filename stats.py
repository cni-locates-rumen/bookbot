
def get_num_words(text_file):
    word_count = text_file.split()
    return len(word_count)

def count_symbols(text):
    symbols = {}
    words = []
    for symbol in text.lower():
        if symbol not in symbols:
            symbols[symbol] = 1
        else:
            symbols[symbol] += 1
    return symbols

def sort_on(dict):
    return dict["num"]

def list_sorted_symbols(symbols):
    listed_symbols = []
    for key in symbols:
        listed_symbols.append({"char": key, "num": symbols[key]})
    
    # Sort the list in-place
    listed_symbols.sort(reverse=True, key=sort_on)
    
    return listed_symbols

