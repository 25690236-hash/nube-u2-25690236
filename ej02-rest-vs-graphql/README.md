## Ej. 02 REST vs GraphQL medido

## Objetivo
Comparar cuantitativamente el rendimiento y consumo de recursos entre la arquitectura REST (PokéAPI v2) y GraphQL (PokéAPI Beta) al consultar información de una lista de 10 Pokémon (pikachu, charizard, bulbasaur, squirtle, gengar, eevee, snorlax, lucario, greninja, mewtwo), analizando el número de peticiones HTTP, tiempo de respuesta en milisegundos y volumen de datos transferidos en bytes.

## Resultados / mediciones

| Método | Endpoint / Servicio | Peticiones HTTP | Bytes Totales | Tiempo Total (ms) | Eficiencia de Red |
| **REST** | `https://pokeapi.co/api/v2/pokemon/{nombre}` | 10 | ~2.7 MB | ~2,850 ms | Recibe todo el objeto JSON por cada recurso (*over-fetching*). |
| **GraphQL** | `https://graphql.pokeapi.co/v1beta2` | 1 | ~1.2 KB | ~420 ms | Solicita y recibe únicamente `name`, `height` y `weight`. |