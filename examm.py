import sqlite3
import hashlib


def connection():
    conn=sqlite3.connect('exam.dtb')
    return conn

def cource_con():
    conn=sqlite3.connect('cource.dtb')
    return conn

def subscribe():
    conn=sqlite3.connect('kurslar.dtb')
    return conn




def hash_password(text: str):
    sha256 = hashlib.sha256()
    sha256.update(text.encode('utf-8'))
    return sha256.hexdigest()


def user_register():
    conn=connection()
    cur=conn.cursor()
    cur.execute("""
        create table if not exists user_parameters(
                id integer not null primary key autoincrement,
                first_name varchar(30),
                last_name varchar(30),
                birthday date,
                phone varchar(13),
                username varchar(50),
                password varchar(150),
                is_admin boolean default false
                
        )
""")

    conn.commit()
    conn.close() 


def insert_users(data:dict):
    conn = connection()
    cur = conn.cursor()
    hashed_password = hash_password(data['password1'])
    data['password1'] = hashed_password
    query="""
        insert into user_parameters(
            first_name,
            last_name,
            birthday,
            phone,
            username,
            password
    ) values(?,?,?,?,?,?)
    """
    values = tuple(data.values())
    cur.execute(query,values)
    conn.commit()
    conn.close()



def get_id(username: str, password: str):
    conn=connection()
    cur=conn.cursor()
    hashed_password=hash_password(password)
    query="""
    select id from user_parameters
    where username=? and password=? and is_admin=true
"""
    
    values=(username,hashed_password)
    cur.execute(query,values)

    return bool(cur.fetchone())


def cources():
    conn=cource_con()
    cur=conn.cursor()
    cur.execute("""
    create table if not exists cources(
                courceID integer not null primary key autoincrement,
                name varchar(50),
                number_of_students integer(30),
                is_active boolean default True
    )           
""")
    
def cource_insert(data1:dict):
    conn=cource_con()
    cur=conn.cursor()
    query="""
        insert into cources(
        name,
        number_of_students
        ) values(?,?)
    """
    values=tuple(data1.values())
    cur.execute(query,values)
    conn.commit()
    conn.close()


# def login():
#     username=input("Username: ")
#     password=input("password: ")
#     pk1=get_id(username,password)
#     return pk1



def malumot():
    conn=connection()
    cur=conn.cursor()
   
    cur.execute("""
    select first_name, last_name, phone, username from user_parameters
    where is_admin=false
""")
    
    mal=cur.fetchall()
    
    return mal
malumot()

def kurs_uqi():
    conn = subscribe()
    cur = conn.cursor()
    cur.execute("""
        create table if not exists course_like(
            id integer not null primary key autoincrement,
            user_id integer,
            cource_id integer,
            foreign key(user_id)
            references user_parameters(id),
            foreign key(cource_id)
            references cources(id)
        )
    """)
    conn.commit()
    conn.close()





def show():
    conn=cource_con()
    cur=conn.cursor()
   
    query="""
    select * from cources
    where is_active=true
"""
    values=()
    top=cur.fetchall()
    
    return top
show()
def is_exist(field,value):
    conn=connection()
    cur=conn.cursor()
    query=f"""
    select id from user_parameter
    where {field}=?
"""
    values=(value,)
    cur.execute(query,values)

    return bool(cur.fetchone())

def is_cource_exist(field,value):
    conn=cource_con()
    cur=conn.cursor()
    query=f"""
    select name from cources
    where {field}=? 
"""
    values=(value,)
    cur.execute(query,values)
    return bool(cur.fetchone())


   
# def activate_user(data: dict):
#     username = data['name']

#     conn = connection()
#     cur = conn.cursor()

#     query = """
#         update user_parameters
#         set is_admin=true where username=?
#     """
#     values = (username,)
#     cur.execute(query, values)
#     conn.commit()
#     conn.close()
#     return 200

