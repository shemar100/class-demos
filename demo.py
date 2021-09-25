import psycopg2

connection = psycopg2.connect('dbname=example')

cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS table3')

cursor.execute('''
    CREATE TABLE table3(
        id INTEGER PRIMARY KEY,
        completed BOOLEAN NOT NULL DEFAULT False
    );
''')

#dictionary assigned to variable data
data = {
    'id' : 3,
    'completed' : True
}

cursor.execute('INSERT INTO table3 (id, completed) VALUES (%s, %s)', (1, True))
cursor.execute('INSERT INTO table3 (id, completed) VALUES (%s, %s)', (2, False))
#using named variable ins string composition - In this case rather than using tuple we use dictionary
cursor.execute('INSERT INTO table3 (id, completed) VALUES (%(id)s, %(completed)s)', data)


connection.commit() 

connection.close()

cursor.close() 