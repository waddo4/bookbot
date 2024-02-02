def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    chars = char_count(text)
    print(final_report(book_path,num_words,chars))
     

    # I made this its own function because it ended up being doing more than just the printing.
def final_report(book_path,num_words,chars):
    # I decided to work with tuples because I couldn't work out how else to sort the list.
    Char_list = list(chars.items())
    letters_list = []
    # Looping through the tuples, checking if it's a letter + appending and sorting it based on the tuple's 2nd index (the letter count value).
    for tuple in Char_list:
         if tuple[0].isalpha():
              letters_list.append(tuple)
    sorted_letters = sorted(letters_list, key=lambda x: x[1], reverse=True)

    # Print statements for the report
    print(f"===== Begin report of {book_path} =====")
    print(f"{num_words} words found in the document.")
    for tuple in sorted_letters:
            print(f"The {tuple[0]} character was found {tuple[1]} times.") 
    print(f"===== End Report =====")

    # Too lazy to work out how to return all the print statements/change the code.
    return ""

def char_count(text):
    count = {}
    for char in text:
        char = char.lower()
        count[char] = count.get(char, 0) + 1
    return(count)
    

def word_count(text):
        words = text.split()
        return len(words)

def get_book_text(path):
     with open(path) as f:
        return f.read()

main()