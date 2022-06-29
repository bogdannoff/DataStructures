import random, numpy

# сортировка выбором
def selectionSort(l):
    for i in range(len(l)):
        for j in range(i, len(l)):
            if l[j] < l[i]:
                l[i], l[j] = l[j], l[i]
    return l

# сортировка вставками
def insertionSort(l):
    for i in range(len(l)):
        for j in range(i, 0, -1):
            if l[j] < l[j-1]:
                l[j-1], l[j] = l[j], l[j-1]
            else:
                break
    return l


# сортировка пузырьком
def bubleSort(l):
    for i in range(len(l)):
        for j in range(len(l)-i-1):
            if l[j+1] < l[j]:
                l[j], l[j+1] = l[j+1], l[j]
    return l


def mergeSort(l):

    def mergeLists(l1, l2):

        l = []
        n = len(l1)
        m = len(l2)
        i, j = 0, 0

        while i < n and j < m:
            if l1[i] < l2[j]:
                l.append(l1[i])
                i += 1
            else:
                l.append(l2[j])
                j += 1

        l += l1[i:] + l2[j:]

        return l


    n1 = len(l)//2
    l1 = l[:n1]
    l2 = l[n1:]

    if len(l1)>1:
        l1 = mergeSort(l1)
    if len(l2)>1:
        l2 = mergeSort(l2)

    return mergeLists(l1, l2)

l1 = [-5, 6, 0, -3, 8, 1]
l3 = [random.randint(0, 100) for _ in range(100)]
l2 = list(map(lambda _: random.randint(0, 100), range(100)))
l1 = list(numpy.random.randint(0, 100, 10))

print(l1)
print(mergeSort(l1))


