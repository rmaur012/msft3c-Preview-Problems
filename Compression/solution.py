def compress(stringer):
	uncomp_str = stringer
	cmprsd_str = ""


	while(uncomp_str != ""):
		currChar = uncomp_str[0]
		charCount = 1
		while(charCount < len(uncomp_str) and uncomp_str[charCount] == currChar):
			charCount = charCount + 1

		if(charCount != 1):
			cmprsd_str = cmprsd_str + str(charCount) + currChar
		else:
			cmprsd_str = cmprsd_str + currChar
		
		#Slice off the chars counted to be similar
		uncomp_str = uncomp_str[charCount:]

		

	return cmprsd_str

reader = open('input.txt', 'r')

#runs is the number of compressions to do
runs = int(reader.readline().strip('\n'))

print(runs)

while(runs != 0):
	uncomp_str = reader.readline().strip('\n')
	print(compress(uncomp_str));
	runs = runs - 1

reader.close()
