from Patients.patient import Patient


class User:
    def __init__(self, first_name, last_name, age, address):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.address = address

    def create_patient(self, name, age, gender, id_card, date_of_birth):
        patient = Patient(
            name=name,
            age=age,
            gender=gender,
            idCard=id_card,
            dateOfBirth=date_of_birth,
            user=self
        )
        patient.printDetails()
        return patient