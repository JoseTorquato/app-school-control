from src.db.database import DataBase
from src.domain.student import Student
from src.domain.teacher import Teacher


def propt_init():
    print()
    print("1 - Adicionar aluno \n2 - Adicionar professor \n3 - Buscar um aluno \n4 - Buscar uma classe \n5 - Sair")
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
    new_student.confirm_data()
    confirmed = input("Digite S para salvar os dados ou pressione qualquer tecla para cancelar: ")
    print()
    if confirmed.lower() == "s":
        return new_student.add_studant()

    propt_init()


def add_teacher():    
    print()
    name_teacher = input("Nome completo:  ")
    age_teacher = input("Idade:  ")
    number_class_room = input("Turma que será responsável:  ")
    new_teacher = Teacher()
    new_teacher.create_teacher(name_teacher, age_teacher, number_class_room)
    print()
    new_teacher.confirm_data()
    confirmed = input("Digite S para salvar os dados ou pressione qualquer tecla para cancelar: ")
    print()
    if confirmed.lower() == "s":
        return new_teacher.add_teacher_db()

    propt_init()

def get_class():
    db = DataBase()

    number_class_room = input("Qual o número da turma:  ")
    print()
    db.get_class_db('school', 'teachers', 'students', number_class_room)

map = {
    "1": add_student,
    "2": add_teacher,
    "3": get_class
}


if __name__ == "__main__":
    # try:
    map[propt_init()]()
    # except:
    #     print()
    #     print("Escolha inválida!")
    #     map[propt_init()]()

