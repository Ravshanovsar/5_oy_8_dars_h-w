import psycopg2

db_params = {
    'database': 'oy_5_dars_8_homework',
    'user': 'postgres',
    'password': 'google_0330',
    'host': 'localhost',
    'port': 5432}



class DBConnect:
    def __init__(self, db_params):
        self.db_params = db_params

    def __enter__(self):
        self.conn = psycopg2.connect(**db_params)

        self.cur = self.conn.cursor()
        return self.conn, self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.close()

        if self.cur:
            self.cur.close()



# -- Create Table

# with DBConnect(db_params) as (conn, cur):
#     create_table_book_query = """create table books(
#     id bigserial primary key,
#     title varchar(150) not null unique,
#     description varchar(150) not null unique,
#     author varchar(50) not null,
#     created_at varchar(50) default current_date);"""
#     cur.execute(create_table_book_query)
#     conn.commit()






# -- Creat Data

# with DBConnect(db_params) as (conn, cur):
#     insert_date_query = '''insert into books(title, description, author)
#     values('Harry Potter', 'Fantastic', 'K.Ruoling')'''
#     cur.execute(insert_data_query)
#     conn.commit()



# -- Read Data

# with DBConnect(db_params) as (conn, cur):
#     select_data_query = '''select * from books'''
#     cur.execute(select_data_query)
#     books_info = cur.fetchall()
#     print(books_info)
#     conn.commit()



# -- Update Data

# with DBConnect(db_params) as (conn, cur):
#     update_query = '''update book set description = 'History' where id = 1;'''
#     cur.execute(update_query)
#     conn.commit()



# -- Delete Data

# with DBConnect(db_params) as (conn, cur):
#         delete_query = f"""delete from books where id = 1"""
#         cur.execute(delete_query)
#         conn.commit()