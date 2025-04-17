import os
import matplotlib.pyplot as plt

class Assignment:
    def __init__(self, name, assignment_id, points):
        self.name = name
        self.assignment_id = (assignment_id)
        self.points = int(points)

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = (student_id)

class Submission:
    def __init__(self, student_id, assignment_id, scorePercent):
        self.student_id = (student_id)
        self.assignment_id = (assignment_id)
        self.scorePercent = int(scorePercent)

def get_students():
    students = {}
    with open("data/students.txt") as f:
        for line in f:
            students[line[3:].strip()] = Student(line[3:].strip(), line[:3])
    return students



def get_assignments():
    assignments = {}
    with open("data/assignments.txt") as f:
        lines = f.readlines()
        for i in range(0, len(lines), 3):
            name = lines[i].strip()
            assignment_id = lines[i+1].strip()
            pts = lines[i+2].strip()
            assignments[name] = Assignment(name, assignment_id, pts)
    return assignments

def get_submissions():
    submissions = []
    for filename in os.listdir("data/submissions"):
        with open(f"data/submissions/{filename}") as f:
            student_id, assignment_id, pts = f.read().split("|")
            submissions.append(Submission(student_id, assignment_id, pts))
    return submissions

def main():
    students = get_students()
    assignments = get_assignments()
    submissions = get_submissions()

    menu = "1. Student grade\n2. Assignment statistics\n3. Assignment graph\n"

    print(menu)
    selection = int(input("Enter your selection: "))

    if selection == 1:
        name = input("What is the student's name: ")
        if name in students:
            student = students[name]
            total_earned = 0
            for s in submissions:
                if s.student_id == student.student_id:
                    for a in assignments.values():
                        if a.assignment_id == s.assignment_id:
                            total_earned += (s.scorePercent / 100) * a.points
            print(f"{round(total_earned / 1000 * 100)}%")
        else:
            print("Student not found")

    elif selection == 2:
        assmt = input("What is the assignment name: ")
        if assmt in assignments:
            assignment_id = assignments[assmt].assignment_id
            scores = [submission.scorePercent for submission in submissions if submission.assignment_id == assignment_id]
            print(f"Min: {min(scores)}%")
            print(f"Avg: {sum(scores) // len(scores)}%")
            print(f"Max: {max(scores)}%")
        else:
            print("Assignment not found")


    elif selection == 3:
        assmt = input("What is the assignment name: ")
        if assmt in assignments:
            assignmentid = assignments[assmt].assignment_id
            scores = [s.scorePercent for s in submissions if s.assignment_id == assignmentid]
            print(scores)
            plt.hist(scores, bins = list(range(0, 101, 10)))
            plt.show()
        else:
            print("Assignment not found")


if __name__ == "__main__":
    main()
