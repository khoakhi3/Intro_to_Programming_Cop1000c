stuGrades = []
stuName = input("Enter Student Name: ")
stuGrades.append(float(input("Enter Score 1: ")))
stuGrades.append(float(input("Enter Score 2: ")))
stuGrades.append(float(input("Enter Score 3: ")))
stuGrades.append(float(input("Enter Score 4: ")))
stuGrades.append(float(input("Enter Score 5: ")))
def calAvg (avgScore):
    avgScore = sum(stuGrades) / len(stuGrades)
    return avgScore
def letterGrades (averageGrade):
    if calAvg(stuGrades) >= 90:
        return "A"
    elif calAvg(stuGrades) >= 80:
        return "B"
    elif calAvg(stuGrades) >= 70:
        return "C"
    elif calAvg(stuGrades) >= 60:
        return "D"
    else:
        return "F"
print(stuName)
print("average grade: ", calAvg(stuGrades))
print("letter grade: ", letterGrades(stuGrades))