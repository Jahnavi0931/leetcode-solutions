# 1071. GCD of Strings

## Difficulty
Easy

## Approach

- Find the smaller string length.
- Check prefixes from largest to smallest.
- Verify whether the prefix can recreate both strings.
- Return the first valid prefix.

## Time Complexity

O(n²)

## Space Complexity

O(1)

## Concepts Learned

- String slicing
- String multiplication
- Divisibility using %
- Brute-force search
