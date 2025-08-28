from typing import Dict, Any, Optional
from src.Patients.patient import Patient


class User:
    def __init__(self,id, first_name: str, last_name: str, age: int, address: str):
        self.id=id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.address = address

    def create_patient(
        self,
        id:int,
        name: str,
        age: int,
        gender: str,
        id_card: str,
        date_of_birth: str,
        patient_id: Optional[str] = None,
    ) -> Patient:
        patient = Patient(
            id=id,
            name=name,
            age=age,
            gender=gender,
            id_card=id_card,
            date_of_birth=date_of_birth,
            user=self,
        )
        patient.print_details()
        return patient

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id":self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age,
            "address": self.address,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "User":
        return cls(
            id=data["id"],
            first_name=data["first_name"],
            last_name=data["last_name"],
            age=data["age"],
            address=data["address"],
        )
