import sqlite3


class DataBase:
    def create_db(self, name_db):
        conn = sqlite3.connect(f'{name_db}.db')

        print('DB criada com sucesso.')

        conn.close()

    def create_table(self, name_db, table, schema):
        conn = sqlite3.connect(f'/Users/torquato/Documents/Pessoal/app-school-control/{name_db}.db')

        cursor = conn.cursor()

        cursor.execute(f"""
            CREATE TABLE {table} (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            id_teacher INTEGER NOT NULL,
            name_teacher TEXT,
            number_class_room INTEGER NOT NULL
            );
        """
        )

        print('Tabela criada com sucesso.')

        conn.close

    def add_row(self, name_db, table, data):
        print(name_db, table, data)
        conn = sqlite3.connect(f'/Users/torquato/Documents/Pessoal/app-school-control/{name_db}.db')

        cursor = conn.cursor()

        columns = tuple(data.keys())
        values = tuple(data.values())

        cursor.execute(f"INSERT INTO {table} {columns} VALUES {values};")

        conn.commit()
        print('Dados inseridos com sucesso.')

        conn.close()

    def read_table(self, name_db, table):
        conn = sqlite3.connect(f'/Users/torquato/Documents/Pessoal/app-school-control/{name_db}.db')

        cursor = conn.cursor()

        cursor.execute(f"SELECT * FROM {table};")

        for row in cursor.fetchall():
            print(row)

        conn.close()

    def get_student_db(self, name_student):
        conn = sqlite3.connect(f'/Users/torquato/Documents/Pessoal/app-school-control/school.db')

        cursor = conn.cursor()
        query = f"SELECT * FROM students WHERE name_student LIKE ?"
        cursor.execute(query, (f'%{name_student}%',))
        records = cursor.fetchall()
        if records:
            if len(records) > 1:
                students = [row[1] for row in records]
                print()
                print(f'Alunos: {", ".join(map(str, students))} \n\nPor favor selecione um dos alunos acima digitando o seu nome completo')
                conn.close()
                return True
            else:
                print()
                print(f'Matricula: {records[0][0]}')
                print(f'Nome completo: {records[0][1]}')
                print(f'Idade: {records[0][2]}')
                print(f'Turma: {records[0][3]}')
                print(f'Nome Pai: {records[0][4]}')
                print(f'Nome Mãe: {records[0][5]}')

                conn.close()
                return False
        else:
            print(f"Não existe aluno: {name_student}")
            conn.close()
            return True

    def get_teacher_db(self, name_teacher):
        conn = sqlite3.connect(f'/Users/torquato/Documents/Pessoal/app-school-control/school.db')

        cursor = conn.cursor()
        query = f"SELECT * FROM teachers WHERE name_teacher LIKE ?"
        cursor.execute(query, (f'%{name_teacher}%',))
        records = cursor.fetchall()
        if records:
            if len(records) > 1:
                teachers = [row[1] for row in records]
                print()
                print(f'Professores: {", ".join(map(str, teachers))} \n\nPor favor selecione um dos professores acima digitando o seu nome completo')
                conn.close()
                return True
            else:
                print()
                print(f'Matricula: {records[0][0]}')
                print(f'Nome completo: {records[0][1]}')
                print(f'Idade: {records[0][2]}')
                print(f'Turma: {records[0][3]}')

                conn.close()
                return False

    def get_name_teacher_db(self, id_teacher):
        conn = sqlite3.connect(f'/Users/torquato/Documents/Pessoal/app-school-control/school.db')

        cursor = conn.cursor()
       
        query = f"SELECT name_teacher FROM teachers WHERE id = ?"
        cursor.execute(query, (id_teacher,))
        records = cursor.fetchall()
        if records:
            conn.close()
            return records[0][0]            
        else:
            print(f"Não existe matricula: {id_teacher}")
            conn.close()

    def get_teacher_avaliable_db(self):
        conn = sqlite3.connect(f'/Users/torquato/Documents/Pessoal/app-school-control/school.db')

        cursor = conn.cursor()
        query = f"SELECT * FROM teachers AS T1 WHERE T1.id NOT IN (SELECT id_teacher FROM class AS T2 WHERE T1.id = T2.id_teacher)"
        cursor.execute(query)
        records = cursor.fetchall()
        if records:
            for id, name, age, number_class in records:
                print()
                print(f'Matricula: {id}')
                print(f'Nome completo: {name}')
                print(f'Idade: {age}')
                print(f'Turma: {number_class}')
                print(f'Dispponivel: {"Não" if number_class != "" else "Sim"}')
                print(30*"-")

            conn.close()
            return False
        else:
            print(f"Não existe professores")
            conn.close()
            return True


    def get_class_db(self, number_class_room):
        conn = sqlite3.connect(f'/Users/torquato/Documents/Pessoal/app-school-control/school.db')

        cursor = conn.cursor()

        cursor.execute(f"SELECT T1.number_class_room, T1.name_teacher, T2.name_student FROM class AS T1 INNER JOIN students AS T2 ON T1.number_class_room = T2.number_class_room WHERE T1.number_class_room = {number_class_room};")
        records = cursor.fetchall()
        if records:
            students = [row[2] for row in records]
            print(f'Turma: {records[0][0]} \nProf: {records[0][1]} \nAlunos: {", ".join(map(str, students))}')
            conn.close()
            return False
        else:
            print(f"Não existe a turma {number_class_room}")
            conn.close()
            return True


    def validate_class_db(self, number_class_room):
        conn = sqlite3.connect(f'/Users/torquato/Documents/Pessoal/app-school-control/school.db')

        cursor = conn.cursor()

        query = "SELECT * FROM class WHERE id = ?;"
        cursor.execute(query, (number_class_room,))

        records = cursor.fetchall()

        if records:
            return True
        else:
            print(f"Não existe a turma {number_class_room}")
            conn.close()
            
            return False

# (
# id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
# name_student TEXT NOT NULL,
# age_student INTEGER,
# number_class_room INTEGER NOT NULL,
# name_father TEXT,
# name_mother TEXT
# );
# # (
# id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
# name_teacher TEXT NOT NULL,
# age_teacher INTEGER,
# number_class_room INTEGER NOT NULL,
# );
# db = DataBase()
# db.create_table('school', 'class', 'ok')
