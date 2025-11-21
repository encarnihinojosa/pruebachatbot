import os
from flask import Flask, request, jsonify # <--- Nuevas importaciones de Flask
from flask_cors import CORS # <-- ¡Nueva importación!
from google import genai
from google.genai import types

app = Flask(__name__)
ALLOWED_ORIGINS = [
    "https://www.diariosur.es",
    "http://127.0.0.1:5500"  # <-- ¡Este es tu origen local!
]
CORS(app, resources={r"/chat": {"origins": ALLOWED_ORIGINS}})
# -----------------------------------------------------------------
# SOLUCIÓN: Desactiva la escapada ASCII para ver caracteres en español
app.json.ensure_ascii = False 
# Asegura que el contenido se marque como UTF-8
app.json.charset = 'utf-8' 
# -----------------------------------------------------------------

# Cargar la clave API (hay que encriptarla primero en Terminal)
client = genai.Client()
# Convertir la fuente de información en el formato que el modelo puede leer
fuente = [
    "Las tocayas andaluzas en el mundo: descubre qué ciudad es la más repetida. Cádiz, Sevilla o Jaén, y también Andalucía, tienen dobles toponímicos a lo largo del globo. Lunes, 17 de noviembre 2025, 00:34. Málaga no es la única ciudad andaluza que tiene su réplica en otra parte del mundo. Andalucía −sí, también la toponimia de la comunidad autónoma− tiene un total de 65 poblaciones tocayas, tanto dentro de las fronteras españolas como fuera de ellas. Hay capitales provinciales de la región que ocupan el podio de repeticiones con bastante ventaja y otras ciudades andaluzas cuyo nombre sólo se reproduce una vez o ninguna. La gran base de datos 'World Cities Database' (de la compañía Maxmind) recoge más de tres millones de nombres de poblaciones de todo el mundo; donde están las otras 'Córdobas', 'Almerías' o 'Granadas'. Damos una vuelta al mundo para descubrirlas. El mapa de las tocayas andaluzas en el mundo Se representa la ubicación de la población con su nombre literal. Se incluyen algunas localizaciones donde el nombre de la ciudad andaluza se repite como una parte del nombre completo. En el filtro, se pueden desactivar o activar la visualización de cada nombre. El vestigio de la época colonial de España queda patente visualmente en el mapa. La mayoría de estos familiares lejanos se encuentran en el continente americano o en Filipinas. Pero, ¿qué capital andaluza es la más repetida a lo largo del globo? Granada es la toponimia andaluza con más réplicas. En España, es parte del nombre de otras 5 poblaciones −3 de ellas en la provincia con el mismo nombre, 1 en Huelva y 1 en Barcelona−. Pero en el mundo nombra a 13 localizaciones, lo que la suma le da 18 repeticiones. En segundo lugar se encuentra Córdoba con 15 clones −5 en España y 10 en el mundo− y, en tercera posición, Málaga con 12 tocayas −4 dentro de nuestras fronteras y 8 fuera de ellas−. 3 tocayas en el mundo Andalucía México Puerto Rico Colombia Las tres réplicas de Andalucía se encuentran en el centro del continente americano. La de Colombia (en el departamento Valle del Cauca) es la población más grande con más de 17.000 habitantes. Este municipio, a tan sólo 2 horas de la gran ciudad colombiana de Cali, es conocida también como 'La capital de la gelatina' por la producción de este dulce. Llamado anteriormente San Vicente, a principios del siglo XX cambió de nombre a la 'Andalucía' actual mediante el voto popular de sus habitantes. 13 tocayas en el mundo Granada California, EEUU California, EEUU Minnesota, EEUU Colorado, EEUU El Salvador México Magdalena, Colombia Negros Occidental, Filipinas Nicaragua Antioquia, Colombia Sucre, Colombia Meta, Colombia Argentina En Nicaragua se encuentra el clon de Granada más habitado (más de 90.000 vecinos). Y en segundo lugar por tamaño, una gran urbanización, Granada Hills, de California (EEUU). En el país norteamericano son 4 las réplicas de la ciudad de la Alhambra y el resto se concentra en centroamérica y Colombia. La Granada de Nicaragua se encuentra en el departamento del mismo nombre y es una de las ciudades más antiguas de América Central, ya que fue fundada en 1524. Tal es su importancia, que casi fue declarada capital del país. Al igual que la Granada andaluza, la Granada nicaragüense tiene referencias arquitectónicas y culturales moriscas. 10 tocayas en el mundo Córdoba Bolívar, Colombia Antioquia, Colombia México Quindío, Colombia Filipinas Cali, Colombia Córdoba, Colombia Perú Corrientes, Argentina Argentina Sin lugar a dudas, la tocaya más famosa de las ciudades andaluzas repite el nombre de Córdoba. Su clon argentino es la capital de la provincia con el mismo nombre y tiene una población de más de 140.000 habitantes, siendo la segunda más poblada del país y la primera en extensión. La catedral de la Córdoba argentina es una joya colonial y es uno de los reclamos turísticos de su importante centro histórico donde, además, se ubica la Manzana Jesuítica, declarada Patrimonio de la Humanidad por la Unesco. 8 tocayas en el mundo Málaga Washington, EEUU Nueva Jersey, EEUU Nuevo México, EEUU México Filipinas California, EEUU Colombia Argentina En el caso de Málaga, se reproduce sobre todo en norteamérica, con 4 tocayas en EEUU y 1 en México. Pero es en Colombia, en el departamento de Santander, donde tiene su réplica más grande. Con una población de algo más de 20.000 habitantes, la Málaga colombiana también tiene una catedral, la de la Inmaculada Concepción. Comparte con la Málaga original el gentilicio (malagueño, malagueña), que también sirve de nombre para una población dentro de la provincia argentina de Córdoba. 6 tocayas en el mundo Sevilla Cuba Magdalena, Colombia Filipinas Valle del Cauca, Colombia Ecuador Córdoba, Colombia De nuevo, la mayoría de las tocayas de la capital andaluza se encuentran en el centro del continente americano, con 3 repeticiones en Colombia. En el mismo departamento colombiano (Valle del Cauca) de la otra Andalucía más poblada, se encuentra también la otra Sevilla más grande (más de 40.000 habitantes). Esta Sevilla colombiana se considera la 'Capital cafetera' del país y se encuentra dentro del 'Paisaje Cultural Cafetero', declarado Patrimonio Cultural de la Humanidad por la UNESCO. 5 tocayas en el mundo Cádiz Indiana, EEUU Ohio, EEUU Kentucky, EEUU Filipinas Guinea Ecuatorial Con 3 repeticiones en EEUU (Ohio, Kentucky e Indiana) y la única de las andaluzas con réplica en el continente africano (Guinea Ecuatorial). También es la primera cuya tocaya más grande no se encuentra en América, sino al otro lado del charco: Filipinas. Cadiz City es una gran ciudad de más de 130.000 habitantes dentro de la provincia filipina de Negros Occidental. Su principal motor económico es la producción de azúcar. 2 tocayas en el mundo Jaén Filipinas Perú El Pacífico separa las dos réplicas de Jaén en el mundo. Una ubicada en Perú y, la otra, en Filipinas. Es esta última la de mayor población (más de 60.000 habitantes). Se encuentra en una provincia filipina cuyo nombre también es familiar, Nueva Écija. 1 tocaya en el mundo Almería Filipinas Casi exclusivo de Andalucía es el nombre de Almería. Sólo una réplica se encuentra en el mundo: de nuevo, en Filipinas. La Almería filipina es una ciudad pequeña de la provincia de Biliran. 0 tocayas en el mundo Huelva Única e irrepetible. La ironía de la historia nos muestra que la ciudad más cercana al puerto de salida hacia las Indias de Cristóbal Colón no tiene réplica en el mundo. La única Huelva que existe en la Tierra es la andaluza. Fuente y metodología: 'World Cities Database', MaxMind. Con 3.047.000 registros de poblaciones con datos de su toponimia y de su geolocalización (latitud y longitud). Para este reportaje se han excluido todos los datos que se ubican en zonas repetidas, con casas muy diseminadas, despobladas o entornos naturales."
]
fuentemodelo = " ".join(fuente)
# Definir la personalidad y el comportamiento del chatbot
system_instruction = (
    "Eres un chatbot especializado del periódico 'SUR', de Málaga."
    "Tu objetivo es responder preguntas **únicamente** basándote en la información proporcionada a continuación."
    "Si la pregunta no puede ser respondida con esa información, debes decir cortésmente que no tienes la información."
    "No quiero que seas creativo ni que alucines. Si la respuesta no se puede encontrar en la información, debes decir cortésmente que no tienes la respuesta."
    "Si el usuario se desvía del objetivo de este chat bot, preguntas sobre la información proporcionada a continuación, debes pedir cortésmente al usuario que pregunte sobre el tema."
)
# Configuración del modelo
config = types.GenerateContentConfig (
    system_instruction=system_instruction
)
# Tipo de modelo usado, apto para chatbots
model = 'gemini-2.5-flash'

