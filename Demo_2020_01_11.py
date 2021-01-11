"""
This is a demo for List Tuple Set and Dictionary.
Date:2021_01_11
Written by Dr. Fan Song.
This demo is only for self studying.
List: Is an ordered and changeable collection. Duplicate members are allowed.
Tuple: Is an ordered and unchangeable collection. Duplicate members are allowed.
Set: Is an unordered and un-indexed collection. There are no duplicate members.
Dictionary: Is an unordered, variable and indexed collection. There are no duplicate members.
"""
print("------------------demo_list_start--------------------")
demo_list = ["Apple", "Banana", "Orange", "Watermelon", "Grape", "Lemon", "Mango"]
print(demo_list)
print(type(demo_list))
print(demo_list[1])  # Get list member by index
print(demo_list[-1])  # Get list member by index
print(demo_list[2:5])  # Get list member by index range, 2 included 5 excluded
print(demo_list[-4:-2])  # Get list member by index range, -4 included -2 excluded
demo_list[4] = "Cherry"  # Change list member by index.
print(demo_list)
# Traverse list by for loop
for x in demo_list:
    print(x)
# To determine if the specified item exists in the list, use the in keyword
if "Watermelon" in demo_list:
    print("Watermelon exists!")
else:
    print("Watermelon doesn't exist in demo_list!")
# To determine how many items are in the list, use the len() method
demo_len = len(demo_list)
print("demo_list's length is ", demo_len)

# To add an item to the end of the list, use the append() method
print(demo_list)
demo_list.append("Grape")
print(demo_list)
# To add an item at the specified index, use the insert() method
demo_list.insert(1, "Wiki")
print(demo_list)
# 删除项目:
# remove() delete specific items in the list.
# pop() if not set, it will delete the last item in the list.
# del() delete item by index.
# clear() delete all items in the list.
print("------------------demo_list_end--------------------")
print("------------------demo_tuple_start--------------------")
demo_tuple = ("Apple", "Banana", "Orange", "Watermelon", "Grape", "Lemon", "Mango")
print(demo_tuple)
"""
Change tuple value
After you create a tuple, you cannot change its value. Tuples are immutable, or also constant.
But there is a solution. You can convert tuples to lists, change lists, and then convert lists back to tuples.
"""
demo_tuple_tolist = list(demo_tuple)
demo_tuple_tolist[1] = "Kiwi"
demo_tuple = tuple(demo_tuple_tolist)
print(demo_tuple)
demo_tuple_sg_1 = ("Sg_obj1",)  # Single item tuple must use a comma.
demo_tuple_sg_2 = ("Sg_obj1")  # Single item tuple must use a comma.
print(demo_tuple_sg_1, " is of type", type(demo_tuple_sg_1))
print(demo_tuple_sg_2, " is of type", type(demo_tuple_sg_2))

tuple_adj = ("red", "green", "black")
tuple_obj = ("pen", "shoe", "ladder")
tuple_merge = tuple_obj + tuple_adj  # merge two tuples
print(tuple_merge)

for x in tuple_adj:
    for y in tuple_obj:
        print(x + y)
print("------------------demo_tuple_end--------------------")
print("------------------demo_set_start--------------------")
demo_set = {"Apple", "Banana", "Orange", "Watermelon", "Grape", "Lemon", "Mango"}
print(demo_set)  # Note: the collection is out of order, so you cannot determine the order in which items are displayed.
"""
You cannot access the items in the set by referencing the index because the set is unordered 
and the items have no index.
However, you can use the for loop to traverse the set item, or use the in keyword to query 
whether the specified value exists in the collection.
"""
# print(demo_set[1]) is wrong.
for x in demo_set:
    print(x)
# Once the collection is created, you cannot change items, but you can add new items.
print("------------------demo_set_end--------------------")
