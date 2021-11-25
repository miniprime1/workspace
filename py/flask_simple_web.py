from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return 'Hello, World!'

@app.route('/user/<user_name>/<user_id>')
def user(user_name, user_id):
    return f'Hello, {user_name}({user_id})!'

app.run()

"""
print("Simple Web Site v1.0\n")
print("[Login]")
user_name = input("Username: ")
user_id = input("User ID: ")
user_pwd = input("Password: ")
print("")
"""