def report_header(func):
    def nomnom(*args, **kwargs):
        print("=" * 40)
        print(" STUDENT REPORT")
        print("=" * 40)
        result = func(*args, **kwargs)
        print("=" * 40)
        return result

    return nomnom


class Report:
    college = "ABC Engineering College"

    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    @classmethod
    def change_college(cls, new_name):
        cls.college = new_name

    def __str__(self):
        return f"Name : {self.name}\nRoll No : {self.roll}\nMarks : {self.marks}"

    @report_header
    def display_report(self):
        print(f"College : {Report.college}")
        print(self)
        if self.marks >= 40:
            print("Result : PASS")
        else:
            print("Result : FAIL")


student1 = Report("Rahul", 101, 85)
student1.display_report()

print()

Report.change_college("XYZ Institute of Technology")

student2 = Report("Priya", 102, 35)
student2.display_report()
