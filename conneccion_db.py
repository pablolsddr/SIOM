import os
import psycopg2
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo env
load_dotenv('.env')

class ConexionDB():
    _instance = None
    _connection = None

    def __new__(cls):
        if cls._instance is None:  
            cls._instance = super().__new__(cls)
            cls._instance._connection = cls._instance.connect_to_db()
        return cls._instance
    


    def connect_to_db(self):
        try:
            connection = psycopg2.connect(
                host=os.getenv('POSTGRES_HOST'),
                port=os.getenv('POSTGRES_PORT'),
                database=os.getenv('POSTGRES_DB'),
                user=os.getenv('POSTGRES_USER'),
                password=os.getenv('POSTGRES_PASSWORD')
            )
            print("Conexión exitosa a la base de datos")
            return connection
        except Exception as e:
            print(f"Error al conectar a la base de datos: {e}")
            return None
        


    def get_connection(self):
        return self._connection
    


    def close_connection(self):
        if self._connection:
            self._connection.close()
            print("Conexión a la base de datos cerrada")

if __name__ == "__main__":
    print("=== Probando conexión a PostgreSQL ===\n")
    
    # Crear instancia (Singleton)
    db1 = ConexionDB()
    
    # Verificar si la conexión fue exitosa
    conn = db1.get_connection()
    
    if conn:
        print("\n✓ Conexión obtenida correctamente")
        
        # Probar una query simple
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT version();")
            version = cursor.fetchone()
            print(f"\n✓ Versión de PostgreSQL: {version[0]}")
            
            cursor.execute("SELECT current_database();")
            db_name = cursor.fetchone()
            print(f"✓ Base de datos actual: {db_name[0]}")
            
            cursor.close()
        except Exception as e:
            print(f"\n✗ Error al ejecutar query: {e}")
        
        # Probar que es Singleton
        print("\n=== Probando patrón Singleton ===")
        db2 = ConexionDB()
        print(f"¿db1 y db2 son la misma instancia? {db1 is db2}")
        print(f"ID de db1: {id(db1)}")
        print(f"ID de db2: {id(db2)}")
        
        # Cerrar conexión
        db1.close_connection()
    else:
        print("\n✗ No se pudo establecer la conexión")
        print("\nVerifica:")
        print("1. Que el archivo 'env' exista en el mismo directorio")
        print("2. Que las variables estén correctamente definidas")
        print("3. Que PostgreSQL esté corriendo")
        print("4. Que las credenciales sean correctas")




