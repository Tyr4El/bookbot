def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
def count_words(string_book):
    list_words=string_book.split()
    return len(list_words)
def main():
    num_words=count_words(get_book_text("books/frankenstein.txt"))
    print(f"{num_words} words found in the document")
main()