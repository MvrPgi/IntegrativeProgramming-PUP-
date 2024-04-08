#thislist =["apple","banana","cherry","orange","kiwi","melon","mango"]
#thislist[1:3] = ["strawberry","raspberry"]
#print(thislist)


#thislist =["apple","banana","cherry","orange","kiwi","melon","mango"]
#thislist.insert(2,"raspberry")
#print(thislist)

#tropical =["orange","kiwi","melon","mango"]

#//INSERT
thislist =["apple","banana","cherry","orange","kiwi","melon","mango"]
thislist.append("raspberry")
print(thislist)


#//EXTEND
thislist =["orange","kiwi","melon","mango"]
tropical =["raspberry"]
thislist.extend(tropical)
print(thislist)

#//DELETE
thislist =["orange","kiwi","melon","mango"]
tropical =["raspberry"]
thislist.remove("mango")
print(thislist)