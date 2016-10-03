#  coding=utf-8
#Defining methods
def dollar_to_yen(dollar, rate=100):
    return dollar * rate

_dollar = 10
print('$ {} ->Yen {} '.format(_dollar,dollar_to_yen(_dollar, 90)))


# List is mutable for argument
_lst =[1, 2, 3]

def power(list):
    print("list: {}".format(id(list)))
    # list does not change if list is used again
    list = [num**2 for num in list]
    print("list: {}".format(id(list)))

def power_1(list):
    for num in list:
        # list is changed
        list[num-1] = num**2

power(_lst)
print(_lst) #[1, 2, 3]
power_1(_lst)
print(_lst) #[1, 4, 9]

# multiple average
def average(*num):
    return sum(num)/len(num)

print(average(1,2,3,4,5))

# argment as dictionary
def print_dic(**dic):
    return print(dic)

num_dic = {1: 'one', 2: 'two', 3: 'three'}
print_dic(num =1, name = 'one') #{'name': 'one', 'num': 1}

smaller = lambda n1, n2: n2 if n2 < n1 else n1

print(smaller(2,9))
print(smaller(9,3))

# first class object
def to_cm(inch):
    return inch * 2.54

## list, map
inches = [2, 5, 7.5]
for cm in map(to_cm, inches):
    print(cm)
cms = list(map(to_cm, inches))
print(cms)

lambda_cms = [n * 2.54 for n in inches]
print(lambda_cms) #[5.08, 12.7, 19.05]

## filter
filter_cms = []
for inch in filter(lambda i: i > 3, inches):
    filter_cms.append(inch * 2.54)
print(filter_cms) #[12.7, 19.05]

## sorted
names = {"Taro":14, "Hanako":45, "Jiro":33, "Ken":21}
for name in sorted(names.items(), key= lambda n:n[1]):
    print("{}:{}".format(name[0], name[1]))
