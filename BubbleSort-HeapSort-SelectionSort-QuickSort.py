#!/usr/bin/env python
# coding: utf-8

# Insertion  Sort

# In[1]:


l=[4,1,3,2]
for i in range(1,len(l)):
    key=l[i]
    j=i-1
    while j>=0:
        if l[j]>key:
            l[j+1]=l[j]
            l[j]=key
        j -=1
for i in l:
    print(i)
            
    


# Recursive Insertion Sort

# In[2]:


def RecursiveInsertionSort(l,n):
    if n<=1:
        return l
    RecursiveInsertionSort(l,n-1)
    key=l[n-1]
    j=n-2
    while (l[j]>key and j>=0):
        l[j+1]=l[j]
        j -=1
    l[j+1]=key
l=[4,2,1,0]
RecursiveInsertionSort(l,len(l))
print(l)


# In[3]:


def swap(x,y,arr):
    temp=arr[x]
    arr[x]=arr[y]
    arr[y]=temp


# In[57]:


def partition(l,h,arr):
    pivot=arr[l]
    i=l
    j=h
    while(i<j):
        while(i<len(arr) and pivot>=arr[i]):
            i +=1
        while(pivot<arr[j] and j>0):
            j -=1
        if(i<j):
            swap(i,j,arr)
    swap(l,j,arr)
    return j


# QuickSort

# In[58]:


def QuickSort(l,h,arr):
    if(l<h):
        j=partition(l,h,arr)
        print(j)
        QuickSort(l,j-1,arr)
        QuickSort(j+1,h,arr)


# In[59]:


arr=[100,2,0,9]
h=len(arr)
QuickSort(0,len(arr)-1,arr)


# In[60]:


print(arr)


# Selection Sort
# -------Algorithm the minimum value and put it at the start 
# ----Two for loops are involved, 
# ----Time complexity is O(n^2)
# --Space Complexitt is O(1)

# In[72]:


def SelectionSort(arr):
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if(arr[i]>arr[j]):
                swap(i,j,arr)

        


# In[73]:


arr=[1,7,2,6]
SelectionSort(arr)


# In[74]:


print(arr)


# Bubble Sort -----It is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.--Its time complexity is O(n^2)

# In[95]:


def BubbleSort(arr):
    for i in range(len(arr)):
        count=0
        j=1
        k=0
        while(j<len(arr)):
            if arr[k]>arr[j]:
                swap(k,j,arr)
                count +=1
            k +=1
            j +=1
            
        if(count==0):
            break


# In[96]:


arr=[100,0,9,30,5]
BubbleSort(arr)


# In[97]:


print(arr)


# Merge Sort 
# It is divide and conquer rule
# Time Complexity is O(n log(n))

# In[1]:


def mergeSort(arr):
    if len(arr) > 1:
  
         # Finding the mid of the array
        mid = len(arr)//2
  
        # Dividing the array elements
        L = arr[:mid]
  
        # into 2 halves
        R = arr[mid:]
  
        # Sorting the first half
        mergeSort(L)
  
        # Sorting the second half
        mergeSort(R)
  
        i = j = k = 0
  
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
  
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
  
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
  
# Code to print the list
  
  
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
  
  
# Driver Code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)


# In[2]:


def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2
 
    # See if left child of root exists and is
    # greater than root
    if l < n and arr[largest] < arr[l]:
        largest = l
 
    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r
 
    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
 
        # Heapify the root.
        heapify(arr, n, largest)
 
# The main function to sort an array of given size
 
 
def heapSort(arr):
    n = len(arr)
 
    # Build a maxheap.
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
 
    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)
 
 
# Driver code
arr = [12, 11, 13, 5, 6, 7]
heapSort(arr)
n = len(arr)
print("Sorted array is")
for i in range(n):
    print("%d" % arr[i],end=" ")
# This code is contributed by Mohit Kumra


# In[ ]:




