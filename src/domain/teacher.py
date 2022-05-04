from src.db.database import DataBase


class Teacher:
    def __init__(self):
        self.data = {}
        self.db = DataBase()
        
    def create_teacher(self, name_teacher, age_teacher, number_class_room):
        self.data["name_teacher"] = name_teacher 
        self.data["age_teacher"] = age_teacher 
        self.data["number_class_room"] = number_class_room

    def confirm_data(self):
        print(f'Por favor confira se todos os dados abaixo estão corretos: ')
        print(f'Nome completo: {self.data["name_teacher"]}')
        print(f'Idade: {self.data["age_teacher"]}')
        print(f'Turma que será responsável: {self.data["number_class_room"]}')

    def add_teacher_db(self):
        self.db.add_row("school", "teachers", self.data)

    def get_teacher(self, name_teacher):
        print(f"Buscar o teacher {name_teacher}")
