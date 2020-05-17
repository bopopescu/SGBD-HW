import cx_Oracle
from pip._vendor.distlib.compat import raw_input


def get_friends(conn, id_student):
    cur = conn.cursor()
    cur.execute("select studenti.id, studenti.nume, studenti.prenume " +
                "from studenti join prieteni on prieteni.id_student1 = " + str(id_student) + " and studenti.id = prieteni.id_student1")
    if cur.fetchone() is None:
        print("There is no student with this id")
    else:
        print("Studentului: ")
        print(cur.fetchone())
        print("\nI se sugereaza prietenii: ")
        cur.execute("select S.id, S.nume, S.prenume from studenti S where id in (select id_student2 from " +
                    "(select t2.id_student2 from prieteni t1 join prieteni t2 " +
                    "on t1.id_student1=" + str(id_student) + " and t1.id_student2=t2.id_student1 " +
                    "where t2.id_student2 NOT IN " +
                    "(select id_student2 from prieteni where id_student1=" + str(id_student) + ")) where ROWNUM <= 5)")
        for result in cur:
            print(result)


def main(student):
    dsn = cx_Oracle.makedsn(host="localhost", port=32769)
    connection = cx_Oracle.connect(user="system", password="oracle", dsn=dsn)
    get_friends(connection, student)
    connection.close()


if __name__ == '__main__':
    try:
        student = int(raw_input('Id for Student:'))
        main(student)
    except ValueError:
        print("Not a number")
