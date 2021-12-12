"""
Given a list of numbers and a number k, return whether 
any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, 
return true since 10 + 7 is 17.
"""
from timer import timer

@timer
def main(num_list: list, k: int) -> bool:
    ''' check if any two numbers in sample add up to k '''
    for idx, num in enumerate(num_list):
        if k - num in num_list[idx + 1:]:
            return True
    return False


if __name__ == "__main__":
    """ test cases """
    assert main([10, 15, 3, 7], 17) == True
    assert main([10, 15, 3, 7], 18) == True
    assert main([10, 15, 3, 7], 16) == False
    assert main([10, 15, 3, 7], 19) == False
    assert main([10, 15, 3, 7], 20) == False
    assert main([10, 15, 3, 7], 21) == False
    assert main([10, 15, 3, 7], 22) == True
    assert main([10, 15, 3, 7], 23) == False
    assert main([10, 15, 3, 7], 24) == False
    assert main([10, 15, 3, 7], 25) == True
    assert main([10, 15, 3, 7], 26) == False
