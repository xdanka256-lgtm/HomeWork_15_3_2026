
def get_average_grade(grades: dict) -> float:
    average = float(sum(grades.values()) / len(grades))
    return average
"""
second option:
def get_average_grade(grades: dict) -> float:   
    total = 0
    for value in grades.values():
        total += value
    average: float = total / len(grades)
    return average
"""
grades = {"Tom":80, "Anna":95, "John":70, "Sara":85}
print(get_average_grade(grades))