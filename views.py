import json
def index():
    with open('templates/index.html') as template:
        return template.read()

def home():
    with open('templates/home.html') as template:
        return template.read()

def post():
    with open('templates/post.html') as template:
        return template.read()
