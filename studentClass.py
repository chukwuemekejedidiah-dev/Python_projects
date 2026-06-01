class Student:
    def __init__ (self, name,age, scores):
        self.name = name
        self.age = age
        self.scores = scores

    @getname.setters
    def set_name(self, name):
        self.name = name

    def average_scores(self):
        average_scores = sum(self.scores) / len(self.scores)
        return average_scores

    def __str__(self):
        return f"{self.name}'s scores are {self.scores} and the average score is {self.average_scores()} "



student_one = Student("Vivian", 25, [85,90,78,92,88])
print(student_one.__str__())
