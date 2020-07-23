'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    pass
    # if len(arr) == 0:
    #     return -1
    # if len(arr) == 1:
    #     return arr[0]
    # i = 0
    # while i < len(arr)-1:
    #     if arr[i] != arr[i+1]:
    #         return arr[i]
    #     i += 2
    res = arr[0] 
      
    # Do XOR of all elements and return 
    for i in range(1,len(arr)): 
        res ^= arr[i] 
      
    return res 

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")