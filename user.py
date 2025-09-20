import sqlite3
import hashlib
import streamlit as st


database_name = 'database.db'


# Initialize the SQLite database
def init_db():
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL,
            role TEXT DEFAULT 'user'
        )
    ''')
    conn.commit()
    conn.close()

# Hash the password for secure storage
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Add a new user to the database
def add_user_to_db(username, hashed_password, role='user'):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO users (username, password, role) VALUES (?, ?, ?)', 
                       (username, hashed_password, role))
        conn.commit()
    except sqlite3.IntegrityError:
        st.error("Username already exists. Please choose another.")
    conn.close()

# Verify user credentials and retrieve user role
def verify_user(username, password):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    hashed_password = hash_password(password)
    cursor.execute("SELECT role FROM users WHERE username = ? AND password = ?", (username, hashed_password))
    result = cursor.fetchone()
    conn.close()
    return (result is not None, result[0] if result else None)

# Sign-up function for new users
def signup():

    # Título da página
    st.title("🌟 Tela de Cadastro 🌟")
    st.subheader("Criar uma conta para acessar o sistema")

    new_username = st.text_input("Create Username")
    new_password = st.text_input("Create Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")
    
    if st.button("Sign Up"):
        if new_password != confirm_password:
            st.error("Passwords do not match.")
        else:
            hashed_password = hash_password(new_password)
            add_user_to_db(new_username, hashed_password)
            st.success("Account created successfully!")

# Login function for registered users
def login():

    # Título da página
    st.title("🌟 Tela de Login 🌟")
    st.subheader("Acesse sua conta para entrar no sistema")


    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        is_valid, role = verify_user(username, password)
        if is_valid:
            st.success(f"Welcome back, {username}!")
            st.session_state['role'] = role
            st.session_state['username'] = username
            st.session_state['logged_in'] = True
        else:
            st.error("Invalid username or password")
            
        st.rerun()

# Member dashboard for regular users
def member_dashboard():
    st.title("Member Dashboard")
    st.write(f"Welcome to your dashboard, {st.session_state['username']}!")

# Admin dashboard with additional features
def admin_dashboard():
    if st.session_state.get('role') == 'admin':
        st.title("Admin Dashboard")
        view_user_data()
    else:
        st.error("Access Denied: Admins only.")

# Display all user data for admin users
def view_user_data():
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    cursor.execute("SELECT username, role FROM users")
    user_data = cursor.fetchall()
    conn.close()
    st.dataframe(user_data)

# Main function to handle different states
def main():
    st.sidebar.title("Navigation")
    choice = st.sidebar.radio("Go to", ["Login", "Sign Up",  "Dashboard"])
    
    if choice == "Sign Up":
        signup()
    elif choice == "Login":
        login()
    elif choice == "Dashboard":
        if 'username' in st.session_state:
            if st.session_state['role'] == 'admin':
                admin_dashboard()
            else:
                member_dashboard()
        else:
            st.warning("Please log in to access the dashboard.")

# Initialize database on first run
if __name__ == '__main__':
    init_db()
    main()