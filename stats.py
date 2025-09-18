def get_word_count_from_text(text):
  word_list = text.split()
  return len(word_list)

def get_word_character_count(text):
  count = {}
  for c in text:
    c_lower = c.lower()
    if c_lower in count:
      count[c_lower] += 1
    else: 
      count[c_lower] = 1
  
  return count

def sort_on(items):
  return items["num"]

def format_word_count(word_count):
  formatted_count = []
  for key in word_count:
    if (key.isalpha()): 
      formatted_char = {"char": key, "num": word_count[key]}
      formatted_count.append(formatted_char)
  
  formatted_count.sort(reverse=True, key=sort_on)

  return formatted_count