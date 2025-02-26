#write a recursive function to print all elemnts in a list.
#hint:use list & index as parameters.

def print_list(list,idx=0):
    if(idx==len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)

cities=["Nagpur","Mumbai","Pune","Delhi"]
print_list(cities)
