import random
import time

import cx_Oracle


def drop_table(db, cursor):
    cursor.execute("DROP TABLE biblioteca")
    db.commit();
    print("Tabela biblioteca a fost stearsa")


def create_table(db, cursor):
    try:
        cursor.execute("CREATE TABLE biblioteca (id_student INTEGER, nume_autor VARCHAR2(20), prenume_autor VARCHAR2(20), " +
                       "titlu_carte VARCHAR(50), volum INTEGER)")
        print("Tabela biblioteca a fost creata cu succes")
        db.commit()
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        print('Error.code =', error.code)
        print('Error.message =', error.message)
        print('Error.offset =', error.offset)
        db.rollback()


def add_in_table(db, cursor):
    authors_first_name = ["Ion", "Lucian-Liviu", "Gheorghe", "Vlad", "Cristian", "Francisca", "Radu", "Ernest",
                          "George-Valentin", "Angela", "Lucian", "Titu", "Liviu", "Mircea", "Traian", "Alexandru ","Constantin",
                          "Dumitru", "Ioana", "Iuliana", "Mirela", "Constantin", "Andries", "Ana-Maria", "Diana"]
    authors_last_name = ["Agarbiceanu", "Albu", "Alexandrescu", "Alexandrescu", "Balan", "Baltaceanu", "Barbuta",
                         "Beligan", "Bernea", "Bibescu", "Bidu-Vranceanu", "Blaga", "Maiorescu", "Malița",
                         "Manolescu", "Dogaru", "Dorz", "Dragomir", "Dram", "Draghicescu", "Lupu", "Maiorescu",
                         "Dumimtru", "Garleanu", "Iordache", "Guga", "Holban", "Nicolescu", "Chivu", "Furca"]
    books_title = ["Invataturile lui Neagoe Basarab", "Viata lumii", "Divanul", "Dihaniile", "O sama de cuvinte",
                   "Povestea vorbii", "Viata la tara", "Morometii", "Cuvinte potrivite", "Ion", "Iona", "Rascoala",
                   "Padurea spanzuratilor", "Ultima noapte de dragoste, Intaia noapte de razboi", "Fram, ursul polar",
                   " Concert din muzica de Bach", "Craii de Curtea Veche", "Remember", "Sub pecetea tainei",
                   "Huliganii", "Maitreyi", "Nunta in cer", "Nuvele fantastice", "Romanul adolescentului miop",
                   "La Medeleni", "Caietele", "Jurnal", "Jurnalul fericirii"]
    cursor.execute("SELECT COUNT(*) FROM STUDENTI")
    row, = cursor.fetchone()
    for student in range(row):
        books = random.randint(0, 4)
        if books == 0:
            cursor.execute("INSERT INTO biblioteca(id_student) VALUES ({})".format(student))
        else:
            for book in range(books):
                author_first_name = random.sample(authors_first_name, 1)
                author_last_name = random.sample(authors_last_name, 1)
                book_title = random.sample(books_title, 1)
                volum = random.randint(1, 6)
                print(student, author_last_name, author_first_name, book_title, volum)
                command = "INSERT INTO biblioteca(id_student,nume_autor,prenume_autor,titlu_carte,volum) VALUES (" + str(student) + "," + author_last_name[0] + "," + author_first_name[0] + "," + book_title[0] + "," + str(volum) + ");"
                print(command)
                cursor.execute(command)
    db.commit()


def select_from_table(cursor):
    cursor.execute("select * from biblioteca")
    print(cursor.fetchall())


def main():
    dsn = cx_Oracle.makedsn(host="localhost", port=32769)
    connection = cx_Oracle.connect(user="system", password="oracle", dsn=dsn)
    cur = connection.cursor()
    drop_table(connection, cur)
    print("test1")
    create_table(connection, cur)
    print("test2")
    add_in_table(connection, cur)
    print("test13")
    select_from_table(cur)
    connection.close()


if __name__ == '__main__':
    main()
