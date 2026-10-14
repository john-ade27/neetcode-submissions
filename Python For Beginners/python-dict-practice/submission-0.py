from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    dict2 = {}
    for i in word:
        if i in dict2:
            dict2[i] += 1
        else:
            dict2[i] = 1
    return dict2



# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
