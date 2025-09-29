# Function to check if pair
# with given sum exists
def pair_sum(dict, arr, sum):
    dict.clear()
    for num in arr:
        comp=sum-num
        if comp in dict:
            return True
        dict[num]=1
    return False
    
    
    
    