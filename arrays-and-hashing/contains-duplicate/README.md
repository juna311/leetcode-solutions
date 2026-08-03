Contains Duplicate

Difficulty: Easy
Category: Arrays & Hashing
Pattern: Set membership

Problem summary

Determine whether any value appears more than once in the array.

Key insight

A set stores unique values and supports fast membership checks.

Approach

1. Create an empty set.
2. Examine each number.
3. If the number is already in the set, a duplicate exists.
4. Otherwise, add it to the set.
5. If the loop finishes, all values were unique.

Another valid approach is to compare the length of the array with the length of a set created from it.

Complexity

Time: O(n)
Space: O(n)

Edge cases

* Empty array
* One-element array
* Multiple copies of the same value
* Negative numbers and zero

Common mistakes

* Using nested loops, which gives O(n²)
* Sorting without considering that sorting changes the array and usually costs O(n log n)

What I learned

A set is often the first tool to consider when the question asks whether something has appeared before.