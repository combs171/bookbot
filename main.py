import sys

def get_book_text(file_path):
	with open(file_path) as f:
		return f.read()

from stats import count_words
from stats import count_characters
from stats import sort_characters

def main():
	if len(sys.argv) !=2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)

	path_to_book_file = sys.argv[1]
	book_text = get_book_text(path_to_book_file)
	num_words = count_words(book_text)
	char_counts = count_characters(book_text)
	sorted_char_counts = sort_characters(char_counts)
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {path_to_book_file}...")
	print("----------- Word Count ----------")
	print(f"Found {num_words} total words")
	print("--------- Character Count -------")
	for y in sorted_char_counts:
		print(f"{y["character"]}: {y["count"]}")
	print("============= END ===============")

main()
