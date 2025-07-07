import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ''))


from flask import Flask, render_template, request, redirect, url_for
from models.municipio import Municipio
from models.database import Evento, Session

app = Flask(__name__)

# Lista de municipios restaurada del original
municipios = [
    Municipio("Alicante", "Alicante, conocida en valenciano como Alacant, es una ciudad portuaria con una rica historia que se remonta a la época romana...", 358720, 150, [], ["Mesa 1"], "Coordinador 1", "Vice 1", ["Miembro A", "Miembro B"]),
    Municipio("Campello", "El Campello tiene vestigios arqueológicos que evidencian asentamientos desde la Edad de Bronce...", 30600, 150, [], ["Mesa 1"], "Coordinador 1", "Vice 1", ["Miembro A", "Miembro B"]),
    Municipio("San Juan", "San Juan de Alicante, conocido en valenciano como Sant Joan d'Alacant, tiene orígenes que se remontan a la época romana...", 25275, 150, [], ["Mesa 1"], "Coordinador 1", "Vice 1", ["Miembro A", "Miembro B"]),
    Municipio("Mutxamel", "Mutxamel es conocido por su tradición agrícola, especialmente en el cultivo de hortalizas y flores...", 27761, 150, [], ["Mesa 1"], "Coordinador 1", "Vice 1", ["Miembro A", "Miembro B"]),
    Municipio("Augues de Busot", "Aigües de Busot es un municipio conocido por sus aguas termales, utilizadas desde la época romana...", 1189, 150, [], ["Mesa 1"], "Coordinador 1", "Vice 1", ["Miembro A", "Miembro B"]),
    Municipio("San Vicente", "San Vicente del Raspeig, conocido en valenciano como Sant Vicent del Raspeig...", 60269, 150, [], ["Mesa 1"], "Coordinador 1", "Vice 1", ["Miembro A", "Miembro B"]),
    Municipio("Busot", "Busot es conocido por su castillo de origen musulmán y las Cuevas de Canelobre...", 3629, 150, [], ["Mesa 1"], "Coordinador 1", "Vice 1", ["Miembro A", "Miembro B"]),
    Municipio("Jijona", "Xixona es famosa por ser la cuna del turrón, con una tradición que se remonta al siglo XV...", 7307, 150, [], ["Mesa 1"], "Coordinador 1", "Vice 1", ["Miembro A", "Miembro B"]),
    Municipio("Tibi", "Tibi es conocido por su embalse, uno de los más antiguos de Europa...", 1803, 150, [], ["Mesa 1"], "Coordinador de Tibi", "Vicecoordinador de Tibi", ["Miembro A", "Miembro B"]),
    Municipio("Torremanzanas", "Torremanzanas, conocida en valenciano como La Torre de les Maçanes, tiene orígenes medievales...", 744, 150, [], ["Mesa 1"], "Coordinador 1", "Vice 1", ["Miembro A", "Miembro B"]),
    Municipio("Agress", "Agres, en la comarca de El Comtat. Su historia está marcada por su origen musulmán...", 610, 1, [], ["Mesa 1"], "Coordinador 1", "Vice 1", ["Miembro A", "Miembro B"]),
]

@app.route('/')
def index():
    return render_template("base.html", municipios=municipios)

@app.route('/municipio/<name>')
def municipio_detail(name):
    municipio = next((m for m in municipios if m.name == name), None)
    session = Session()
    eventos = session.query(Evento).filter_by(municipio=name).all()
    session.close()
    if municipio:
        municipio.events = [e.nombre for e in eventos]
        return render_template("municipio.html", municipio=municipio)
    return "Municipio no encontrado", 404

@app.route('/add_event/<name>', methods=["POST"])
def add_event(name):
    session = Session()
    event_name = request.form.get("event_name")
    if event_name:
        nuevo_evento = Evento(municipio=name, nombre=event_name)
        session.add(nuevo_evento)
        session.commit()
    session.close()
    return redirect(url_for('municipio_detail', name=name))

@app.route('/remove_event/<name>', methods=["POST"])
def remove_event(name):
    session = Session()
    event_name = request.form.get("event_name")
    evento = session.query(Evento).filter_by(municipio=name, nombre=event_name).first()
    if evento:
        session.delete(evento)
        session.commit()
    session.close()
    return redirect(url_for('municipio_detail', name=name))

if __name__ == '__main__':
    app.run(debug=True)
