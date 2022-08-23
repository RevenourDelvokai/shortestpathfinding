import streamlit as st
import hashlib
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx


st.title("Shortest Path Creator")
markdown = """This is a small project which made for identifying a shortest path in a visual map. 
            
            Please chose the content in the right"""

st.markdown(markdown)

def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

#password make
def check_hashes(password,hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False

import sqlite3
conn = sqlite3.connect('data.db')
c = conn.cursor()

#DB functions
def create_usertable():
    c.execute('CREATE TABLE IF NOT EXISTS usertable(username TEXT, password TEXT)')

def add_userdata(username,password):
	c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
	conn.commit()

def login_user(username,password):
	c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
	data = c.fetchall()
	return data


def view_all_users():
	c.execute('SELECT * FROM userstable')
	data = c.fetchall()
	return data

def main():
    """Simple Login App"""
