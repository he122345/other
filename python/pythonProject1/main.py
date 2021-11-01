import pymysql

host = 'localhost'
port = 3306
db = 'salary'
user = 'root'
password = 'root'


def get_connection():
    conn = pymysql.connect(host=host, port=port, db=db, user=user, password=password)
    return conn


def check_it():
    conn = get_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("select * from type")
    data = cursor.fetchall()
    for i in range(len(data)):
        for key in data[i]:
            if type(data[i][key]) is bytes:
                data[i][key] = data[i][key].decode('utf-8')
    print(data)
    cursor.close()
    cursor.close()


def type_insert(id, name):
    conn = get_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    sql = "insert into message (id,name) values('%s','%s')"
    try:
        cursor.execute(sql % (id, name))
        conn.commit()
    except:
        conn.rollback()

    cursor.close()
    cursor.close()


if __name__ == '__main__':
    type_insert(13, "张七")
