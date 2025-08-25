

class Patient:

    def __init__(self, name, age, gender,idCard,dateOfBirth,user):
        self.name = name
        self.age = age
        self.gender = gender
        self.idCard = idCard
        self.dateOfBirth = dateOfBirth
        self.user = user
    def printDetails(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("IDCard:", self.idCard)
        print("Date of Birth:", self.dateOfBirth)
        print("User:", self.user.first_name+" "+self.user.last_name)
