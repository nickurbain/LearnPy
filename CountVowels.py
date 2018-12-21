def main():
	count_vowels(input("Input string to count vowels: "))

def count_vowels(input_string):
	split = input_string.split()
	count = [0,0,0,0,0] #array represents count of a,e,i,o,u
	for x in range(len(split)):
		word = split[x]
		for y in range(len(word)):
			char = word[y]
			if (char == "a"):
				count[0] += 1
			elif (char == "e"):
				count[1] += 1
			elif (char == "i"):
				count[2] += 1
			elif (char == "o"):
				count[3] += 1
			elif (char == "u"):
				count[4] += 1
	print("a e i o u")
	print("- - - - -")
	print(*count)


if __name__ == "__main__":
    main()