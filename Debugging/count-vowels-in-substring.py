def vowelStrings(word, queries):
    # Part 1: Build the prefix array of counts
    n = len(word)
    prefix = [0] * (n + 1)
    for i in range(1, n + 1):
        is_vowel = word[i - 1].lower() in 'aeiou'
        prefix[i] = prefix[i-1] + (1 if is_vowel else 0)
        

    # Part 2: Calculate the number of vowels for each subarray
    results = []
    for q in queries:
        l = q[0]
        r = q[1]
        results.append(prefix[r + 1] - prefix[l])
    return results



word = "prefixsum"
queries = [[0, 2], [1, 4], [3, 5]]
results = vowelStrings(word, queries)
print(results)