import random as rd

# Define functions for each kind of sort.
def selection_sort(unsted_ls):
    for x in range(len(unsted_ls)):
        for y in range(len(unsted_ls)):
            if unsted_ls[x] < unsted_ls[y]:
                unsted_ls[x],unsted_ls[y] = unsted_ls[y],unsted_ls[x]
    print(unsted_ls)

def bubble_sort(unsted_ls):
    for x in range(len(unsted_ls)):
        z = 1
        for y in range(len(unsted_ls)-1):
            if unsted_ls[y] > unsted_ls[z]:
                unsted_ls[y],unsted_ls[z] = unsted_ls[z],unsted_ls[y]
            z +=1
    print(unsted_ls)

def insertion_sort(unsted_ls):
    sorted_list
    for x in range(len(unsted_ls)):
        for y in range(len(unsted_ls)):
            

unsorted_list = [x for x in range(101)]
rd.shuffle(unsorted_list)
bubble_sort(unsorted_list)
