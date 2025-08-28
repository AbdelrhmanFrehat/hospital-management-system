from datetime import date

from src.Data.data_manager import DataManger
from src.Patients.patient_service import PatientService
from src.Users.users import User


def main():
    data_manager = DataManger("patient.json", "id")
    patient_service = PatientService(data_manager)


    pid = "5"
    name = "Mohammed Frehat"
    age = 15
    gender = "male"
    id_card = "123123"
    date_of_birth = date.today().isoformat()  # مثال: "2025-08-28"

    user = User(1,"Abdelrhman", "Frehat", 21, "Ramallah")

    patient_service.add(pid, name, age, gender, id_card, date_of_birth,user)

    patients = patient_service.get_all()
    print(patients)
    name = input("enter the name: ")

    matches=[patient for patient in patients if name.lower() in patient.get('name').lower() ]
    print(matches)
if __name__ == "__main__":
    main()
