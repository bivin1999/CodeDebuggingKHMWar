for i in range(int(input())): #added int() 
        word = input().upper()#removed word.upper and added .upper()
        vowels = ['A','E','I','O','U']
        count = 0 #== to = 
        for j in range(1,len(word)):#added colon and length to len 
                if word[j] in vowels:#removed []
                        if j == 0: #= to == 
                                count+=1 #++ to +=
                        elif word[j+1] in vowels:#removed []
                                count+=1#added this statement 
                                break
                        else:
                                count+=1 #++ to +=
        print (count) 