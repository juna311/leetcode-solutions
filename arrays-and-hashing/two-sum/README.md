Two Sum

Difficulty: Easy
Category: Arrays & Hashing
Pattern: Complement lookup

Problem summary

Find two different elements whose values add up to the target and return their indices.

Key insight

* For each number, calculate the value needed to reach the target: needed value = target - current value.
* A hash map lets us check whether that needed value has already appeared.

Approach

1. Create a map from numbers to their indices.
2. Go through the array once.
3. For each number, calculate its complement.
4. Check whether the complement is already in the map.
5. If it is, return the two indices.
6. Otherwise, store the current number and its index.

Complexity

Time: O(n)
Space: O(n)

Edge cases

* Duplicate values, such as [3, 3]
* Negative numbers
* Zero
* The same array position cannot be used twice

Common mistakes

* Adding the current number before checking its complement and accidentally using the same element twice
* Returning values instead of indices
* Forgetting that duplicate numbers can have different indices

What I learned

When searching for a pair with a target relationship, store previously seen values and look for the missing complement.