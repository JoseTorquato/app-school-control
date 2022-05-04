class Teacher:
    def __init__(self, name_teacher, number_class_room):
        self.name_teacher = name_teacher 
        self.number_class_room = number_class_room

    def get_teacher(self, name_teacher):
        print(f"Buscar o teacher {name_teacher}")
