#read input
#sepatarte two lists by delimiter--sort
#store diff
#return a diff
#------------------------------------part 1--------------------------------------------
#read input
delimiter=' '
list1=[]
list2=[]

#sepatarte two lists by delimiter--sort
input_file=open(r"C:\Users\2000p\Desktop\advent_input.txt")
if input_file:
   for line in input_file:
      value=line.strip().split()

      if len(value)==2:
         list1.append(value[0])
         list2.append(value[1])

list1.sort()
list2.sort()


#store diff
list3=[0]*1000
for index in range(len(list1)):
  #print(index)
    list3[index]=abs(int(list1[index])-int(list2[index]))
    


#return a diff
       
result=sum(list3)
print(result)

#--------------------------------------part 2-----------------------------------
#finding similarity score
score=0
for i in list1:
   if i in list2:
      score+=int(i)*list2.count(i)

print(score)