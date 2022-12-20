import json

# Ficheros JSON
# JSON: Notación de objeto de JavaScript(JavaScript Object Notation)
# Documentación: https: // docs.python.org/3/library/json.html
# Escritura de datos en JSON


contactos = [
    ("Manuel", "Desarrollador Web", "manuel@ejemplo.com"),
    ("Lorena", "Gestora de proyectos", "lorena@ejemplo.com"),
    ("Javier", "Analista de datos", "javier@ejemplo.com"),
    ("Marta", "Experta en Python", "marta@ejemplo.com")
]

datos = []

for nombre, empleo, email in contactos:
    datos.append({"nombre": nombre, "empleo": empleo, "email": email})

with open("contactos.json", "w") as jsonfile:
    json.dump(datos, jsonfile)

# Lectura de datos en JSON
with open("contactos.json") as jsonfile:
    datos = json.load(jsonfile)
    for contacto in datos:
        print(contacto["nombre"], contacto["empleo"], contacto["email"])
