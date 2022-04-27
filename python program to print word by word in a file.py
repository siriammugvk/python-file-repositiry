

# file word by word
   
# opening the text file
with open('siri.txt','r') as file:
   
    # reading each line    
    for line in file:
   
        # reading each word        
        for word in line.split():
   
            # displaying the words           
            print(word) 