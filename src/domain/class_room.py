from src.db.database import DataBase


class ClassRoom:
    def __init__(self, ):
        self.data = {}
        self.db = DataBase()

    def create_class(self, number_class_room, id_teacher):
        self.data["id_teacher"] = id_teacher 
        self.data["number_class_room"] = number_class_room
        self.data["id"] = number_class_room

    def confirm_data(self):
        self.data["name_teacher"] = self.db.get_name_teacher_db(self.data["id_teacher"])
        print(f'Por favor confira se todos os dados abaixo estão corretos: ')
        print(f'Número da nova turma: {self.data["number_class_room"]}')
        print(f'Responsável pela turma: {self.data["name_teacher"]}')
        
    def add_teacher_db(self):
        self.db.add_row("school", "class", self.data)    
