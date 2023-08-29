value = input('Enter your value: ')
print('Value entered: ', value)

N = input('Enter a positive number: ')
print('Number entered: ', N)

dict = {}
for i in range(int(N)):
    value = input('Enter your value: ')
    print('Value entered: ', value)
    dict[i] = value

inal_value = input('Enter your value: ')
k = 0
for i in list(dict.keys()):
    if dict[i] == final_value:
        print('Index of your input: ',i+1)
        k = 1
        break
if k==0:
    print('Index of your input: ',-1)
