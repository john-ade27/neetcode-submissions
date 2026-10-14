from typing import List

def read_integers() -> List[int]:
    numbers = input()
    numbers_list = numbers.split(",")
    num = []
    for n in numbers_list:
        num.append(int(n))
    return num

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
