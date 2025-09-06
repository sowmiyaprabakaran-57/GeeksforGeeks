#User function Template for python3

arr = tuple(map(int, input().split()))
x = int(input())

########### Write your code below ###############
# Print the index of x in arr

########### Write your code above ###############
for i in range(len(arr)):
    if arr[i]==x:
        print(i)
        break
