import sqlite3
import streamlit as st

def createDb():
    # 데이터베이스 연결 (데이터베이스가 없으면 새로 생성됨)
    conn = sqlite3.connect('dajunga.db')

    # 커서 객체 생성
    cursor = conn.cursor()

    # 테이블 생성
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tb_score (
            nick_name TEXT NOT NULL,
            reg_date DATE DEFAULT (datetime('now')),
            score INTEGER NOT NULL
        )
    ''')
    conn.close()

# 데이터 삽입
def insertTb(nick,score):
    conn = sqlite3.connect('dajunga.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO tb_score (nick_name, score) VALUES (?, ?)
    ''', (nick, score))

    # 커밋하여 변경 사항 저장
    conn.commit()
    conn.close()

# 데이터 삭제
def deleteTb():
    conn = sqlite3.connect('dajunga.db')
    cursor = conn.cursor()
    cursor.execute('''
       delete from tb_score 
    ''')

    # 커밋하여 변경 사항 저장
    conn.commit()
    conn.close()

def list():    
# 데이터 조회
    conn = sqlite3.connect('dajunga.db')
    cursor = conn.cursor()
    cursor.execute('SELECT nick_name, score FROM tb_score ORDER BY score DESC, reg_date DESC LIMIT 10')
    rows = cursor.fetchall()
    list = ""
    for row in rows:
        list = list + str(row[0])+"|"+str(row[1])+"###"


    st.text("@@@@"+list+"@@@@")       
    # 연결 종료
    conn.close()

# You can read query params using key notation
if st.query_params["cmd"] == "save":
    insertTb(st.query_params["nick"],st.query_params["score"])
    list()
elif st.query_params["cmd"] == "delete":
    deleteTb()
else:
    list()
    


