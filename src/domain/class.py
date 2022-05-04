class Class:
    def __init__(self, number_class_room):
        self.number_class_room = number_class_room

    def add_teacher_class(self, name):
        self.teacher_name = name
        
    def add_student_class(self, name):
        self.teacher_name = name
    
    def get_class(self, number_class_room):
        print(f"Buscar os dados da sala {number_class_room}")
 