from src.Data.idata_manager import IDataManager
from src.Patients.patient import Patient
from src.Users.users import User
from typing import  List

class PatientService:
    def __init__(self,data_manager:IDataManager):
        self.data_manager=data_manager

    def add(self,id,name:str,age,gender,id_card,date_of_birth,user:User):
        patient=Patient(id,name, age, gender, id_card, date_of_birth, user)
        self.data_manager.add(patient.to_dict())

    def get_all(self) -> list[dict]:
        return self.data_manager.get_all()


