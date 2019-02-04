#!/usr/bin/env python3

# Eric Nielsen
# Student ID: 1801963



def option():

    print("Would you like to: Send a Thank You, Create a Report, or Quit?")

def thank_you():

    output = []
    for donors in donor_list:
        if donors[0] not in output:
            output.append(donors[0])

    while True:
        name = input("Please Enter Full Name of Donor or (list) to See Current Donors: ")
        if name == "List" or name == "list":
            print()
            print("Donor List")
            print("-"*20)
            for donors in output:
                print(donors)
            print()

        elif name not in output:
            print(f'{name} is a new donor.')
            amount = float(input("Enter the donation amount: "))
            donor_list.append((name, [amount]))
            print(f"{name} has been added to the donor list.")
            break
        elif name in output:
            name_index = output.index(name)
            amount = float(input("Enter the donation amount: "))
            donor_list[name_index][1].append(amount)
            print(f"{name}'s donation history has been updated.")
            break

    #send email
    print()
    print("Mr./Ms.",f"{name},",)
    print()
    print("Thank you so much for your generous donation of", f"${amount:,.2f}.")
    print()
    print("Rest assured that your generosity will ensure the future of our organization remains bright!")
    print()
    print("Sincerely - The UWPCE Python210B Winter 2019 Association")
    print()

def create_report():

    donor_list_2 = []
    for donor in donor_list:
        total_donations = float(sum(donor[1]))
        number_of_donations = len(donor[1])
        average = total_donations / number_of_donations
        donor_list_2.append([donor[0], total_donations, number_of_donations, average])
        donor_list_2.sort(key=lambda d: d[1], reverse=True)
    #print(donor_list_2)

    #set up the table
    print("")
    print(": Donor Name"," "* 9, ": Total Given"," "*2,": Num Gifts :","Average Gift :")
    print("-"*68)

    for i in donor_list_2:
        print(":", i[0]," "*(19-len(i[0])),":",
        f"${i[1]:,.2f}"," "*(13-len(str(f"${i[1]:,.2f}"))),":",
        i[2]," "*(8-len(str(i[2]))),":",
        f"${i[3]:,.2f}"," "*(11-len(str(f"${i[3]:,.2f}"))),":")

    print()

def main():

    select = ''
    while True:
        select = input("Would you like to: Send a Thank You, Create a Report, or Quit?")
        if select == "Send a Thank You" or select == "send a thank you":
            thank_you()
        elif select == "Create a Report" or select == "create a report":
            create_report()
        elif select == "Quit" or select == "quit":
            break
        else:
            print("Invalid Response. Please Try Again.")


if __name__ == "__main__":

    donor_list = [('Daniel Cormier', [6345, 78450.67, 15450.50]),
              ('Jon Jones', [100000.00]),
              ('Robert Whittaker', [32675.00, 43750.67, 234.95]),
              ('Tyron Woodley', [245000.00, 325.50]),
              ('Khabib Nurmagomedov', [500000.00, 1000000.00])]

    main()
