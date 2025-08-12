from operator import indexOf

my_list = []

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list.insert(1,15)
my_list2 = [50,60,70]
my_list = my_list + my_list2
my_list.pop()
my_list.sort()
nums = my_list.index(30)


print(my_list)
print(f'The index of 30 is {nums}')