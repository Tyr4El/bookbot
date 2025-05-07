import sys

from stats import counting_char, get_num_words
from stats import transform_dict

def get_book_text(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read() # function read returns a string of the whole input/file
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        sys.exit(1)
    except PermissionError:
        print(f"Error: You do not have permission to access {file_path}.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred:{e}")
        sys.exit(1)

def main():
#    num_words=get_num_words(get_book_text("books/frankenstein.txt"))
#    print(f"{num_words} words found in the document")
    print("Enter book filepath:")
# change everything to use readline() instead of file.read()
# and reread the part to use try... except for everything that needs testing.

    if len(sys.argv)==2:
        file_path=sys.argv[1]
        dict_char=counting_char(get_book_text(file_path))
    else:
        print("Error, Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    #print(f"count {dict_char}")
    list_dict=transform_dict(dict_char)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}") #change this line for answering to the specific title #done #sys.argv is a variable universal to the whole main
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(get_book_text(file_path))} total words")# change this number of words to a variable
    print("--------- Character Count -------")
    for item in list_dict:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['count']}")
    print("============= END ===============")
main()