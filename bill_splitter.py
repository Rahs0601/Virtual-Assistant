def sort_dict_by_value(d, reverse=False):
    return dict(sorted(d.items(), key=lambda x: x[1], reverse=reverse))


def split(highest_payer, lowest_payer):
    for (k, v) in highest_payer.items():
        temp = v
        for (a, b) in lowest_payer.items():
            temp2 = b
            while temp != 0 and b != 0:
                if temp - temp2 == 0:
                    print(f"{a} has to pay {temp2}rs to {k}")
                    temp = 0
                    temp2 = 0
                    break
                elif temp - temp2 < 0:
                    print(f"{a} has to pay {temp}rs to {k}")
                    temp2 = temp2 - temp
                    temp = 0
                    break
                else:
                    print(f"{a} has to pay {temp2}rs to {k}")
                    temp = temp - temp2
                    temp2 = 0
                    break
            highest_payer[k] = temp
            lowest_payer[a] = temp2


def equal():
    peps = {}
    for _ in range(num):
        name = input("enter the names ")
        amount = int(input("enter the amount "))
        peps[name.title()] = amount

    avg = sum(peps.values()) / num
    print("average = ", avg)

    highest_payer = {k: v - avg for (k, v) in peps.items() if v > avg}
    sort_dict_by_value(highest_payer)
    lowest_payer = {k: avg - v for (k, v) in peps.items() if v < avg}
    sort_dict_by_value(lowest_payer)

    print("People who should get", highest_payer)
    print("People who should give ", lowest_payer)
    split(highest_payer, lowest_payer)


def unequal():
    peps = {}
    for i in range(num):
        names = input('Enter the name of the person :')
        peps[names.title()] = 0

    # money paid by each person 
    for (k, v) in peps.items():
        b = {}
        for i in peps.keys():
            name = i
            amount = int(input(f'Enter the amount paid by {k} for {i} :'))
            b[name.title()] = amount
            peps[k] = b

    # his bank
    bank = {}
    for (k, v) in peps.items():
        sum = 0
        for b in v.values():
            sum += b
        bank[k.title()] = sum

    for (k, v) in bank.items():
        print(f'Total money debited from {k}\'s account is {v}')

    # total expenditure by individual for himself
    q = []
    for (k, v) in peps.items():
        for i in v.values():
            q.append(i)

    ex = []
    for i in range(len(q) - 1):
        sum1 = 0
        while i <= len(q) - 1:
            sum1 += q[i]
            i += num
        ex.append(sum1)

    z = {}
    j = 0
    for (k, v) in peps.items():
        z[k.title()] = ex[j]
        j += 1
    print("spent", z)
    highest_payer = {}
    lowest_payer = {}
    for (k, v) in bank.items():
        for (a, b) in z.items():
            if k == a:
                if v > b:
                    highest_payer[k.title()] = v - b
                else:
                    lowest_payer[k.title()] = b - v
    print("People who should get", highest_payer)
    print("People who should give ", lowest_payer)
    split(highest_payer, lowest_payer)


if __name__ == '__main__':
    print("\n \t WelCome To Bill splitter Made By Rah'S And Vagi\t \n")
    num = int(input('Enter the number of person\'s :'))
    print('Is splitting equally distributed or unequally distributed?')
    ans = input('Type equal or unequal\n')
    if ans == 'equal':
        equal()
    else:
        unequal()