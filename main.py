from stats import counting_char
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
#    num_words=get_num_words(get_book_text("books/frankenstein.txt"))
#    print(f"{num_words} words found in the document")
    list_char=counting_char(get_book_text("books/frankenstein.txt"))
    print(f"count {list_char}")
main()