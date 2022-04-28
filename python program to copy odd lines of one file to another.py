file1 = open('siri.txt', 'r') 

# creating another file to store odd lines
file2 = open('siriupdated.txt', 'w') 

# reading content of the files
# and writing odd lines to another file
lines = file1.readlines() 
type(lines) 
for i in range(0, len(lines)): 
	if(i % 2 != 0): 
		file2.write(lines[i]) 

# closing the files
file1.close()
file2.close() 

# opening the files and printing their content
file1 = open('siri.txt', 'r') 
file2 = open('siriupdated.txt', 'r') 

# reading and printing the files content
str1 = file1.read()
str2 = file2.read()

print("siri content...")
print(str1)

print() # to print new line

print("siriupdated content...")
print(str2)

# closing the files
file1.close()
file2.close()