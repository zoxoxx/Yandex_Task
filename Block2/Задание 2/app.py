from jinja2 import Template
import json

# Загрузка данных из JSON
json_data = '''
{
    "event": "mission_complete",
    "id": 123,
    "points": 150
}
'''
data = json.loads(json_data)

# Загрузка HTML-шаблона
with open('template.html', encoding='utf-8') as file:
    template_content = file.read()

# Создание объекта шаблона Jinja2
template = Template(template_content)

# Рендеринг письма с данными
rendered_email = template.render(username="Имя пользователя", points=data['points'])

# Генерация нового файла и замена старого
file.close()
try:
    myfile = open("2.html", "w", encoding='utf-8')
    try:
        myfile.write(rendered_email)
    finally:
        myfile.close()
except Exception as ex:
    print(ex)
