import sqlite3


class DataBase:
    def create_db(self, name_db):
        conn = sqlite3.connect(f'{name_db}.db')

        print('DB criada com sucesso.')

        conn.close()

    def create_table(self, name_db, schema):
        conn = sqlite3.connect(f'/Users/torquato/Documents/Pessoal/app-school-control/{name_db}.db')

        cursor = conn.cursor()

        cursor.execute(schema)

        print('Tabela criada com sucesso.')

        conn.close

    def add_row(self, name_db, table, data):
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
                print(f'Nome M??e: {records[0][5]}')

                conn.close()
                return False
        else:
            print(f"N??o existe aluno: {name_student}")
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
            print(f"N??o existe matricula: {id_teacher}")
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
                print(f'Dispponivel: {"Sim" if number_class != "" else "N??o"}')
                print(30*"-")

            conn.close()
            return False
        else:
            print(f"N??o existe professores")
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
            print(f"N??o existe a turma {number_class_room} ou ela n??o possui alunos ainda.")
            conn.close()
            return True


    def get_all_class_db(self):
        conn = sqlite3.connect(f'/Users/torquato/Documents/Pessoal/app-school-control/school.db')

        cursor = conn.cursor()

        cursor.execute(f"SELECT id,  FROM class;")
        records = cursor.fetchall()
        if records:
            for id, teacher in records:
                print(f"Turma: {id[0]} \nProf: {teacher[0]}")
            conn.close()
            return False
        else:
            print(f"N??o existe nenhuma turma")
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
            print(f"N??o existe a turma {number_class_room}")
            conn.close()
            
            return False

    def migrate(self):
        schema_students = f"""
                            CREATE TABLE students (
                            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                            name_student TEXT NOT NULL,
                            age_student INTEGER,
                            number_class_room INTEGER NOT NULL,
                            name_father TEXT,
                            name_mother TEXT
                        );
                        """
        schema_teachers = f"""
                            CREATE TABLE teachers (
                            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                            name_teacher TEXT NOT NULL,
                            age_teacher INTEGER,
                            number_class_room INTEGER
                            );
                        """
        schema_class = f"""
                            CREATE TABLE class (
                            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                            id_teacher INTEGER NOT NULL,
                            name_teacher TEXT,
                            number_class_room INTEGER NOT NULL
                        );
                        """
        print("Create DB start...")
        self.create_db("school")
        print("Create DB School...")
        print()
        print("Create table students...")
        self.create_table('school', schema_students)
        print("Create table students SUCESS...")
        print()
        print("Create table teachers...")
        self.create_table('school', schema_teachers)
        print("Create table teachers SUCESS...")
        print()
        print("Create table class...")
        self.create_table('school', schema_class)
        print("Create table class SUCESS...")
        print()

