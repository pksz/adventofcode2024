#read input
#part1 read each line 
# and determine its safety
#variable list length-->brute force approach
#store count of safe values
#return safe docs


#   The levels are either all increasing or all decreasing.
#   Any two adjacent levels differ by at least one and at most three.
#dampner tolrates one level of bad level--set flag

#read input
#sepatarte two lists by delimiter--sort
#oworks but idk why
safe_document_count=0
part1=0
part2=0

input_file=open(r"C:\Users\2000p\Desktop\adventinput2.txt")
if input_file:
    for line in input_file:
        value=line.strip().split()
        int_vals=list(map(int, value))
       # print(value)
        flag1=1
        flag2=1

        # # #case 1 check increasing
        for index in range(len(int_vals)-1):        
             if(abs((int_vals[index])-(int_vals[index+1])))>3 or ((int_vals[index])==(int_vals[index+1])) or ((int_vals[index])>(int_vals[index+1])):
                if flag1==0:
                    break
                else:
                    flag1=0
    
                    
        else:
            safe_document_count+=1
            part1+=1
        

            
        # # #case 2 decreasing
        for index in range(1,len(int_vals)): 
            if(abs((int_vals[index])-(int_vals[index-1])))>3 or ((int_vals[index])<(int_vals[index-1])) or ((int_vals[index])==(int_vals[index-1])):
                if flag2==0:
                    break
                else:
                    flag2=0
                
                    
        else:
            safe_document_count+=1
            part2+=1

print(safe_document_count)
print(part1,part2)



    
        