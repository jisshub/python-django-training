count = 0


def count_vowel(name):
    global count
    for each in name:
        for j in each:
            if j == 'a' or j == 'e' or j == 'i' or j == 'o' or j == 'u' in each:
                count += 1
    return count


count = count_vowel({'jissmoeen', 'akhil'})
print(count)


