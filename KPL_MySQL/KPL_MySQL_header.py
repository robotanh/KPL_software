import mysql.connector

from datetime import datetime
import random
import time

db = mysql.connector.connect(
    host="localhost",
    user="KPL_admin",
    passwd="adminkplpassword",
    database = "kpl_gaspump_db"
)

mycursor = db.cursor()

col="id_voi_bom,ma_lan_bom,thoi_gian,so_lit_da_bom,gia_ban_tren_lit,tong_ban_hang,so_tien_thu_ve"

def insert(table,id_voi_bom,ma_lan_bom,thoi_gian,so_lit_da_bom,gia_ban_tren_lit,tong_ban_hang,so_tien_thu_ve):
    tuple_val=(id_voi_bom,ma_lan_bom,thoi_gian,so_lit_da_bom,gia_ban_tren_lit,tong_ban_hang,so_tien_thu_ve)
    mycursor.execute(f"INSERT INTO {table} ({col}) VALUES (%s,%s,%s,%s,%s,%s,%s)",tuple_val)
    db.commit()


def faking_data(id_voi_bom,ma_lan_bom):
    now = datetime.now()
    table="recent_gaspump"
    thoi_gian=now.strftime("%Y-%m-%d %H:%M:%S")
    so_lit_da_bom=random.randint(1, 20)
    gia_ban_tren_lit=20000
    tong_ban_hang=1
    so_tien_thu_ve=so_lit_da_bom*gia_ban_tren_lit

    insert(table,
    id_voi_bom,
    ma_lan_bom,
    thoi_gian,
    so_lit_da_bom,
    gia_ban_tren_lit,
    tong_ban_hang,
    so_tien_thu_ve)

    time.sleep(random.uniform(0, 5))



# insert(table="recent_gaspump",
#     id_voi_bom=6,
#     ma_lan_bom=1,
#     thoi_gian="2024-05-28 20:34:30",
#     so_lit_da_bom=5,
#     gia_ban_tren_lit=20000,
#     tong_ban_hang=1,
#     so_tien_thu_ve=100000)

#YYYY-MM-DD hh:mm:ss



# mycursor.execute("CREATE TABLE recent_gaspump (id INT PRIMARY KEY AUTO_INCREMENT,id_voi_bom INT, ma_lan_bom INT, thoi_gian DATETIME, so_lit_da_bom DOUBLE, gia_ban_tren_lit INT, tong_ban_hang INT, so_tien_thu_ve INT)")

# mycursor.execute("CREATE DATABASE kpl_gaspump_db")
