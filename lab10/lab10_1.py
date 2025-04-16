print("Файл читается успешно!")

import psycopg2

print("Импорт прошел")

dsn = "host=localhost dbname=mydatabase user=myuser password=2303 port=5432"
conn = psycopg2.connect(dsn)

print("Подключение установлено!")
