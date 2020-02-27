list1=[1,2,3,4,5,6]
list2=["one","Two","Three","Four","Five","Six"]

zipped_list=list(zip(list1,list2))
print(zipped_list)

unzipped=list(zip(*zipped_list))

print(unzipped)

items=["apple","Banana","Graps","Orange"]
counts=[2,3,5,1]
prices=[1,2,0.2,0.8]

sentences=[]

for (item,count,price) in zip(items,counts,prices):
    item,count,price=str(item),str(count)+str(price)
    sentence="I bought "+count+" "+item+" "+"for "+price+" USD"
    sentences.append(sentence)

print(sentences)
