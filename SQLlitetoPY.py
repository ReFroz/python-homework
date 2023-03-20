import sqlite3
con=sqlite3.connect("tut.db")
cur=con.cursor()
#Создание таблицы
cur.execute("CREATE TABLE name(year,week,hour)")
#Заполение таблицы
cur.execute("""
    INSERT INTO name VALUES
    (1,2,3),
    (2,3,4),
    (19,20,44)
""")
#Сохранение изменений
con.commit()
#Выбор объектов
res=cur.execute("SELECT year,week,hour FROM name")
#Вывод объектов 

print("Вывод до удаления")
for year,week,hour in cur.execute("SELECT year,week,hour FROM name"):
    print(f"{year} {week} {hour}")
cur.execute("DELETE FROM name")
con.commit()
print("Все данные были удалены")
print("Новое заполение данных")
cur.execute("""
    INSERT INTO name VALUES
    (13,23,33),
    (1232,33,34),
    (19123,13220,344)
""")
print("Вывод с новыми данными")
for year,week,hour in cur.execute("SELECT year,week,hour FROM name"):
    print(f"{year} {week} {hour}")

