import mysql.connector

# Database
db = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    password = 'BlaCK_KnigHT',
    database = 'food_list'
)

cursor = db.cursor()
sql = '''
    INSERT INTO foods (foods_name, price, is_carted)
    VALUES (%s, %s, %s);
'''

cursor.executemany(sql)
db.commit()
print('Add data ' + str(cursor.rowcount) + 'row')