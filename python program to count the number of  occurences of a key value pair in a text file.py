file= open("siri.txt", "r") 
dct = dict() 
 
for temp in file: 
    temp = temp.strip() 
    temp = temp.lower() 
    readLine = temp.split() 
    for i in readLine: 
        if i in dct: 
            dct[i] = dct[i]+1
        else: 
            dct[i] = 1
 
file.close() 
print("Count of: ")
for k in list(dct.keys()): 
    print("{} is {}".format(k,dct[k]))