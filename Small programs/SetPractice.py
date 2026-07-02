from typing import Any




numbers1: Any = {1, 2, 3, 4, 4, 3, 2, 7, 8, 2}
numbers2: Any = {1, 5, 6, 9, 3, 5, 2, 3, 1, 8}


result = numbers1 | numbers2
print(result)
result = numbers1 & numbers2
print(result)
result = numbers1 ^ numbers2
print(result)



