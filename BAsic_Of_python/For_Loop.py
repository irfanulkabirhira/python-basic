#  for (int i =0 ; i<5 ; i++)
# 
# }
numbers =[5,10 ,15,20 ,25]
sum=0
for num in numbers :
    print(num)
    sum=sum+num
    if sum>20:
        print('Biger values',sum)
print(sum)

print()

nums =[20 , 30 , 40 , 50 ]
for count in nums:
    print(count)

print()
    # for Range 
print(range(1,10))

print()
for i in range(1,10,2):
    print(i)

# For charectar type
text ='pagal Hawer'
for char in text :
    print(char)

print()
# Importing array as a arr
import array as arr
# how to find spefic element of an array in python
x=arr.array('i', [40 , 60 , 70 ])
# to access the index 1
print('The element in the index 1 of the array is ', x[1])


