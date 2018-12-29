def main():
	count = count_words(input("Input string to count words: "))
	print("There are " + str(count) + " words in the string\n")

def count_words(input_string) -> int:
	split = input_string.split()
	return len(split)
	



if __name__ == "__main__":
    main()