
from typing import List

def check_ints(list: List[int]) -> bool:
    for i in range(len(list)):
        if not isinstance(list[i], int):
            return False
    return True
