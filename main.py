from stats import counting_char
from stats import transform_dict
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
#    num_words=get_num_words(get_book_text("books/frankenstein.txt"))
#    print(f"{num_words} words found in the document")
    dict_char=counting_char(get_book_text("books/frankenstein.txt"))
    #print(f"count {dict_char}")
    list_dict=transform_dict(dict_char)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print("Found 75767 total words")
    print("--------- Character Count -------")
    for item in list_dict:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['count']}")
    print("============= END ===============")
main()