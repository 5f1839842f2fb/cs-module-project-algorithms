'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''


def sliding_window_max(nums, k):  # version 1
    # Your code here
    maxarr = [-9999] * (len(nums) - k + 1)  # this will fail if a number less than -9999 is in the input array
    for i, v in enumerate(maxarr):
        for n in range(i, i + k):
            if nums[n] > maxarr[i]:
                maxarr[i] = nums[n]
    return maxarr


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
