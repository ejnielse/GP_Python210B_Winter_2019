#!/usr/bin/env python3

# Eric Nielsen
# Student ID: 1801963

#Ran a little short on time this week. Code functions as required but is
#not as efficient or as general as it could be and I didn't have time to
#incorporate all the guidelines at the bottom of the assignement. 
#Still pretty solid, though

#add groupby function b/c I couldn't figure out how to group without it
from itertools import groupby

#Create a Donor List
teams_list = ['Donor', 'Amount Donated']
donor_list =[('Daniel Cormier', 6345), ('Daniel Cormier', 78450.67),
            ('Daniel Cormier', 15450.50), ('Jon Jones', 100000.00),
            ('Robert Whittaker', 32675.00), ('Robert Whittaker', 43750.67),
            ('Robert Whittaker', 234.95), ('Tyron Woodley', 245000.00),
            ('Tyron Woodley', 325.50), ('Khabib Nurmagomedov', 500000),
            ('Khabib Nurmagomedov', 1000000)]

#Throwing in $40 for a good cause
donor_list.append(('Eric Nielsen', 40))

print()
command = 0

while command == 0:
    option = input("Would you like to: Send a Thank You, Create a Report, or Quit?")

    while option not in ["Send a Thank You", "send a thank you", "Create a Report",
                        "create a report", "Quit", "quit"]:
        option = input("Invalid Response: Send a Thank You, Create a Report, or Quit?")

    if option == "Send a Thank You" or option == "send a thank you":
        name = input("Please Enter Full Name of Donor: ")

        #show list of donors if user selects list
        if name == "List" or name == "list":
            output = []
            print()
            print("Donor List")
            print("-"*20)
            for donors in donor_list:
                if donors[0] not in output:
                    output.append(donors[0])
                    print(donors[0])
            print()
            name = input("Please Enter Full Name of Donor: ")
            amount = input("Please Enter a Donation Amount: ")
            amount = float(amount)

        else:
            amount = input("Please Enter a Donation Amount: ")
            amount = float(amount)

        donor_list.append((name, amount))
        print()
        print("Mr./Ms.",f"{name},",)
        print()
        print("Thank you so much for your generous donation of", f"${amount:,.2f}.")
        print()
        print("Rest assured that your generosity will ensure the future of our organization remains bright!")
        print()
        print("Sincerely - The UWPCE Python210B Winter 2019 Association")
        print()

    if option == "Create a Report" or option == "create a report":
        donor_list_2 = []
        donor_list_3 = []
        donor_list_5 = []
        donor_list_7 = []
        donor_list_8 = []

        #sum by name and find number of donations
        for i, g in groupby(sorted(donor_list), key = lambda x: x[0]):
            donor_list_2.append([i, sum(v[1] for v in g)])
        donor_list_2.sort(key=lambda x:x[1], reverse = True)
        dict_1={}
        for i in donor_list:
            if i[0] not in dict_1:
                dict_1[i[0]] = 1
            else:
                dict_1[i[0]] += 1

        #hot mess - don't ask me to expain this
        donor_list_3 = list(filter(lambda y:y != None, (map(lambda x:(x,dict_1.get(x)) if dict_1.get(x)>0 else None, dict_1.keys()))))

        donor_list_4 = donor_list_2 + donor_list_3

        unique_sorted = sorted(donor_list_4, key = lambda x: x[0])
        for key, group in groupby(unique_sorted, lambda x: x[0]):
            donor_list_5.append(list(group))
        donor_list_6 = [(x[0][0], [y[-1] for y in x]) for x in donor_list_5]
        donor_list_6.sort(key=lambda x:x[1], reverse = True)

        #set up the table
        print("")
        print(": Donor Name"," "* 9, ": Total Given"," "*2,": Num Gifts :","Average Gift :")
        print("-"*68)
        for i in donor_list_6:
            donor_list_7 = [(i[0], *i[1])]

            #add average to list tuples
            for i in donor_list_7:
                donor_list_8 = [(i[0], i[1], i[2], i[1]/i[2])]


                #for loop to align list items
                for i in donor_list_8:
                    print(":", i[0]," "*(19-len(i[0])),":",
                    f"${i[1]:,.2f}"," "*(13-len(str(f"${i[1]:,.2f}"))),":",
                    i[2]," "*(8-len(str(i[2]))),":",
                    f"${i[3]:,.2f}"," "*(11-len(str(f"${i[3]:,.2f}"))),":")

        print()

    #Exit the program
    if option == "Quit" or option == "quit":
        command = 1
