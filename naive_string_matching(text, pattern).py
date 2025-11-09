def naive_string_matching(text, pattern):
    """
    Finds all starting indices in the text where the pattern occurs,
    using the Naive String Matching Algorithm.

    Args:
        text (str): The main text string of length n.
        pattern (str): The pattern string of length m.

    Returns:
        list: A list of starting indices where the pattern is found in the text.
    """
    n = len(text)
    m = len(pattern)
    occurrences = []

    # Iterate through all possible starting positions in the text
    # The loop runs from i = 0 to n - m
    for i in range(n - m + 1):
        # Assume a match for the current window
        match = True
        # Compare the substring text[i:i+m] with the pattern
        for j in range(m):
            if text[i + j] != pattern[j]:
                match = False
                break  # Mismatch found, no need to compare further in this window
        
        # If all characters matched, add the starting index to the occurrences list
        if match:
            occurrences.append(i)

    return occurrences

# Example usage:
text1 = "ABAAABCDBAAABCDE"
pattern1 = "ABA"
print(f"Text: '{text1}', Pattern: '{pattern1}'")
print(f"Occurrences: {naive_string_matching(text1, pattern1)}")

text2 = "GEEKSFORGEEKS"
pattern2 = "GEEK"
print(f"Text: '{text2}', Pattern: '{pattern2}'")
print(f"Occurrences: {naive_string_matching(text2, pattern2)}")

text3 = "AAAAA"
pattern3 = "AA"
print(f"Text: '{text3}', Pattern: '{pattern3}'")
print(f"Occurrences: {naive_string_matching(text3, pattern3)}")

text4 = "HELLO"
pattern4 = "WORLD"
print(f"Text: '{text4}', Pattern: '{pattern4}'")
print(f"Occurrences: {naive_string_matching(text4, pattern4)}")
