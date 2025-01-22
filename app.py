# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
from models.municipio import Municipio
from flask import redirect, url_for
app = Flask(__name__)

# Lista de municipios
municipios = [
    Municipio("Alicante", "Alicante, conocida en valenciano como Alacant, es una ciudad portuaria con una rica historia que se remonta a la época romana,cuando era conocida como Lucentum. A lo largo de los siglos, ha sido influenciada por diversas culturas, incluyendo los musulmanes, quienes la denominaron Al-Laqant.Fiestas tradicionales: Las Hogueras de San Juan, celebradas en junio, son las fiestas más destacadas de la ciudad, declaradas de Interés Turístico Internacional.Aspectos importantes: Alicante es un importante centro turístico y económico de la Comunidad Valenciana, destacando su puerto y la Explanada de España.Gobierno actual: El alcalde de Alicante es Luis Barcala, del Partido Popular.", 358.720, 150, ["Acto 1"], ["Mesa 1"], "Coordinador 1", "Vice 1", ["Miembro A", "Miembro B"]),
    Municipio("Campello", "El Campello tiene vestigios arqueológicos que evidencian asentamientos desde la Edad de Bronce.Fiestas tradicionales: Las fiestas de Moros y Cristianos se celebran en octubre, con desfiles y recreaciones históricas.Aspectos importantes: Destacan sus playas y el yacimiento arqueológico de La Illeta dels Banyets", 30 600, 150, ["Acto 1"], ["Mesa 1"], "Coordinador 1", "Vice 1", ["Miembro A", "Miembro B"]),
    Municipio("San Juan", "San Juan de Alicante, conocido en valenciano como Sant Joan d'Alacant, tiene orígenes que se remontan a la época romana, aunque su consolidación como núcleo urbano ocurrió en la Edad Media.Fiestas tradicionales: Las fiestas en honor al Santísimo Cristo de la Paz se celebran en septiembre, destacando las procesiones y actos culturales.Aspectos importantes: El municipio es conocido por su cercanía a las playas y su ambiente tranquilo, siendo una zona residencial apreciada.Gobierno actual: Información no disponible en las fuentes proporcionadas.", 25.275, 150, ["Acto 1"], ["Mesa 1"], "Coordinador 1", "Vice 1", ["Miembro A", "Miembro B"]),
    Municipio("Mutxamel", "Mutxamel es conocido por su tradición agrícola, especialmente en el cultivo de hortalizas y flores. Su historia está vinculada al crecimiento rural de la región. Las fiestas de Moros y Cristianos en honor a la Virgen de Loreto, celebradas en septiembre, son las más destacadas.", 27.761, 150, ["Acto 1"], ["Mesa 1"], "Coordinador 1", "Vice 1", ["Miembro A", "Miembro B"]),
    Municipio("Augues de Busot", "Aigües de Busot es un municipio conocido por sus aguas termales, utilizadas desde la época romana. Su historia incluye el Balneario de Aigües, fundado en el siglo XIX, y sus fiestas más importantes son las dedicadas a San Francisco de Paula en abril, con actos religiosos y culturales.", 1.189, 150, ["Acto 1"], ["Mesa 1"], "Coordinador 1", "Vice 1", ["Miembro A", "Miembro B"]),
    Municipio("San Vicente", "San Vicente del Raspeig, conocido en valenciano como Sant Vicent del Raspeig, se desarrolló alrededor de una ermita dedicada a San Vicente Ferrer en el siglo XV. Su crecimiento se consolidó en el siglo XIX con la llegada del ferrocarril.Fiestas tradicionales: Las fiestas patronales en honor a San Vicente Ferrer se celebran el lunes siguiente al lunes de Pascua, con desfiles y actos religiosos.Aspectos importantes: El municipio alberga el campus de la Universidad de Alicante, siendo un importante centro académico.Gobierno actual: El alcalde es José Rafael Pascual Llopis, del Partido Popular.", 60.269, 150, ["Acto 1"], ["Mesa 1"], "Coordinador 1", "Vice 1", ["Miembro A", "Miembro B"]),
    Municipio("Busot", "Busot es conocido por su castillo de origen musulmán y las Cuevas de Canelobre. En el siglo XIX, contaba con aproximadamente 1.200 habitantes.BUSOT, Fiestas tradicionales: Las fiestas patronales en honor a San Vicente Ferrer se celebran en abril, incluyendo desfiles de Moros y Cristianos.Aspectos importantes: Las Cuevas de Canelobre son una atracción turística destacada por sus formaciones geológicas.Gobierno actual: Información no disponible en las fuentes proporcionadas.", 3629 , 150, ["Acto 1"], ["Mesa 1"], "Coordinador 1", "Vice 1", ["Miembro A", "Miembro B"]),
    Municipio("Jijona", "Xixona es famosa por ser la cuna del turrón, con una tradición que se remonta al siglo XV. Su fundación está ligada a asentamientos musulmanes. Sus fiestas de Moros y Cristianos, celebradas en agosto, recrean la historia de la Reconquista.", 7.307, 150, ["Acto 1"], ["Mesa 1"], "Coordinador 1", "Vice 1", ["Miembro A", "Miembro B"]),
    Municipio("Tibi", "Tibi es conocido por su embalse, uno de los más antiguos de Europa, construido en el siglo XVI.Fiestas tradicionales: Las fiestas en honor a San Juan Bautista se celebran en junio, con actos religiosos y festivos.Aspectos importantes: El embalse de Tibi es una obra de ingeniería histórica que aún se conserva.Gobierno actual: Información no disponible en las fuentes proporcionadas.", 1803, 150, ["Acto 1"], ["Mesa 1"], "Coordinador 1", "Vice 1", ["Miembro A", "Miembro B"]),
    Municipio("Torremanzanas", "Torremanzanas, conocida en valenciano como La Torre de les Maçanes, tiene orígenes medievales con tradiciones agrícolas que aún se conservan. Sus fiestas patronales en honor a Santa Ana se celebran en julio, destacando actos religiosos y populares.", 744, 150, ["Acto 1"], ["Mesa 1"], "Coordinador 1", "Vice 1", ["Miembro A", "Miembro B"]),
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
        return redirect(url_for('municipio_detail', name=name))
    return f"Municipio '{name}' no encontrado", 404
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
