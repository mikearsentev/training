import hashlib as hash
import psycopg2 
import os
from dotenv import load_dotenv

load_dotenv()
class information():
    def profile_creator(self,first_name, last_name):
        self.name = first_name
        self.last_n = last_name
        password = input("Input password: ")
        hash_object = hash.sha256(password.encode())
        hash_password = hash_object.hexdigest()
        #print("Our pass: ", hash_password)
        try:
            conn = psycopg2.connect(
                dbname=os.getenv("DB_NAME"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                host=os.getenv("DB_HOST"),
                port=os.getenv("DB_PORT")
            )
            cur = conn.cursor()
            # Создаем таблицу, если ее еще нет
            cur.execute("""
                CREATE TABLE IF NOT EXISTS profiles (
                    id SERIAL PRIMARY KEY,
                    first_name VARCHAR(100) NOT NULL,
                    last_name VARCHAR(100) NOT NULL,
                    password_hash VARCHAR(256) NOT NULL
                );
            """)
            
            # Вставляем данные
            cur.execute("""
                INSERT INTO profiles (first_name, last_name, password_hash)
                VALUES (%s, %s, %s);
            """, (self.name, self.last_n, hash_password))
            
            conn.commit()
            print("Профиль успешно сохранен в базе данных.")
            
            cur.close()
            conn.close()
        except Exception as e:
            print("Ошибка при работе с базой:", e)