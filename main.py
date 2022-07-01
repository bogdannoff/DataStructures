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


# сортировка слиянием
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


# быстрая сортировка Хоара
import random

def qsort(l):

    if len(l)>1:
        c = l[random.randint(0, len(l)-1)]
        ll = [el for el in l if el<c]
        lc = list(filter(lambda el: el==c, l))
        lr = [el for el in l if el>c]
        l = qsort(ll)+lc+qsort(lr)
    return l


# Сортировка Шелла
def shellSort(l):
    step = len(l)//2
    while step > 0:
        for i in range(step, len(l)):
            j = i
            while l[j] < l[j-step] and j>=step:
                l[j], l[j - step] = l[j-step], l[j]
                j -=step
        step //=2
    return l


l1 = [-5, 6, 0, -3, 8, 1]
l2 = [random.randint(0, 100) for _ in range(100)]
l3 = list(map(lambda _: random.randint(0, 100), range(100)))
l4 = list(numpy.random.randint(0, 100, 10))

print(l1)
print(shellSort(l1))

print(l4)
print(shellSort(l4))



