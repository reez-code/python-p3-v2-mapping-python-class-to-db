# lib/config.py
import sqlite3

CONN = sqlite3.connect('company.sqlite')
CURSOR = CONN.cursor()
