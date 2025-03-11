def count_words(text):
        x = len(text.split())
        return x

def count_characters(text):
	text = text.lower()
	letter_count = {}
	for letter in text:
		if letter in letter_count:
			letter_count[letter] += 1
		else:
			letter_count[letter] = 1
	return letter_count

def sort_characters(char_counts):
	x = []
	for char in char_counts:
		if char.isalpha():
			x.append({"character": char, "count": char_counts[char]})
	def sort_on(dict):
		return dict["count"]
	x.sort(reverse=True, key=sort_on)
	return x
