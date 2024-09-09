import streamlit as st
import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()

#Usersテーブルから全ての行を引っ張ってくる
def show_data():
    c.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)')
    c.execute('SELECT * FROM users')
    data = c.fetchall()
    for d in data:
        st.write(d)


#Usersテーブルに指定された行を挿入する
def add_data(name):
    c.execute('INSERT INTO users (name) VALUES (?)', name)
    conn.commit()


# Usersテーブルからnameで指定された行を引っ張ってくる
def search_data(key):
    c.execute('SELECT * FROM users WHERE name = ?', key)
    data = c.fetchall()
    for d in data:
        st.write(d)


# Usersテーブルから末尾100件を削除する（ほぼリセット）
def reset_data():
    c.execute('DELETE FROM users ORDER BY id DESC LIMIT 100')
    conn.commit()


# データベースを全表示したい
st.title('DATABASE')
show_data()


# データベースに行を追加したい
st.title('Add')
name = st.text_input('name')
if st.button('Add'):
    add_data(name)


# データベースの行を検索したい
st.title('Search')
name = st.text_input('name', key='ya')
if st.button('Search'):
    search_data(name)


# データベースをリセットしたい
st.title('Reset')
if st.button('Reset100'):
    reset_data()

conn.close()
