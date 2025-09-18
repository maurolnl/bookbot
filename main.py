import sys 
from stats import format_word_count, get_word_character_count, get_word_count_from_text

def get_book_text(file_path):
  with open(file_path) as f:
    return f.read()  

def main(): 
  if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  book_path = sys.argv[1]

  file_contents = get_book_text(book_path)
  num_of_words = get_word_count_from_text(file_contents)
  chars = get_word_character_count(file_contents)
  formatted_count = format_word_count(chars)

  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {book_path}...")
  print("----------- Word Count ----------")
  print(f"Found {num_of_words} total words")
  print("--------- Character Count -------")

  for char_dic in formatted_count:
    char = char_dic["char"]
    num = char_dic["num"]
    print(f"{char}: {num}")

main()