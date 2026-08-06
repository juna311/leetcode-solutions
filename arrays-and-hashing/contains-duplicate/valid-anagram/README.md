Valid Anagram

Difficulty: Easy
Category: Arrays & Hashing
Pattern: Frequency counting

Problem summary

Determine whether two strings contain exactly the same characters with exactly the same frequencies.

Key insight

The order of the characters does not matter, but the number of occurrences of every character does.

Approach

1. First compare the string lengths.
2. Count how many times every character occurs in the first string.
3. Decrease those counts using the second string.
4. If a character is missing or its count becomes invalid, the strings are not anagrams.
5. Otherwise, they are anagrams.

Sorting both strings is another possible approach, but frequency counting can be more efficient.

Complexity

For frequency counting:
Time: O(n)
Space: O(1) when the input contains only a fixed alphabet, such as 26 lowercase letters
Space: O(n) when the character set is unrestricted

For sorting:

Time: O(n log n)
Space: Depends on the sorting implementation

Edge cases

* Strings of different lengths
* Empty strings
* Repeated characters
* Strings that contain the same characters but different frequencies

Common mistakes

* Checking only whether characters exist without comparing their counts
* Forgetting to compare string lengths
* Assuming every input uses only lowercase English letters when it may not

What I learned

When order is irrelevant but frequency matters, use a frequency map.