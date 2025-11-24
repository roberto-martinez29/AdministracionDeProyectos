from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware #Por si se necesita CORS en el futuro y para pruebas locales
#Imports Equipo 1
from Modules.Equipo1.Routes.equipo1_router import router as equipo1_router
#Imports Equipo 2
from Modules.Equipo2.routes.equipo2_routes import equipo2_router, populate_database_if_empty
from Modules.Equipo2.models.database import create_db_and_tables_equipo2
#Imports Equipo 3
# Imports Equipo 3
from Modules.Equipo3.Routes.equipo3_routes import equipo3_router
from Modules.Equipo3.Seguimiento_Juegos.seguimiento_juegos import seguimiento_router
from Modules.Equipo3.Calendario.eventos import router as calendario_router
from Modules.Equipo3.Registro_equipos.registro_routes import registro_router
from Modules.Equipo3.Registro_equipos.database import create_db_and_tables as db3
#Imports Equipo 4
from Modules.Equipo4.models.database import create_db_and_tables_equipo4
from Modules.Equipo3.Calendario.eventos import router as calendario_router

app = FastAPI()

# Configuración de CORS (Cross-Origin Resource Sharing)
origins = [
    "http://localhost:4200", 
    "http://localhost",
    "http://127.0.0.1:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"], 
)
#fin Configuración CORS


@app.on_event("startup")
def on_startup() -> None:
#    create_db_and_tables_equipo4() ---Comentado temporalmente debido a fallas en su implementación
    #Funcion para equipo2
    create_db_and_tables_equipo2()
    populate_database_if_empty()
    #Funcion para equipo 3
    db3()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    equipo1_router,
    prefix="/api/equipo1",
    tags=["Equipo 1 - Items"],
)

app.include_router(
    calendario_router,
    prefix="/api/calendario",   
    tags=["Equipo 3 - Calendario"],
)
    
app.include_router(
    seguimiento_router,
    prefix="/api",
    tags=["Equipo 3 - Deportes y seguimiento de juegos"],
)

app.include_router(
    registro_router,
    prefix="/api/registro",
    tags=["Equipo 3 - Registro de participantes"],
)
