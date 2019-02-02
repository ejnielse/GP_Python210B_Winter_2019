#!/usr/bin/env python3

# Eric Nielsen
# Student ID: 1801963

#Task 1
fnames = (2, 123.4567, 10000, 12345.67)
print("Task 1")
print("file_{:03d} : {:.2f}, {:.2e}, {:.2e}".format(*fnames))
print("")

#Task 2
print("Task 2")
name = (2, 123.4567, 10000, 12345.67)
print(f"file_{name[0]:03d}, {name[1]/1000:.2%}, {name[2]:b}, {name[3]:,}")
print("")

#Task 3
print("Task 3")
tuple = (34, 56, 63, 12, 7)
def formatter(in_tuple):
    if type(in_tuple) == int:
        print("The number is:",in_tuple)
    else:
        length = len(in_tuple)
        form_string = ("{:d}, " * (length -1)) + "{:d}"
        print("The ", len(in_tuple)," numbers are:", form_string.format(*in_tuple))

formatter(tuple)
print("")

#Task 4
print("Task 4")
five_element_tuple = ( 4, 30, 2017, 2, 27)
index = [3, 4, 2, 0, 1]
five_element_sort = []

for i in index:
    five_element_sort.append(five_element_tuple[i])

formatted = "{:02d} {:d} {:d} {:02d} {:d}".format(*five_element_sort)

print(formatted)
print("")

#Task 5
print("Task 5")
four_element_list = ['oranges', 1.3, 'lemons', 1.1]
print("f-string 1")
print(f"The weight of an {four_element_list[0]:.6} is {four_element_list[1]}"
f" and the weight of a {four_element_list[2]:.5} is {four_element_list[3]}")
print("")

print("f-string 2")
print(f"The weight of an {four_element_list[0].upper():.6} is {four_element_list[1] * 1.2}"
f" and the weight of a {four_element_list[2].upper():.5} is {four_element_list[3] * 1.2}")
print("")

#Task 6a
print("Task 6")
table_tuple = (('Eric', 37, 1149.57), ('Julian', 31, 150), ('Jason', 45, 343674.92))

#Add curency format to cost
def alignment_table(another_tuple):
    #Print out table
    for i in range(len(another_tuple)):
        print("{0:<7}{1:^5}${2:<3,.2f}".format(*another_tuple[i]))

alignment_table(table_tuple)
print("")

#Task 6b

cons_tuple_1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
cons_tuple_2 = (11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
cons_tuple_3 = (211, 212, 213, 214, 215, 216, 217, 218, 219, 220)

print(('{:5d} ' * len(cons_tuple_1)).format(*cons_tuple_1))
print(('{:5d} ' * len(cons_tuple_2)).format(*cons_tuple_2))
print(('{:5d} ' * len(cons_tuple_3)).format(*cons_tuple_3))
