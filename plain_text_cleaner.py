import sys

from unidecode import unidecode


array = [] # Array will contain all the clean lines

# clean and remove all characters that do not bellong to the alphabet and make them all uppercase
def cleanFromFile(input_file_string : str) -> str:
	# Open file and parse it
	with open(input_file_string , "r") as input_file:



		# Iterate throught every line of the file
		for line in input_file:

			# parse every char in the line and remove non alphanumeric chars
			clean_line = ''.join(chr for chr in line if chr.isalnum())

			# remove numbers from a line
			clean_line = ''.join(chr for chr in clean_line if not chr.isnumeric())

			# remove accentuation and other weird characters
			clean_line = unidecode(clean_line)


			# convert all chars to allCaps
			clean_line = clean_line.upper()

			# If the line is not empty
			if clean_line != "":
				array.append(clean_line)

	clean_line = ''.join(line for line in array)

	return clean_line


if __name__ == "__main__":

	# get args from command line
	argv = sys.argv
	# if inputFile in not present
	if len(argv) != 2:
		print("Usage: python3 plain_text_cleaner.py inputFile")
		sys.exit(2)

	# get string from inputFile
	input_file_string = argv[1]
	
	clean_line = cleanFromFile(input_file_string)

	print(clean_line)
