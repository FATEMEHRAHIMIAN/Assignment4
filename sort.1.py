import numbers
list_1 = []
list_2 = []
for i in range(10):
    number = int(input("Entre your number \n"))
    list_1.append(number)
for i in range(len(list_1)):
    for j in range(0, len(list_1)-i - 1):
        if list_1[j] > list_1[j+1]:
            list_1[j], list_1[j+1] = list_1[j+1], list_1[j]
for i in range(len(list_1)):
    list_2.append(list_1[i])
print("sorted id => ", list_2)
