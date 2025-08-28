from typing import Dict, Any



class Patient:

    def __init__(self, id, name, age, gender, id_card, date_of_birth, user):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.id_card = id_card
        self.date_of_birth = date_of_birth
        self.user = user

    def print_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("IDCard:", self.id_card)
        print("Date of Birth:", self.date_of_birth)
        print("User:", self.user.first_name + " " + self.user.last_name)

    def to_dict(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
            'id_card': self.id_card,
            'date_of_birth': self.date_of_birth,
            'user': self.user.to_dict()
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Patient':
        return cls(
            id=data['id'],
            name=data['name'],
            age=data['age'],
            gender=data['gender'],
            id_card=data['id_card'],
            date_of_birth=data['date_of_birth'],
            user=data.get("user"),
        )
