def calculateGrade(boundary: dict, mark: int) -> str:
    achieved = [grade for grade in boundary]
    for grade in boundary:
        if mark == boundary[grade]:
            return(grade)
        elif mark < boundary[grade]:
            achieved.remove(grade)
    return(achieved[0])

boundary = {"Full Marks": 100, "A": 90, "B": 80, "C": 70, "D": 50, "E": 20, "F": 0}
mark = int(input("Enter marks: "))
print(calculateGrade(boundary, mark))