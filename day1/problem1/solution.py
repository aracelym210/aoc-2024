# two empty lists for input
lista = []
listb = []

# read in file and split each line into two lists
with open('input.txt', 'r') as file:
    for line in file:
        lista.append(line.split()[0])
        listb.append(line.split()[1])

# sort lists
lista.sort()
listb.sort()

# iterate through lists and take the absolute difference between the lists
sum = 0

for index, value in enumerate(lista):
    diff = abs(int(value) - int(listb[index]))
    sum += diff

print(lista)
print(listb)
print(sum)
