from flask import Flask, jsonify, request
import json
import csv
app = Flask(__name__)

@app.route('/lista_estudiantes', methods=['GET'])
def get_listaestudiantes():
    with open('escuela_api/datos/estudiante.csv', 'r', encoding='utf-8') as archivo_estudiantes:
        estudiantes = csv.DictReader(archivo_estudiantes)
        lista_estudiante = list(estudiantes)
        lista_estudiantes_asc = sorted(lista_estudiante,
            key=lambda parametro: (parametro['primer_apellido'],parametro['segundo_apellido'],parametro['primer_nombre'],parametro['segundo_nombre'],))
        return json.dumps(lista_estudiantes_asc)
@app.route('/registro_asistencia', methods=['POST'])
def post_registroasistencia():
    asistencia = request.get_json()
    with open('escuela_api/datos/asistencia.csv','a',newline='') as archivo_asistencias:
        escritor = csv.writer(archivo_asistencias)
        escritor.writerow([asistencia["cedula"],asistencia["materia"],asistencia["fecha_año"],asistencia["fecha_mes"],asistencia["fecha_dia"]])
        return jsonify({'mensaje': 'La sistencia ha sido registrada'}), 201

@app.route('/total_asistencias', methods=['GET'])
def get_totalasistencias():
    cedula = request.args.get('cedula_estudiante')
    curso = request.args.get('nombre_curso')
    total_asistencias = 0
    with open('escuela_api/datos/asistencia.csv', 'r', encoding='utf-8') as archivo_asistencias:
        for fila in csv.DictReader(archivo_asistencias):
            if fila['cedula'] == cedula and fila['materia'] == curso:
                total_asistencias += 1
    if total_asistencias>0:
        return(jsonify({'total_asistencias':total_asistencias}),200)
    else:
        return (jsonify({'error': 'El estudiante o la materia solicitada no existen'}), 404)


