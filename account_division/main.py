people = {
    "Name": [],
    "Amount" : [],
    "Final amount" : [],
    "Refund" : []
}


def names_of_people():
    number_people = int(input("Cantidad de personas: "))
    print("")
    count_people = 1
    for person in range(number_people):
        people["Name"].append(
            str(input(f"Nombre {count_people}: "))
        )
        count_people += 1
    print("")


def len_names():
    '''
    This function stores the length of people's names in a list.
    In the end, it is used to calculate the length of our table
    using the maximum length of the list.
    '''
    len_name_people = []
    for name in people["Name"]:
        len_name_people.append(len(name))
    return len_name_people


def amount_contributed():
    # Amount contributed by each person
    for name in people["Name"]:
        people["Amount"].append(
            float(input(f"Cantidad aportada por {name}: "))
        )
    print("")


def total_and_individual_amount():
    # Calculate the total amount
    total = sum(people["Amount"])
    print("Total: {} $".format(round(total,1)))
    print("")

    # Calculate individual amount
    individual_amount = total / len(people["Name"])
    print("A pagar c/u: {} $".format(
        round(individual_amount,1)
    ))
    print("")

    # Determine if the person should contribute or receive money
    for amount in range(len(people["Amount"])):
        final_amount = individual_amount - (people["Amount"][amount])
        if final_amount < 0:
            people["Refund"].append(abs(round(final_amount, 1)))
            people["Final amount"].append(float(0))
        else:
            people["Final amount"].append(abs(round(final_amount, 1)))
            people["Refund"].append(float(0))


def final_summary():
    print((('+--'+('-'*max(len_names()))+'--')*4)+'+')
    print('| '+'NOMBRE'+(' '*(max(len_names())-(len('NOMBRE'))+3))+'|'+
        ' '+'APORTADO'+(' '*(max(len_names())-(len('APORTADO'))+3))+'|'+
        ' '+'PAGAR'+(' '*(max(len_names())-(len('PAGAR'))+3))+'|'+
        ' '+'VUELTO'+(' '*(max(len_names())-(len('VUELTO'))+3))+'|')
    print((('+--'+('-'*max(len_names()))+'--')*4)+'+')

    final_list = list(zip(
        people["Name"],
        people["Amount"],
        people["Final amount"],
        people["Refund"]
    ))

    for value in final_list:
        print('| '+(value[0])+(' '*(max(len_names())-(len(value[0]))+3))+'|' +
            ' '+(str(value[1]))+(' '*(max(len_names())-(len(str(value[1])))+3))+'|'+
            ' '+(str(value[2]))+(' '*(max(len_names())-(len(str(value[2])))+3))+'|'+
            ' '+(str(value[3]))+(' '*(max(len_names())-(len(str(value[3])))+3))+'|')
    print((('+--'+('-'*max(len_names()))+'--')*4)+'+')


if __name__ == "__main__":

    names_of_people()

    amount_contributed()

    total_and_individual_amount()

    final_summary()
