# Ejercicio 01: APIs REST

## Tabla de resultados

| API / Endpoint | Método | Código | Tiempo (ms) | Bytes |
| :--- | :---: | :---: | :---: | :---: |
| JSONPlaceholder (Listar posts) | GET | 200 | 300 ms | 27520 B |
| JSONPlaceholder (Crear post) | POST | 201 | 341 ms | 35 B |
| PokéAPI (Pikachu) | GET | 200 | 255 ms | 300521 B |
| OpenWeatherMap (Cd. Valles) | GET | 200 | 315 ms | 108 B |
| Recurso Inexistente | GET | 404 | 205 ms | 2 B |
| Sin Clave / Clave inválida | GET | 401 | 250 ms | 108 B |

---

### Pruebas de errores simulados
Error 404 (Not Found): Se envió una solicitud al endpoint /posts/999999 dentro de JSONPlaceholder. Como el recurso no está registrado en el servidor, devolvió un estatus 404 acompañado de un objeto JSON vacío {} que ocupó únicamente 2 bytes.

Error 401 (Unauthorized): Se ejecutó una consulta a OpenWeatherMap proporcionando un token de acceso ficticio (INVALIDA). El servidor rechazó la solicitud devolviendo el código 401, indicando que las credenciales suministradas no eran correctas.

### Análisis y preguntas finales
¿Qué fragmento de la respuesta te fue útil?

De la estructura JSON devuelta por la PokéAPI, únicamente extraje el arreglo con las habilidades principales de Pikachu: ['static', 'lightning-rod'].

¿Qué proporción del payload recibido resultó prescindible?

El objeto devuelto por PokéAPI alcanzó un peso de 300,521 bytes (aprox. 300 KB) debido a la gran cantidad de atributos adicionales que incluye (sprites visuales, historial de movimientos, métricas de combate y apariciones en juegos). Dado que la cadena con las habilidades ocupa menos de 100 bytes, el desperdicio de transferencia superó el 99.9% de los datos recibidos.