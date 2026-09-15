# LeetCode Solutions

My accepted Python solutions to LeetCode problems.

**24 problems · 26 accepted submissions · Python 3**

## Solutions

| Problem | Solution | Last accepted (Japan time) |
| --- | --- | --- |
| [3Sum](https://leetcode.com/problems/3sum/) | [Python](solutions/3sum/solution.py) | 2026-08-04 |
| [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | [Python](solutions/best-time-to-buy-and-sell-stock/solution.py) | 2026-07-19 |
| [Binary Search](https://leetcode.com/problems/binary-search/) | [Python](solutions/binary-search/solution.py) | 2026-07-23 |
| [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) | [Python](solutions/binary-tree-level-order-traversal/solution.py) | 2026-09-04 |
| [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | [Python](solutions/container-with-most-water/solution.py) | 2026-08-05 |
| [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | [Python](solutions/contains-duplicate/solution.py) | 2026-07-11 |
| [Group Anagrams](https://leetcode.com/problems/group-anagrams/) | [Python](solutions/group-anagrams/solution.py) | 2026-07-26 |
| [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) | [Python](solutions/koko-eating-bananas/solution.py) | 2026-08-27 |
| [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) | [Python](solutions/linked-list-cycle/solution.py) | 2026-08-28 |
| [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) | [Python](solutions/longest-consecutive-sequence/solution.py) | 2026-07-31 |
| [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) | [Python](solutions/longest-repeating-character-replacement/solution.py) | 2026-08-10 |
| [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | [Python](solutions/longest-substring-without-repeating-characters/solution.py) | 2026-08-06 |
| [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | [Python](solutions/maximum-depth-of-binary-tree/solution.py) | 2026-07-24 |
| [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) | [Python](solutions/merge-two-sorted-lists/solution.py) | 2026-07-23 |
| [Min Stack](https://leetcode.com/problems/min-stack/) | [Python](solutions/min-stack/solution.py) | 2026-08-27 |
| [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) | [Python](solutions/product-of-array-except-self/solution.py) | 2026-07-27 |
| [Reorder List](https://leetcode.com/problems/reorder-list/) | [Python](solutions/reorder-list/solution.py) | 2026-08-31 |
| [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) | [Python](solutions/reverse-linked-list/solution.py) | 2026-07-24 |
| [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | [Python](solutions/top-k-frequent-elements/solution.py) | 2026-07-29 |
| [Two Sum](https://leetcode.com/problems/two-sum/) | [Python](solutions/two-sum/solution.py) | 2026-07-10 |
| [Valid Anagram](https://leetcode.com/problems/valid-anagram/) | [Python](solutions/valid-anagram/solution.py) | 2026-07-17 |
| [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | [Python](solutions/valid-palindrome/solution.py) | 2026-07-17 |
| [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | [Python](solutions/valid-parentheses/solution.py) | 2026-07-21 |
| [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) | [Python](solutions/validate-binary-search-tree/solution.py) | 2026-09-02 |

## About this history

This repository imports my original accepted submissions from LeetCode. Each submission has its own commit, with the author date set to the exact LeetCode submission timestamp and the timezone set to Japan time (UTC+09:00). The committer date records when the import happened; these commits were not pushed to GitHub on the original practice dates. Existing repository history is preserved.

Solution files contain the original submitted code, including comments and whitespace. The latest accepted version is shown in each problem folder; earlier versions remain in Git history. LeetCode supplies types such as `List`, `Optional`, `TreeNode`, and `ListNode` in its execution environment, so the files are not standalone programs.

[submissions.json](submissions.json) records submission IDs, source links, exact timestamps, and SHA-256 hashes of the original code. It contains no login credentials. Full problem statements are linked rather than copied.

## Import future submissions

The importer uses only the Python standard library and Git. It reads saved JSON files locally, requires no LeetCode token, and does not push automatically.

1. While signed into LeetCode, open `https://leetcode.com/api/submissions/?offset=0&limit=20` in your browser and save the response as JSON.
2. If the response has `has_next: true`, repeat with offsets 20, 40, and so on, saving each page separately. This undocumented website endpoint may change.
3. Run the importer from this repository, providing your saved exports:

```sh
python3 scripts/import_submissions.py /path/to/submissions*.json \
  --author-name juna311 \
  --author-email 109890582+juna311@users.noreply.github.com \
  --timezone-offset +0900
```

Only unseen accepted submission IDs create commits. Review the changes and run `git push origin main`. The importer currently supports Python 3. The solution index above describes the initial import; update it when adding new problems.
