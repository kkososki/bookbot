import string

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    char_count = count_characters(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print()
    for key, value in char_count.items():
        print (f"The '{key}' character was found {value} times")
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    word_count = len(words)
    return word_count

def sort_on(dict):
    return dict["count"]

def count_characters(text):
    lowered_text = text.lower()
    alphabet = list(string.ascii_lowercase)
    temp_list = list()
    letter_list = list()
    count_list = list()
    for letter in alphabet:
        letter_count = lowered_text.count(letter)
        temp_dict = dict(letter = letter, count = letter_count)
        temp_list.append(temp_dict)
    temp_list.sort(reverse=True, key=sort_on)
    for i in range(len(alphabet)):
        temp_dict = temp_list[i]
        letter_list.append(temp_dict["letter"])
        count_list.append(temp_dict["count"])        
    char_count = dict(zip(letter_list, count_list))
    return char_count

main()