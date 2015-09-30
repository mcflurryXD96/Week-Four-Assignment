#
# File Header
#
# Add your name to this

# Define a function called piggy(string) that returns a string

vowels = "aeiouAEIOU"

def piggy(word):
	n = 0
	endword = ""
	
	for letter in word:
		# Check if letter is a vowel
		if letter in vowels:
			if n == 0:			# True?  We are done
				pig = word + "yay"
				break
		#		return pig
			else:
				pig = word[n:] = endword = "ay"
				break
			#	return pig
		
		else:
			# False? Consonant
			endword += word[n]
			n = n + 1
	print(pig)

# Open the file *getty.txt* for reading.  
infile = open("getty.txt", "r")

# Open a new file *piggy.txt* for writing.  
outfile = open("piggy.txt", "w")

# Read the getty.txt file into a string.  
gettystring = infile.read()

# Strip out bad characters (, - .).  
gettystring = gettystring.replace (",","")
gettystring = gettystring.replace ("-","")
gettystring = gettystring.replace (".","")

# Split the string into a list of words.  
gettylist = gettystring.split ()

# Create a new empty string.  
piggystring = ""

# Loop through the list of words, pigifying each one.  
for word in gettylist:

# Add the pigified word (and a space) to the new string.  
	if len(word) > 0
		piggystring = piggystring + piggy(word) + " "


# Write the new string to piggy.txt.  
print(piggystring, file = outfile)

# close the files.
infile.close()
outfile.close()