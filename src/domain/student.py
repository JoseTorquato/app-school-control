from src.db.database import DataBase


class Student:
    def __init__(self):
        self.data = {}
        self.db = DataBase()
        
    def create_studant(self, name_student, age_student, number_class_room, name_father, name_mother):
        self.data["name_student"] = name_student 
        self.data["age_student"] = age_student 
        self.data["number_class_room"] = number_class_room
        self.data["name_father"] = name_father
        self.data["name_mother"] = name_mother

    def confirm_data(self):
        print(f'Por favor confira se todos os dados abaixo estão corretos: ')
        print(f'Nome completo: {self.data["name_student"]}')
        print(f'Idade: {self.data["age_student"]}')
        print(f'Turma: {self.data["number_class_room"]}')
        print(f'Nome Pai: {self.data["name_father"]}')
        print(f'Nome Mãe: {self.data["name_mother"]}')

    def add_studant(self):
        self.db.add_row("school", "students", self.data)

    def get_student(self, name_student):
        print(f'Buscar o aluno {name_student}')
    