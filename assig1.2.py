#creating a list 
from operator import le


list1=["apple","banana","Cherry"]
print(list1)
#list allow Duplicates
listD=["apple","apple","banana","Cherry","Coconut","Strawberry"]
print(listD)
#len function is used to Determine how many elements is in list 
print(len(listD))
#list Allows string int boolean data types
list2=[1,5,3,9]
list3 = [True, False, False]
print(list1)
print(list2)
print(list3)
#list() costructor is use to make list
thislist=list(("apple","banana","Cherry"))
print(thislist)
#we can acess single elemnt in list  usinging indexing
print(thislist[1]) 
#acessing by negative indexing
print(thislist[-1])
#if in list
if "apple" in listD:
    print("Yes apple is present")
#WE Can Change item value
listD[1]="Coconut"
print("changed First item value")
print(listD)
#change Element in specific Range
listD[1:3]=["blackcurrant","Watermelon"]
print("change Element in specific Range")
print(listD)
#to Insert Element in List
#insert method is used to add item at specified index
listD.insert(2,"grapes")
print("list After insertion at 2 nd index")
print(listD)
#Append method is used to Add Element At the end of the list
print("Adding Element Using Append Method ")
listD.append("Orange")
print(listD)
#extend Method is used to add element from another list to current list 
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print("List After using Extend Method")
print(thislist)
#reomve method is used to remove element from the list 
#for using remove method we have to pass name of item which is to be removed
thislist.remove("apple")
print("list after removing apple using remove method")
print(thislist)
#pop method is used to remove element at specified index we have to pass the index of item to be removed
tropical.pop(1)
print("list after poping the element at 1 index")
print(tropical)
#del method is also used to remove element at specified index
tropical = ["mango", "pineapple", "papaya"]
del tropical[0]
print("After using Del keyword ")
print(tropical)
#Clear method is used to delet all item in the list
print("before using Clear method")
print(tropical)
tropical.clear()
print("After using Clear method list is: ")
print(tropical)
#loops in list
thislist = ["apple", "banana", "cherry"]
print("Using For Loop")
for x in thislist:
  print(x)
#by passing index using len function in range function
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])  
#using While loop 
  