from src.db.database import DataBase
from src.domain.class_room import ClassRoom
from src.domain.student import Student
from src.domain.teacher import Teacher


def propt_init():
    print()
    print("1 - Adicionar aluno \n2 - Adicionar professor \n3 - Criar uma Turma \n4 - Buscar um aluno \n5 - Buscar um professor(a) \n6 - Buscar uma turma \n0 - Sair")
    print()
    return input("O que gostaria de fazer? ")


def add_student():    
    print()
    name_student = input("Nome completo do estudante:  ")
    age_student = input("Idade do estudante:  ")
    number_class_room = input("Turma do estudante:  ") # Validar se turma existe e se possui professora
    name_father = input("Nome do Pai:  ")
    name_mother = input("Nome da Mãe:  ")
    new_student = Student()
    new_student.create_studant(name_student, age_student, number_class_room, name_father, name_mother)
    print()
    validator = new_student.confirm_data()
    if validator:
        confirmed = input("Digite S para salvar os dados ou pressione qualquer tecla para cancelar: ")
        print()
        if confirmed.lower() == "s":
            return new_student.add_studant()
    
    propt_init()


def add_teacher():    
    print()
    print("1 - Matricular um novo professor \n2 - Adicionar professor a uma turma \n0 - Sair")
    print() 
    user_input = input("O que gostaria de fazer? ")
    if user_input == "1":
        name_teacher = input("Nome completo:  ")
        age_teacher = input("Idade:  ")
        new_teacher = Teacher()
        new_teacher.create_teacher(name_teacher, age_teacher)
        print()
        new_teacher.confirm_data()
        confirmed = input("Digite S para salvar os dados ou pressione qualquer tecla para cancelar: ")
        print()
        if confirmed.lower() == "s":
            return new_teacher.add_teacher_db()
    elif user_input == "2":
        print("Criar update, loginca onde adiciona a uma turma que já exista e adicione ao prof essa turma")

    propt_init()

    
def add_class_room():    
    db = DataBase()
    print()
    number_class_room = input("Número da nova turma:  ")
    db.get_teacher_avaliable_db()
    id_teacher = input("Selecione o professor reponsável pela matricula:  ")
    new_class = ClassRoom()
    new_class.create_class(number_class_room, id_teacher)
    print()
    new_class.confirm_data()
    confirmed = input("Digite S para salvar os dados ou pressione qualquer tecla para cancelar: ")
    print()
    if confirmed.lower() == "s":
        return new_class.add_teacher_db()

    propt_init()


def get_input(type):
    db = DataBase()
    if type == "student":
        student_search = input("Qual o nome do aluno:  ")
        return db.get_student_db(student_search)
    elif type == "teacher":
        class_search = input("Qual o nome do professor(a):  ")
        return db.get_teacher_db(class_search)
    elif type == "class":
        class_search = input("Qual o número da turma:  ")
        return db.get_class_db(class_search)
    else:
        return False
    
def get_student():
    search = True
    while search:
        search = get_input("student")


def get_teacher():
    search = True
    while search:
        search = get_input("teacher")

def get_class():
    search = True
    while search:
        search = get_input("class")
    

map = {
    "1": add_student,
    "2": add_teacher,
    "3": add_class_room,
    "4": get_student,
    "5": get_teacher,
    "6": get_class
}


if __name__ == "__main__":
    # try:
    map[propt_init()]()
    # except:
    #     print()
    #     print("Escolha inválida!")
    #     map[propt_init()]()

