class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        score = sum(self.scores) / len(self.scores)

        if 90 <= score <= 100:
            return "O"
        if 80 <= score < 90:
            return "E"
        if 70 <= score < 80:
            return "A"
        if 55 <= score < 70:
            return "P" 
        if 40 <= score < 55:
            return "D" 
        if score < 40:
            return "T"
