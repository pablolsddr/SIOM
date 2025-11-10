from psycopg2 import sql
from conneccion_db import ConexionDB

# --------------------------------------------
# Esquemas
# --------------------------------------------
def crear_esquemas(cursor):
    for esquema in ["dimensiones", "hechos"]:
        cursor.execute(
            sql.SQL("CREATE SCHEMA IF NOT EXISTS {}").format(sql.Identifier(esquema))
        )
    print(" Esquemas creados/verificados")
    print("se crearon los esquemas dimensiones, hechos")



def crear_tablas_dimensiones(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS dimensiones.empresa (
            id_empresa      INTEGER PRIMARY KEY,
            nombre_empresa  VARCHAR(255) NOT NULL
            nombre_dueño    VARCHAR(255) NOT NULL,
            direccion       VARCHAR(255) NOT NULL,
            numero_telefono   VARCHAR(50) NOT NULL
        );
    """)
    # cursor.execute("""
    #     CREATE TABLE IF NOT EXISTS dimensiones.xxxxx (
    #         xxxxxx     INTEGER PRIMARY KEY,
    #         xxxxxx VARCHAR(255) NOT NULL
    #     );
    # """)

def crear_tablas_facturas(cursor):
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS hechos.facturas (
                id                       BIGSERIAL PRIMARY KEY,
                rut_empresa              INTEGER NOT NULL,           -- FK -> dimensiones.empresa(id_empresa)
                dirección                VARCHAR(255) NOT NULL,           
                algo1                    INTEGER NOT NULL,           
                algo2                    INTEGER NOT NULL,           
                algo3                    INTEGER NOT NULL,          
                algo4                    VARCHAR NOT NULL,           
                valor_inversion          NUMERIC(18,2) NOT NULL,     -- VALOR_INVERSION

                CONSTRAINT fk_facturas_empresa
                    FOREIGN KEY (rut_empresa) REFERENCES dimensiones.empresa (id_empresa),

    );
""")


        print("✅ Hecho facturas creado/verificado")
    except Exception as e:
        print(f"❌ Error creando hechos.facturas: {e}")
        raise


# --------------------------------------------
#. Crearción de tablas
# --------------------------------------------
def create_tables_dimensiones_y_esquemas():
    print("🚀 Iniciando creación de base de datos…")
    db = ConexionDB()
    conn = db.get_connection()
    cursor = conn.cursor()

    if not conn:
        print("Abortado por error de conexión")
        return
    
    try:
        print("\nCreando esquemas…")
        crear_esquemas(cursor)

        print("\nCreando tablas de dimensiones…")
        crear_tablas_dimensiones(cursor)
        conn.commit()

        print("\nCreando tablas de hechos…")
        crear_tablas_facturas(cursor)
        conn.commit()

        print("\nProceso completado")
    except Exception as e:
        print(f"\n❌ Error durante el proceso: {e}")
        conn.rollback()
        print("↩ROLLBACK aplicado")



if __name__ == "__main__":
    create_tables_dimensiones_y_esquemas()


