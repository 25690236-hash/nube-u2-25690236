## Ej. 01 Consumir APIs REST públicas
## Objetivo
Demostrar la capacidad de consumir servicios Web REST externos utilizando Python y la librería requests, implementando peticiones con métodos HTTP GET y POST, manejo seguro de llaves de API mediante variables de entorno (.env), provocación/inspección de errores HTTP (404 y 401), y la medición sistemática de métricas clave de desempeño (código de estado, tiempo en ms y tamaño en bytes).
## Cómo ejecutarlo
Asegúrate de instalar las dependencias necesarias:
pip install requests python-dotenv

## Crea el archivo .env en la raíz de esta carpeta con tu clave de API:
OPENWEATHER_API_KEY=tu_api_key_aqui

## Ejecuta el script de pruebas:
python ej01-api-rest.py


## Resultados / mediciones

| Servicio / Prueba | Método | URL | Código HTTP | Tiempo (ms) | Tamaño (Bytes) |
| :--- | :---: | :--- | :---: | :---: | :---: |
| **JSONPlaceholder (Listar)** | `GET` | `https://jsonplaceholder.typicode.com/posts` | `200 OK` | ~210 ms | ~27,520 B |
| **JSONPlaceholder (Crear)** | `POST` | `https://jsonplaceholder.typicode.com/posts` | `201 Created` | ~180 ms | ~65 B |
| **PokéAPI (Pikachu)** | `GET` | `https://pokeapi.co/api/v2/pokemon/pikachu` | `200 OK` | ~340 ms | ~268,400 B |
| **OpenWeatherMap (Clima)** | `GET` | `https://api.openweathermap.org/data/2.5/weather` | `200 OK` | ~190 ms | ~480 B |
| **Error 404 Provocado** | `GET` | `https://jsonplaceholder.typicode.com/posts/999999` | `404 Not Found` | ~150 ms | ~2 B |
| **Error 401 Provocado** | `GET` | `https://api.openweathermap.org/data/2.5/weather` | `401 Unauthorized` | ~120 ms | ~108 B |