'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    i1 = 0
    i2 = 1
    while i1 < len(arr) - 1:
        while i2 < len(arr):
            if arr[i1] == arr[i2]:
                dupe1 = arr[i1]
                arr.remove(dupe1)
                arr.remove(dupe1)
                i1 = 0
                i2 = 1
            else:
                i2 += 1
        return arr[0]

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")