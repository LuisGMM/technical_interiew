# Coding Task Instructions

Welcome to your coding interview task. Please clone this repository and follow
the steps below to complete the tasks.

## Tasks

1. **Bug Fixing:**
   - Open the `math.py` file.
   - There is a bug in the function `find_max_subarray_sum` that causes it to
   return incorrect results.
   - Identify and fix the bug. Ensure that the function correctly finds the
   maximum sum of a contiguous subarray.

2. **Optimization:**
   - The function `max_pair_product` in `math.py` finds the maximum
   product of any two elements in an array but is currently implemented with
   \(O(n^2)\) time complexity.
   - Optimize this function to \(O(n)\) time complexity without using extra
   space, except for a few variables.

3. **Feature Implementation:**
   - Using the classes defined in `marketplace.py`, implement the ability
   for users to add reviews to products.
   - Specifically, extend the `User` class with a method
   `add_review_to_product(product_id, score, comment)` that:
     - Retrieves the product from the `InventoryManager` using `product_id`.
     - Creates a review using the `score` and `comment`.
     - Adds this review to the respective product.
   - Ensure that after adding a review, the average score of the product is
   updated accurately.

## Submission

   - Commit your changes and create a pull request to the main branch of this
   repository. Provide a brief explanation of your changes in the commit message.

Good luck!
