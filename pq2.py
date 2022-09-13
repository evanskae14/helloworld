# a list is a sequence if iteams 
## 1D lists like a simp=gle row or a single column 
# declare a list [] and a comma seperated list of values 
#          0 1  2  3 
list_int= [0,1,10,20]
# it stores the data togther whihc means only one varoable name used by an offset 
# there are uniqueindexs for each team mof a  list 
#0-based... meaning the first element is at 0, and the last elementr is at index n-1
# where n is the number of elements in the lsit 
 
print(list_int[0])
print(list_int[-4])

#types can be mixed in a list 
list_numbers = [0,0.0,1,-2]
print(list_numbers)
print(type(list_numbers))
# lists are mutable(they can be changed once they are declared) 
list_numbers[0]="hello"
print(list_numbers)

#use len() to find out how many elemenst are in alist 
print(len(list_numbers))
list_numbers.append("another element")
# print out the last elemtn in the list .. supose we don't know at compile time exactly how many elements are in the list 
print(list_numbers[len(list_numbers)-1])

# we can declare na empty list 
empty_list = []
print(empty_list)

# we can have lists if lists (2d or ND )
nested_list = [[0,1],[2],[3],[4,5],[]]
print(len(nested_list))
print(len(nested_list[0]))

# looping through list items 
candies = ["twix", "reeses", "oreos", "snickers" ]
print(candies)

for candy in candies: 
    print(candy)


i = 0 
while i < len(candies):
      print (i, candies[i])
      i += 1

i=0
for i in range(len(candies)):
        print (i, candies[i])


# common list operators 
# list concatenation.. adding 2 lists together 
print(candies)
candies += ["m&ms ", "starburst"]
print(candies)
# list repetition...repeating elements in a list
bag_o_candies= 5 * ["twix", "snikcers"] 
print(bag_o_candies)

#list slicing 
# grab sublist of list 
print(candies)
print(candies[1:3])# : is the slice operator. start index is inclusive, end index is excutive
# end index is exclusive 
# # if you ever need a copy of a list, you can simply use the : with no start or end indience 
copy_of_candies = candies[:]
copy_of_candies[0]= "TWIX"
print(copy_of_candies) 
print(candies)


#list methods
candies.remove


