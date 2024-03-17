def wordToNum(word):
    total = 0
    i = 10000
    for letter in word:
        num = ord(letter.lower())-96
        total = total + num * i
        i = i / 100
    print(word,total)
    return int(total)

def numToWord(num):
    word=""
    numstr = str(num)
    if(len(numstr)==5):
        numstr = "0"+numstr
    for index in range(0,6,2):
        if(index<len(numstr)):
            segment= numstr[index:index+2]
            chrnum=(int(segment))
            if(chrnum==0):
                word = word+' '
            else:                
                word = word + chr(chrnum+96)
            print(numstr,index,segment,chrnum,word)
    print("numToWord",num,word)
    return word

for num in [10,100]:
    input_filename = "./in_abc"+str(num)+".txt"
    output_filename = "./out_abc"+str(num)+"_sample_actual.txt"
    print(input_filename)
    print(output_filename)
    file = open(input_filename)
    file_out = open(output_filename,'w')
    linesRaw = file.readlines()
    arraySize = 272727
    A = []
    for i in range(0,arraySize):
        A.append(0)
    lineIndex=1
    while(lineIndex<=(len(linesRaw)-1)):
        words = linesRaw[lineIndex].split()
        if(len(words)==0):
            break
        for word in words:
            A[wordToNum(word)] = A[wordToNum(word)] + 1
        lineIndex=lineIndex+1
    i=0
    for a in A:
        for j in range(0,a):            
            file_out.write(numToWord(i) + " ")
        i=i+1