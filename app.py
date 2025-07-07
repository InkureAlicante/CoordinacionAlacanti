
from flask import Flask, render_template, request, redirect, url_for
from models.municipio import Municipio
from models.database import Evento, Session

app = Flask(__name__)

# Lista de municipios originales con datos reales (no modificados)
municipios = [
    Municipio("Alicante", "Alicante, conocida en valenciano como Alacant, es una ciudad portuaria con una rica historia que se remonta a la época romana,cuando era conocida como Lucentum. A lo largo de los siglos, ha sido influenciada por diversas culturas, incluyendo los musulmanes, quienes la denominaron Al-Laqant.Fiestas tradicionales: Las Hogueras de San Juan, celebradas en junio, son las fiestas más destacadas de la ciudad, declaradas de Interés Turístico Internacional.Aspectos importantes: Alicante es un importante centro turístico y económico de la Comunidad Valenciana, destacando su puerto y la Explanada de España.Gobierno actual: El alcalde de Alicante es Luis Barcala, del Partido Popular.", 358720, 682, ["Carmen Robledillo Sánchez"], ["Mesa 1"], "Coordinador 1", "Vice 1", ["Miembro A", "Miembro B"]),
    Municipio("Campello", "El Campello tiene vestigios arqueológicos que evidencian asentamientos desde la Edad de Bronce.Fiestas tradicionales: Las fiestas de Moros y Cristianos se celebran en octubre, con desfiles y recreaciones históricas.Aspectos importantes: Destacan sus playas y el yacimiento arqueológico de La Illeta dels Banyets", 31419, 72, [], ["Mesa 1"], "Coordinador 1", "Vice 1", ["Miembro A", "Miembro B"]),
    Municipio("San Juan", "San Juan de Alicante, conocido en valenciano como Sant Joan d'Alacant, tiene orígenes que se remontan a la época romana, aunque su consolidación como núcleo urbano ocurrió en la Edad Media.Fiestas tradicionales: Las fiestas en honor al Santísimo Cristo de la Paz se celebran en septiembre, destacando las procesiones y actos culturales.Aspectos importantes: El municipio es conocido por su cercanía a las playas y su ambiente tranquilo, siendo una zona residencial apreciada.Gobierno actual: Información no disponible en las fuentes proporcionadas.", 25833, 57, [], ["Mesa 1"], "Coordinador 1", "Vice 1", ["Miembro A", "Miembro B"]),
    Municipio("Mutxamel", "Mutxamel es conocido por su tradición agrícola, especialmente en el cultivo de hortalizas y flores. Su historia está vinculada al crecimiento rural de la región. Las fiestas de Moros y Cristianos en honor a la Virgen de Loreto, celebradas en septiembre, son las más destacadas.", 27761, 56, [], ["Mesa 1"], "Coordinador 1", "Vice 1", ["Miembro A", "Miembro B"]),
    Municipio("Augues de Busot", "Aigües de Busot es un municipio conocido por sus aguas termales, utilizadas desde la época romana. Su historia incluye el Balneario de Aigües, fundado en el siglo XIX, y sus fiestas más importantes son las dedicadas a San Francisco de Paula en abril, con actos religiosos y culturales.", 1189, 3, [], ["Mesa 1"], "Coordinador 1", "Vice 1", ["Miembro A", "Miembro B"]),
    Municipio("San Vicente", "San Vicente del Raspeig, conocido en valenciano como Sant Vicent del Raspeig, se desarrolló alrededor de una ermita dedicada a San Vicente Ferrer en el siglo XV. Su crecimiento se consolidó en el siglo XIX con la llegada del ferrocarril.Fiestas tradicionales: Las fiestas patronales en honor a San Vicente Ferrer se celebran el lunes siguiente al lunes de Pascua, con desfiles y actos religiosos.Aspectos importantes: El municipio alberga el campus de la Universidad de Alicante, siendo un importante centro académico.Gobierno actual: El alcalde es José Rafael Pascual Llopis, del Partido Popular.", 60269, 115, [], ["Mesa 1"], "Coordinador 1", "Vice 1", ["Miembro A", "Miembro B"]),
    Municipio("Busot", "Busot es conocido por su castillo de origen musulmán y las Cuevas de Canelobre. En el siglo XIX, contaba con aproximadamente 1.200 habitantes.BUSOT, Fiestas tradicionales: Las fiestas patronales en honor a San Vicente Ferrer se celebran en abril, incluyendo desfiles de Moros y Cristianos.Aspectos importantes: Las Cuevas de Canelobre son una atracción turística destacada por sus formaciones geológicas.Gobierno actual: Información no disponible en las fuentes proporcionadas.", 3629, 7, [], ["Mesa 1"], "Coordinador 1", "Vice 1", ["Miembro A", "Miembro B"]),
    Municipio("Jijona", "Xixona es famosa por ser la cuna del turrón, con una tradición que se remonta al siglo XV. Su fundación está ligada a asentamientos musulmanes. Sus fiestas de Moros y Cristianos, celebradas en agosto, recrean la historia de la Reconquista.", 7307, 10, [], ["Mesa 1"], "Coordinador 1", "Vice 1", ["Miembro A", "Miembro B"]),
    Municipio("Tibi", "Tibi es conocido por su embalse, uno de los más antiguos de Europa, construido en el siglo XVI. Fiestas tradicionales: Las fiestas en honor a San Juan Bautista se celebran en junio, con actos religiosos y festivos. Aspectos importantes: El embalse de Tibi es una obra de ingeniería histórica que aún se conserva. Gobierno actual: Información no disponible en las fuentes proporcionadas.", 1803, 7, [], ["Mesa 1"], "Coordinador de Tibi", "Vicecoordinador de Tibi", ["Miembro A", "Miembro B"]),
    Municipio("Torremanzanas", "Torremanzanas, conocida en valenciano como La Torre de les Maçanes, tiene orígenes medievales con tradiciones agrícolas que aún se conservan. Sus fiestas patronales en honor a Santa Ana se celebran en julio, destacando actos religiosos y populares.", 744, 0, [], ["Mesa 1"], "Coordinador 1", "Vice 1", ["Miembro A", "Miembro B"]),
    Municipio("Agress", "Agres, en la comarca de El Comtat. Su historia está marcada por su origen musulmán, con referencias a su existencia en documentos del siglo XIII, cuando fue conquistado por el rey Jaime I de Aragón durante la Reconquista. Posteriormente, el municipio pasó a manos cristianas y fue repoblado tras la expulsión de los moriscos en el siglo XVII. Uno de los elementos más destacados de su historia es el Santuario de la Mare de Déu d’Agres, un importante lugar de peregrinación, ligado a la aparición de la Virgen en el siglo XV.Fiestas en honor a la Virgen de Agres (septiembre)Son las festividades más importantes del pueblo, en honor a la Mare de Déu d’Agres.Moros y Cristianos (último fin de semana de agosto) Fiesta de Sant Antoni (enero) Se encienden hogueras en honor a San Antonio Abad y se realiza la tradicional bendición de los animales. Feria de Santa Cecília (noviembre)Gobierno Municipal está gobernado en la actualidad por el Partido Popular (PP), con Josep Manel Francés Perales como alcalde.", 580, 0, [], ["Mesa 1"], "Coordinador 1", "Vice 1", ["Miembro A", "Miembro B"]),
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
