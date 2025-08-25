from Patients.patient import Patient
from Users.users import User

user = User('Abdelrhman', 'Frehat', '21', 'Ramallah T7ta')

user.create_patient(name='Hamza Sayes', age=18, gender='M', date_of_birth='1990-12-31', id_card='123456')

x=[{"name":'abd','age':15 },{"name":'hamza',"age":12}]

print(x[1]['name'])
students = [
    {"id": 1, "name": "Ali"},
    {"id": 2, "name": "Omar"},
    {"id": 3, "name": "Sara"},
]

result = list(filter(lambda s: "" in s["name"].lower(), students))
print(result)

teachers = ['ali','omar']

result2= list (filter( lambda s:"omar"== s, teachers))
print(result2)
