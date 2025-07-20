import sqlite3
import logging

DB_NAME = 'veterinaria.db'

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def conectar():
    try:
        conn = sqlite3.connect(DB_NAME)
        logging.info("🗄️ Conectado a la base de datos SQLite.")
        return conn
    except sqlite3.Error as e:
        logging.error(f"❌ Error al conectar a la base de datos: {e}")
        return None


def crear_tablas():
    conn = conectar()
    if conn:
        cursor = conn.cursor()

        try:
            # Tabla dueños
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS duenos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    documento TEXT UNIQUE NOT NULL,
                    correo TEXT,
                    telefono TEXT
                );
            """)

            # Tabla mascotas
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS mascotas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    especie TEXT,
                    raza TEXT,
                    edad INTEGER,
                    peso REAL,
                    motivo TEXT,
                    documento_dueno TEXT,
                    FOREIGN KEY (documento_dueno) REFERENCES duenos(documento)
                );
            """)

            # Tabla consultas
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS consultas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    fecha TEXT NOT NULL,
                    motivo TEXT,
                    diagnostico TEXT,
                    tratamiento TEXT,
                    documento_mascota TEXT
                );
            """)

            conn.commit()
            logging.info(
                "📦 Tablas con compatibilidad de documento "
                "creadas correctamente."
            )
        except sqlite3.Error as e:
            logging.error(f"❌ Error al crear tablas: {e}")
        finally:
            conn.close()
            logging.info("🔌 Conexión cerrada.")


def insertar_dueno(nombre, documento, correo, telefono):
    conn = conectar()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO duenos (nombre, documento, correo, telefono)
                VALUES (?, ?, ?, ?)
            ''', (nombre, documento, correo, telefono))
            conn.commit()
            logging.info(f"✅ Dueño insertado: {nombre} ({documento})")
        except sqlite3.IntegrityError:
            logging.warning(f"⚠️ Documento duplicado: {documento}")
        except sqlite3.Error as e:
            logging.error(f"❌ Error al insertar dueño: {e}")
        finally:
            conn.close()
            logging.info("🔌 Conexión cerrada tras insertar dueño.")


def insertar_mascota(nombre, especie, raza, edad, peso, motivo, id_dueno):
    conn = conectar()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute(
                '''
                INSERT INTO mascotas (
                    nombre, especie, raza, edad, peso, motivo, id_dueno
                )
                VALUES (?, ?, ?, ?, ?, ?, ?)
                ''',
                (nombre, especie, raza, edad, peso, motivo, id_dueno)
            )
            conn.commit()
            logging.info(f"✅ Mascota insertada: {nombre} (ID: {id_dueno})")
        except sqlite3.Error as e:
            logging.error(f"❌ Error al insertar mascota: {e}")
        finally:
            conn.close()
            logging.info("🔌 Conexión cerrada tras insertar mascota.")


def insertar_consulta(fecha, motivo, diagnostico, tratamiento, id_mascota):
    conn = conectar()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute(
                '''
                INSERT INTO consultas (
                    fecha, motivo, diagnostico, tratamiento, id_mascota
                )
                VALUES (?, ?, ?, ?, ?)
                ''',
                (fecha, motivo, diagnostico, tratamiento, id_mascota)
            )
            conn.commit()
            logging.info(
                f"✅ Consulta registrada para mascota ID: {id_mascota}"
            )
        except sqlite3.Error as e:
            logging.error(f"❌ Error al insertar consulta: {e}")
        finally:
            conn.close()
            logging.info("🔌 Conexión cerrada tras insertar consulta.")
