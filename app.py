from flask import Flask
app = FLASK(_name_)

@app.route('/')
def hello_world():
    return 'Hello, simple app'