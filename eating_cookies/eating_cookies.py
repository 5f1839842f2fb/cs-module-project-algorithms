'''
Input: an integer
Returns: an integer
'''


def eating_cookies(n):
    # Your code here
    if n <= 0:  # don't know how you can eat 0 cookies, but the tests says that there's 1 way to eat them
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2

    return eating_cookies(n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3)


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
