from collections import Counter

numbers = [2, 4, 2, 6]
print(all([i%2==0 for i in numbers]))

print(all([True, True, True]))  # Output: True
print(all([True, False, True]))  # Output: False
print(all([]))  # Output: True (Empty iterable)


def are_anagrams(*words):
    print(words[1])
    # return "Yes" if all(Counter[words[0]]==Counter[word] for word in words[1:])
    print("---",all(Counter(words[0])==Counter(word) for word in words))



print(are_anagrams("bbac", "abcb", "aabb"))
