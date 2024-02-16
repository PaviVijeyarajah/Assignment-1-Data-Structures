#Assignment 1 Data Structures
#Pavishaan Vijeyarajah
#100874494

import time
import sys
import random

product_data = []

with open('product_data.txt') as file:
    lines = [i.strip() for i in file]
for i in range(len(lines)):
    product_data.append(lines[i].split(","))
file.close()

def Insertion():
    pid=input("What is the id of your product: ")
    pname=input("What is the name of your product: ")
    pprice=input("What is the price of your product: ")
    pcategory=input("What category does your product belong in: ")
    pdata=[pid," "+pname," "+pprice," "+pcategory] #spaces added because data is like that
    product_data.append(pdata)
    
def Update(pnum):
    pid=input("What is the id of your product: ")
    pname=input("What is the name of your product: ")
    pprice=input("What is the price of your product: ")
    pcategory=input("What category does your product belong in: ")
    pdata=[pid,pname,pprice,pcategory]
    product_data[pnum]=pdata
    
def Delete(pnum):
    product_data.pop(pnum)
    
def Search(psearch):
    found=0
    for i in range(len(product_data)):
        if product_data[i][0] == psearch:
            found=1
            print("Found product id:", product_data[i][0])
        if product_data[i][1] == psearch:
            found=1
            print("Found product name:", product_data[i][1])
        elif found==0 and i==len(product_data)-1:
            print("Not Found")
            
def bubbleSort(arr):
    n = len(arr)
    swapped=False
    for i in range(n):
        for j in range(0, n-i-1):
            num1=float(arr[j][2])
            num2=float(arr[j+1][2])
            if num1>num2:
                swapped=True
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
        if not swapped:
            return
        
def analyzeSortPerformance(data, description, time_complexity):
    start = time.time()
    bubbleSort(data.copy())
    end = time.time()
    space_complexity = sys.getsizeof(data) + sys.getsizeof(start) + sys.getsizeof(end) + 64
    print(f"{description} - Time taken: {end - start:.6f} seconds, Space used: {space_complexity} bytes")
    print(f"Time Complexity: {time_complexity}\n")

    
    
while True:
    print(product_data)
    request=int(input("Pick from the following operations:\n1. Insert\n2. Update\n3. Delete\n4. Search\n5. Stop\n "))
    if request==1:
        Insertion()
    if request==2:
        uchoice=int(input("Which one of the would you like to edit: "))
        Update(uchoice-1)
    if request==3:
        dchoice=int(input("Which one of the would you like to delete: "))
        Delete(dchoice-1)
    if request==4:
        #Seperated because data for id has no space but data for name has space before it
        pick=input("Do you want to find an id or name: ")
        if pick=="id":
            ichoice=input("Search an id to find: ")
            Search(ichoice)
        if pick=="name":
            nchoice=input("Search an name to find: ")
            Search(" "+nchoice)
    if request==5:
        break
while True:
    sort=int(input("Pick a method of sorting:\n1. Original\n2. Best\n3. Average\n4.Worst \n5. Stop\n "))
    if sort==1:
        analyzeSortPerformance(product_data, "Original Data", "O(n^2)")
    if sort==2:
        best=product_data.copy()
        bubbleSort(best)
        analyzeSortPerformance(best, "Best Case", "O(n^2)")
    if sort==3:
        average=product_data.copy()
        random.shuffle(average)
        analyzeSortPerformance(average, "Average Case", "O(n^2)")
    if sort==4:
        worst= best[::-1] 
        analyzeSortPerformance(worst, "Worst Case", "O(n^2)")
    if sort==5:
        break