import sqlite3


connection = sqlite3.connect('games.db')  # устанавливаем соединение

curs = connection.cursor()

curs.execute('SELECT * FROM games WHERE year = 2024 or year = 2023 ORDER BY price DESC LIMIT 3')
gam = curs.fetchall()

for i in gam:
    print(f'Название: {i[0]} Жанр: {i[1]} Год: {i[2]} Возрастное ограничение: {i[3]} Цена: {i[5]}')

connection.close

















# curs = connection.cursor()                # делаем "ключ"
# name = input()
# zhanr = input()
# year = input()
# age_limit = input()


# curs.execute(f"INSERT INTO games ('name', 'zhanr', 'year', 'age_limit') VALUES ('{name}', '{zhanr}', '{year}', '{age_limit}')")    # делаем запрос

# curs.execute("SELECT * FROM games")
# print(curs.fetchall())

# connection.close()