#Create a list.
fruitList = ["apple", "banana", "cherry", "Grapes", "Orange"]
print(fruitList[0])
#update the index of the list.
fruitList[2] = "pear" #replace 2 with pear.
fruitList.append("pear")#Add pear to end of list.
fruitList.insert(2, "pear") #insert into index to of list.
fruitList.pop(2) #Remove item at index 2 in the list.
print(fruitList)
#print a range excluding the end of range item, [5] in this case.
print (fruitList[2:5])#will print from [2] to [4].
