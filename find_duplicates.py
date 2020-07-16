def find_duplicates(arr):
    seen = set()
    duplicates = []
    for x in arr:
        if x in seen:
            duplicates.append(x)
        else:
            seen.add(x)
    return duplicates


if __name__ == "__main__":
	assert(find_duplicates([8, 5, 8, 4, 5, 1, 2]) == [8, 5])
	assert(find_duplicates([]) == [])