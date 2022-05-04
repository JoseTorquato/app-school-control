from tracemalloc import start

from src.domain.student import Student


def propt_init():
    print()
    print("1 - Adicionar aluno \n2 - Adicionar professor \n3 - Buscar um aluno \n4 - Buscar uma classe")
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
    if confirmed.lower() == "s":
        new_student.add_studant()


map = {
    "1": add_student

}


if __name__ == "__main__":
    try:
        map[propt_init()]()
    except:
        print()
        print("Escolha inválida!")
        map[propt_init()]()

