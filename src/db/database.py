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
            name_teacher TEXT NOT NULL,
            age_teacher INTEGER,
            number_class_room INTEGER NOT NULL
            );
        """
        )

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

        for linha in cursor.fetchall():
            print(linha)

        conn.close()

    def get_class_db(self, name_db, table_one, table_two, number_class_room):
        conn = sqlite3.connect(f'/Users/torquato/Documents/Pessoal/app-school-control/{name_db}.db')

        cursor = conn.cursor()

        cursor.execute(f"SELECT T1.number_class_room, T1.name_teacher, T2.name_student FROM {table_one} AS T1 INNER JOIN {table_two} AS T2 ON T1.number_class_room = T2.number_class_room WHERE T1.number_class_room = {number_class_room};")
        records = cursor.fetchall()
        students = []
        for linha in records:
            students.append(linha[2])

        print(f'Turma: {linha[0]} \nProf: {linha[1]} \nAlunos: {", ".join(map(str, students))}')

        conn.close()

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

