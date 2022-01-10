
def sort_dict_by_value(d, reverse=False):
    return dict(sorted(d.items(), key=lambda x: x[1], reverse=reverse))
print("\n \t WelCome To Bill spliter Made By Rah'S\t \n")
num = int(input("Enter the number of person \n "))
peps = {}
for _ in range(num):
    name = input("enter the names ")
    amount = int(input("enter the amount "))
    peps[name.title()] = amount
avg = sum(peps.values()) / num
print("average = ", avg)
highest_payer = {k: v - avg for (k, v) in peps.items() if v > avg}
sort_dict_by_value(highest_payer)
print("People who should get", highest_payer)
lowest_payer = {k: avg -v for (k, v) in peps.items() if v < avg}
sort_dict_by_value(lowest_payer)
print("People eho should give ", lowest_payer)
for (k,v ) in highest_payer.items():
    temp =v
    for(a,b) in lowest_payer.items(): 
        temp2 =b    
        while (temp!=0 and  b!=0):
            if temp-temp2 == 0:
                print(f"{a} has to pay {temp2}rs to {k}")
                temp=0 
                temp2=0
                break      
            elif temp-temp2 <0:
                print(f"{a} has to pay {temp}rs to {k}")
                temp2=temp2-temp
                temp=0
                break      
            else:
                print(f"{a} has to pay {temp2}rs to {k}")
                temp=temp-temp2
                temp2=0     
                break
        highest_payer[k]=temp
        lowest_payer[a]=temp2