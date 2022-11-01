import json

def index():
    with open('../PMA-33-Computer-Network/server/inna/templates/index.html') as template:
        return template.read()


def blog():
    with open('../PMA-33-Computer-Network/server/inna/templates/blog.html') as template:
        return template.read()


def post():
    with open('../PMA-33-Computer-Network/server/inna/templates/post.json') as template:
        return json.load(template)


def put():
    with open('../PMA-33-Computer-Network/server/inna/templates/put.json') as template:
        return json.load(template)


def delete():
    with open('../PMA-33-Computer-Network/server/inna/templates/delete.json') as template:
        return json.load(template)


def get():
    with open('../PMA-33-Computer-Network/server/inna/templates/get.json') as template:
        return json.load(template)