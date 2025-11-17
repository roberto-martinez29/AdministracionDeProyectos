# Equipo 3 - Deportes - Seguimiento de Juegos
Este módulo implementa la sección **“Seguimiento del juego”** del apartado **Deportes** dentro del proyecto Campus Virtual.

Permite:

- Mostrar una lista de juegos del campus.

- Ver el detalle en tiempo real de un juego seleccionado.

- Actualizar manualmente los datos del partido.

- Manejar los estados del partido: PROGRAMADO, EN_JUEGO, FINALIZADO.

## Funcionalidad implementada
**Lista de juegos**

Se obtiene mediante:
```bash
GET /equipo3/juegos
```

Incluye:

- Deporte

- Equipos

- Fecha/hora

- Estado actual

**Seguimiento del juego**

Mediante:
```bash
GET /equipo3/juegos/{game_id}
```

Incluye:

- Equipos

- Marcador

- Estado del partido

- Periodo actual

- Tiempo restante

- Ubicación

Cuando el partido está PROGRAMADO, se muestra un mensaje especial indicando que aún no inicia.

## Integración Frontend
**Rutas:**

- /equipo3 → Menú principal del módulo del Equipo 3

- /equipo3/seguimiento → Seguimiento de juegos

**Componentes:**

Equipo3Home → Menú del módulo

HolaEquipo3Component → Seguimiento del juego

**Servicio Angular:**

- Equipo3Service:

- getGames()

- getGameDetail(id)

- getSeguimientoDemo()

## Cómo correr este módulo
**Backend (FastAPI)**
```bash
cd Backend/CampusVirtual
fastapi dev
```

**Frontend (Angular)**
```bash
cd FrontEnd/CampusVirtual
ng serve -o
```