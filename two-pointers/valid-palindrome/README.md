Valid Palindrome

Difficulty: Easy
Category: Two Pointers
Pattern: Left and right pointers

Problem summary

Check whether a string reads the same forward and backward after ignoring punctuation, spaces and letter case.

Key insight

Only the meaningful alphanumeric characters need to be compared. Two pointers can move inward from opposite ends.

Approach

1. Place one pointer at the beginning and another at the end.
2. Move the left pointer forward while it points to a non-alphanumeric character.
3. Move the right pointer backward for the same reason.
4. Compare the two meaningful characters without considering case.
5. If they differ, return false.
6. Continue until the pointers meet or cross.

Complexity

Time: O(n)
Space: O(1)

Edge cases

* Empty string
* String containing only punctuation
* One character
* Mixed uppercase and lowercase letters
* Spaces between characters

Common mistakes

* Comparing punctuation and spaces
* Forgetting case normalization
* Moving only one pointer after a successful comparison
* Accessing characters after a pointer has gone out of range

What I learned

Two pointers are useful when comparing elements from opposite ends of a sequence.