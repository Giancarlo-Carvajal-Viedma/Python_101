from typing import Tuple, List, Dict # Different forms of using a library, this is the best
from enum import Enum
from datetime import datetime, date, time 
# from typing import * # From library import (*) all
# Tuple in case of: from above import tuple, fast vi vet inte var den kommer från
# import typing
# typing.tuple # if we only use code above
 
# De vanliga datatyperna finns också
# int, str, float, bool, None


def my_function(a: Tuple[int, str, bool], b: List[int], c: Dict[str, Dict[str, Tuple[int, int]]]):
    print(a, b)


# my_function((1, "hello", True), [1, 2, 3])


def a_new_function(a: int) -> int:
    return a * a


print(a_new_function(2))

EmployementStatus = Enum('EmployementStatus', ['unemployed', 'employed', 'let_go'])


# class EmployementStatus (Enum):
#     let_go = "let_go",
#     unemployed = "unemployed"


person: Dict[str, any] = {
    "name": "Gian",
    "employment_status": EmployementStatus.let_go,
    "born": date(1993, 5, 4)
}
list_of_employees = [person, person]


print(list_of_employees[0]["born"])