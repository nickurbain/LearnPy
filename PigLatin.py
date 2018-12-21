def main():
	pig_latin(input('Input String: '))

def pig_latin(input_string):
	split = input_string.split(" ")
	output = []
	for x in range(len(split)):
		untranslated = split[x]
		initial = ""
		ending = ""
		for c in range(len(untranslated)):
			char = untranslated[c]
			if (char != 'a') and (char != 'e') and (char != 'i') and (char != 'o') and (char != 'u'):
				initial += char
			else:
				ending = untranslated[c:]
				break;
		translated = ending.lower() + initial.lower() + "ay"
		if (x == 0):
			output.append(translated.capitalize())
		else:
			output.append(translated)
	print(*output)


if __name__ == "__main__":
    main()