# Crear la ruta de la API
# api_chatbot.py (Continuación)
# Esta ruta recibirá la pregunta del frontend
@app.route('/chat', methods=['POST'])
def chat():
    # 1. Recibe la pregunta del usuario desde el frontend
    datos = request.get_json()
    pregunta_usuario = datos.get('pregunta', '')

    if not pregunta_usuario:
        return jsonify({"respuesta": "Por favor, proporciona una pregunta."}), 400

    # 2. Crea el prompt combinado (RAG)
    prompt_completo = (
        f"Contexto/Fuentes: {fuentemodelo}\n\n"
        f"Pregunta: {pregunta_usuario}"
    )

    # 3. Llama a la API de Gemini (dentro de try/except)
    try:
        response = client.models.generate_content(
            model=model,
            contents=prompt_completo,
            config=config
        )
        
        # 4. Devuelve la respuesta a tu frontend como JSON
        return jsonify({"respuesta": response.text})

    except Exception as e:
        # Manejo de errores
        print(f"Error de API: {e}")
        return jsonify({"respuesta": "Lo siento, hubo un error interno del servidor."}), 500
    
# api_chatbot.py (Final)

if __name__ == '__main__':
    # Para desarrollo, se ejecuta en http://127.0.0.1:5000/
    # En producción necesitarás un servidor web (como Gunicorn o Nginx)
    app.run(debug=True)

