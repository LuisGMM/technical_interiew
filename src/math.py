import random


class ArrayManipulator:
    """Class for manipulating arrays."""

    @staticmethod
    def reverse_array(arr: list) -> list:
        """Reverse the given array."""

        return arr[::-1]

    @staticmethod
    def shuffle_array(arr: list) -> list:
        """Shuffle the given array randomly."""
        random.shuffle(arr)

        return arr


def find_max_subarray_sum(nums: list[int]) -> int:
    """Find the maximum sum of a contiguous subarray."""
    max_sum = 0
    current_sum = 0

    for num in nums:
        current_sum += num

        if current_sum > max_sum:
            max_sum = current_sum

        if current_sum < 0:
            current_sum = -1

    return max_sum


def max_pair_product(nums: list[int]) -> int:
    """Find the maximum product of any two elements in the array."""
    max_product = 0

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            product = nums[i] * nums[j]

            if product > max_product:
                max_product = product

    return max_product


class MathOperations:
    """Class for performing basic math operations."""

    @staticmethod
    def factorial(n: int) -> int:
        """Calculate the factorial of a number."""

        if n == 0:
            return 1
        else:
            return n * MathOperations.factorial(n - 1)

    @staticmethod
    def fibonacci(n: int) -> int:
        """Generate the nth Fibonacci number."""
        a, b = 0, 1

        for _ in range(n):
            a, b = b, a + b

        return a
