# SIOM
Este GIT es para el proyecto semestral del curso TIC's 2
Profesor: Leandro LLanza
Alumnos: Joaquín Osses, Kevin Cabrera y Pablo Lores 


1. Levantar los Servicios
Ejecuta el siguiente comando para levantar los servicios de PostgreSQL y Metabase:

    ```bash
    docker-compose up -d
    ```

2. Levantar conexión DB
Crea la conexión con la base de datos:

    ```bash
    python3 coneccion_db.py
    ```


3. Levantar conexión DB
Levanta los esquemas de la base de datos :

    ```bash
    python3 db_siom.py
    ```