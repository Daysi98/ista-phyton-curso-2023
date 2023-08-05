from flask import Flask, jsonify
import csv
app = Flask(__name__)

@app.route('/lista_estudiantes', methods=['GET'])
def get_listaestudiantes():
    with open('escuela_api/datos/estudiante.csv', 'r', encoding='utf-8') as archivo_estudiantes:
        estudiantes = csv.DictReader(archivo_estudiantes)
        lista_estudiante = list(estudiantes)
        lista_estudiantes_asc = sorted(lista_estudiante,
            key=lambda parametro: (parametro['primer_apellido'],parametro['segundo_apellido'],parametro['primer_nombre'],parametro['segundo_nombre'],))
        return jsonify(lista_estudiantes_asc)