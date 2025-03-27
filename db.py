import os
import time
import secrets
from colorama import Fore, init
import sqlite3
from abc import ABC, abstractmethod
from dotenv import load_dotenv
load_dotenv()

init(autoreset=True)

# Manejador de eventos de las carpetas

class Database:
    def __init__(self):
        self.db = os.getenv("DB_NAME")

    def __enter__(self):
        self.conn = sqlite3.connect(self.db)
        self.cur = self.conn.cursor()
        return self.cur
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.conn.commit()
        self.cur.close()
        self.conn.close()

class Crud(ABC):
    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def delete(self):
        pass

# Clase de usuario que hereda de CRUD
class User(Crud):
    def __init__(self, username):
        self.username = username
        self.token = None

    def create(self):
        try:
            with Database() as cur:
                self.token = secrets.token_hex(5)
                cur.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, token TEXT)")
                cur.execute("INSERT INTO users (username, token) VALUES (?,?)", (self.username, self.token))
                print(Fore.GREEN + "User created successfully")
        except sqlite3.OperationalError as e:
            print(Fore.RED + f"Error: {e}")
    
    @classmethod
    def read(cls):
        try:
            with Database() as cur:
                cur.execute("SELECT * FROM users")
                print(Fore.GREEN + "Users fetched successfully")
                return cur.fetchall()
        except sqlite3.OperationalError as e:
            print(Fore.RED + f"Error: {e}")
    
    @classmethod
    def comprobe(cls, username,token):
        try:
            with Database() as cur:
                cur.execute("SELECT * FROM users WHERE username = ? AND token = ?", (username, token))
                print(Fore.GREEN + "User fetched successfully")
                if cur.fetchone():
                    return True
                else:
                    return False
        except sqlite3.OperationalError as e:
            print(Fore.RED + f"Error: {e}")
            return False

    def update(self):
        try:
            with Database() as cur:
                cur.execute("UPDATE users SET token = ? WHERE username = ?", (self.token, self.username))
                print(Fore.GREEN + "User updated successfully")
        except sqlite3.OperationalError as e:
            print(Fore.RED + f"Error: {e}")
    
    def delete(self):
        try:
            with Database() as cur:
                cur.execute("DELETE FROM users WHERE username = ?", (self.username,))
                print(Fore.GREEN + "User deleted successfully")
        except sqlite3.OperationalError as e:
            print(Fore.RED + f"Error: {e}")


