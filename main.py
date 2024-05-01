def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = count_characters(text)
    sorted_char_count = sort_characters(char_count)
    print_report(book_path, num_words, sorted_char_count)

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def count_characters(text):
    char_dict = {}
    for char in text.lower():
        if char.isalpha():  # counting only alphabetic characters
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    return char_dict

def sort_characters(char_dict):
    char_list = [{"char": k, "count": v} for k, v in char_dict.items()]
    char_list.sort(key=lambda item: item["count"], reverse=True)
    return char_list

def print_report(book_path, num_words, sorted_char_count):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    for item in sorted_char_count:
        print(f"The '{item['char']}' character was found {item['count']} times")
    print("--- End report ---")

main()
