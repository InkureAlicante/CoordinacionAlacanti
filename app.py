# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
from models.municipio import Municipio

app = Flask(__name__)

# Lista de municipios
municipios = [
    Municipio("Alicante", "Breve historia...", 2000, 150, ["Acto 1"], ["Mesa 1"], "Coordinador 1", "Vice 1", ["Miembro A", "Miembro B"]),
    Municipio("Campello", "Breve historia...", 2000, 150, ["Acto 1"], ["Mesa 1"], "Coordinador 1", "Vice 1", ["Miembro A", "Miembro B"]),
    Municipio("San Juan", "Breve historia...", 2000, 150, ["Acto 1"], ["Mesa 1"], "Coordinador 1", "Vice 1", ["Miembro A", "Miembro B"]),
    Municipio("Mutxamel", "Breve historia...", 2000, 150, ["Acto 1"], ["Mesa 1"], "Coordinador 1", "Vice 1", ["Miembro A", "Miembro B"]),
    Municipio("Augues de Busot", "Breve historia...", 2000, 150, ["Acto 1"], ["Mesa 1"], "Coordinador 1", "Vice 1", ["Miembro A", "Miembro B"]),
    Municipio("Busot", "Breve historia...", 2000, 150, ["Acto 1"], ["Mesa 1"], "Coordinador 1", "Vice 1", ["Miembro A", "Miembro B"]),
    Municipio("San Vicente", "Breve historia...", 2000, 150, ["Acto 1"], ["Mesa 1"], "Coordinador 1", "Vice 1", ["Miembro A", "Miembro B"]),
    Municipio("Busot", "Breve historia...", 2000, 150, ["Acto 1"], ["Mesa 1"], "Coordinador 1", "Vice 1", ["Miembro A", "Miembro B"]),
    Municipio("Jijona", "Breve historia...", 2000, 150, ["Acto 1"], ["Mesa 1"], "Coordinador 1", "Vice 1", ["Miembro A", "Miembro B"]),
    Municipio("Tibi", "Breve historia...", 2000, 150, ["Acto 1"], ["Mesa 1"], "Coordinador 1", "Vice 1", ["Miembro A", "Miembro B"]),
]
@app.route('/')
def index():
    return render_template("base.html", municipios=municipios)

@app.route('/municipio/<name>')
def municipio_detail(name):
    municipio = next((m for m in municipios if m.name == name), None)
    if municipio:
        return render_template("municipio.html", municipio=municipio)
    return "Municipio no encontrado", 404

@app.route('/add_event/<name>', methods=["POST"])
def add_event(name):
    municipio = next((m for m in municipios if m.name == name), None)
    if municipio:
        event_name = request.form.get("event_name")
        municipio.add_event(event_name)
        return render_template("municipio.html", municipio=municipio)
    return "Municipio no encontrado", 404

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/remove_event/<name>', methods=["POST"])
def remove_event(name):
    municipio = next((m for m in municipios if m.name == name), None)
    if municipio:
        event_name = request.form.get("event_name")
        if event_name in municipio.events:
            municipio.remove_event(event_name)
            return render_template("municipio.html", municipio=municipio)  # Refleja los cambios
        else:
            return f"Evento '{event_name}' no encontrado en el municipio '{name}'", 404
    return f"Municipio '{name}' no encontrado", 404
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
