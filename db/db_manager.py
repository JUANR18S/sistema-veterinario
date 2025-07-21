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


def consultar_duenos_sqlite():
    try:
        conexion = sqlite3.connect(DB_NAME)
        cursor = conexion.cursor()

        cursor.execute("SELECT id, nombre, telefono, direccion FROM duenos")
        duenos = cursor.fetchall()

        if not duenos:
            print("⚠️ No hay dueños registrados en la base de datos.")
        else:
            print("\n📋 Lista de Dueños Registrados:\n")
            for d in duenos:
                print(f"🆔 ID: {d[0]}")
                print(f"👤 Nombre: {d[1]}")
                print(f"📞 Teléfono: {d[2]}")
                print(f"🏠 Dirección: {d[3]}")
                print("-" * 30)

        conexion.close()
        logging.info("Consulta de dueños realizada correctamente.")

    except sqlite3.Error as e:
        logging.error(f"Error al consultar dueños: {e}")
        print("❌ Error al consultar dueños.")


def consultar_mascotas_sqlite():
    try:
        conexion = sqlite3.connect(DB_NAME)
        cursor = conexion.cursor()

        cursor.execute(
            "SELECT id, nombre, especie, raza, edad, peso, motivo, "
            "id_dueno FROM mascotas"
        )
        mascotas = cursor.fetchall()

        if not mascotas:
            print("⚠️ No hay mascotas registradas en la base de datos.")
        else:
            print("\n📋 Lista de Mascotas Registradas:\n")
            for m in mascotas:
                print(f"🆔 ID: {m[0]}")
                print(f"🐾 Nombre: {m[1]}")
                print(f"🌍 Especie: {m[2]}")
                print(f"🐶 Raza: {m[3]}")
                print(f"📅 Edad: {m[4]}")
                print(f"⚖️ Peso: {m[5]}")
                print(f"📝 Motivo: {m[6]}")
                print(f"👤 ID Dueño: {m[7]}")
                print("-" * 30)

        conexion.close()
        logging.info("Consulta de mascotas realizada correctamente.")
    except sqlite3.Error as e:
        logging.error(f"Error al consultar mascotas: {e}")
        print("❌ Error al consultar mascotas.")


def consultar_consultas_sqlite():
    try:
        conexion = sqlite3.connect(DB_NAME)
        cursor = conexion.cursor()

        cursor.execute(
            "SELECT id, fecha, motivo, diagnostico, tratamiento, "
            "id_mascota FROM consultas"
        )
        consultas = cursor.fetchall()

        if not consultas:
            print("⚠️ No hay consultas médicas registradas.")
        else:
            print("\n📋 Lista de Consultas Médicas:\n")
            for c in consultas:
                print(f"🆔 ID: {c[0]}")
                print(f"📅 Fecha: {c[1]}")
                print(f"❓ Motivo: {c[2]}")
                print(f"🩺 Diagnóstico: {c[3]}")
                print(f"💊 Tratamiento: {c[4]}")
                print(f"🐾 ID Mascota: {c[5]}")
                print("-" * 30)

        conexion.close()
        logging.info("Consulta de consultas médicas realizada correctamente.")

    except sqlite3.Error as e:
        logging.error(f"Error al consultar consultas médicas: {e}")
        print("❌ Error al consultar consultas médicas.")


def actualizar_dueno(id_dueno, nombre, telefono, direccion):
    conn = conectar()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute(
                '''
                UPDATE duenos
                SET nombre = ?, telefono = ?, direccion = ?
                WHERE id = ?
                ''',
                (nombre, telefono, direccion, id_dueno)
            )
            conn.commit()
            logging.info(f"✅ Dueño actualizado: {id_dueno}")
        except sqlite3.Error as e:
            logging.error(f"❌ Error al actualizar dueño: {e}")
        finally:
            conn.close()
            logging.info("🔌 Conexión cerrada tras actualizar dueño.")


def actualizar_mascota_sqlite():
    try:
        conexion = sqlite3.connect(DB_NAME)
        cursor = conexion.cursor()

        id_mascota = input(
            "🆔 Ingrese el ID de la mascota a actualizar: "
        ).strip()

        # Buscar mascota actual
        cursor.execute(
            "SELECT nombre, especie, raza, edad, peso, motivo, id_dueño "
            "FROM mascotas WHERE id = ?",
            (id_mascota,)
        )
        mascota = cursor.fetchone()

        if not mascota:
            print("❌ No se encontró ninguna mascota con ese ID.")
            return

        print("\n🐶 Mascota actual:")
        print(
            f"Nombre: {mascota[0]}, Especie: {mascota[1]}, "
            f"Raza: {mascota[2]}, Edad: {mascota[3]}, "
            f"Peso: {mascota[4]}, Motivo: {mascota[5]}, "
            f"ID Dueño: {mascota[6]}"
        )

        # Solicitar nuevos valores
        nombre = input(
            "Nuevo nombre (dejar vacío para no cambiar): "
        ).strip() or mascota[0]
        especie = input(
            "Nueva especie (dejar vacío para no cambiar): "
        ).strip() or mascota[1]
        raza = input(
            "Nueva raza (dejar vacío para no cambiar): "
        ).strip() or mascota[2]
        edad_input = input(
            "Nueva edad (dejar vacío para no cambiar): "
        ).strip()
        edad = int(edad_input) if edad_input else mascota[3]
        peso_input = input(
            "Nuevo peso (dejar vacío para no cambiar): "
        ).strip()
        peso = float(peso_input) if peso_input else mascota[4]
        motivo = input(
            "Nuevo motivo (dejar vacío para no cambiar): "
        ).strip() or mascota[5]
        id_dueno_input = input(
            "Nuevo ID del dueño (dejar vacío para no cambiar): "
        ).strip()
        id_dueno = int(id_dueno_input) if id_dueno_input else mascota[6]

        # Actualizar mascota
        cursor.execute(
            "UPDATE mascotas "
            "SET nombre = ?, especie = ?, raza = ?, edad = ?, peso = ?, "
            "motivo = ?, id_dueño = ? "
            "WHERE id = ?",
            (nombre, especie, raza, edad, peso, motivo, id_dueno, id_mascota)
        )

        conexion.commit()
        print("✅ Mascota actualizada correctamente.")
        logging.info(f"Mascota con ID {id_mascota} actualizada.")
        conexion.close()

    except sqlite3.Error as e:
        logging.error(f"Error al actualizar mascota: {e}")
        print("❌ Error al actualizar la mascota.")


def actualizar_consulta_sqlite():
    try:
        conexion = sqlite3.connect(DB_NAME)
        cursor = conexion.cursor()

        id_consulta = input(
            "🆔 Ingrese el ID de la consulta a actualizar: "
        ).strip()

        # Obtener consulta actual
        cursor.execute(
            """
            SELECT fecha, motivo, diagnostico, tratamiento, id_mascota
            FROM consultas WHERE id = ?
            """,
            (id_consulta,)
        )
        consulta = cursor.fetchone()

        if not consulta:
            print("❌ No se encontró ninguna consulta con ese ID.")
            return

        print("\n📋 Consulta actual:")
        print(f"Fecha: {consulta[0]}")
        print(f"Motivo: {consulta[1]}")
        print(f"Diagnóstico: {consulta[2]}")
        print(f"Tratamiento: {consulta[3]}")
        print(f"ID Mascota: {consulta[4]}")

        # Solicitar nuevos valores
        fecha = input(
            "Nueva fecha (YYYY-MM-DD, dejar vacío para mantener): "
        ).strip() or consulta[0]
        motivo = input(
            "Nuevo motivo (dejar vacío para mantener): "
        ).strip() or consulta[1]
        diagnostico = input(
            "Nuevo diagnóstico (dejar vacío para mantener): "
        ).strip() or consulta[2]
        tratamiento = input(
            "Nuevo tratamiento (dejar vacío para mantener): "
        ).strip() or consulta[3]
        id_mascota_input = input(
            "Nuevo ID de la mascota (dejar vacío para mantener): "
        ).strip()
        id_mascota = int(id_mascota_input) if id_mascota_input else consulta[4]

        # Ejecutar actualización
        cursor.execute(
            """
            UPDATE consultas
            SET fecha = ?, motivo = ?, diagnostico = ?, tratamiento = ?,
                id_mascota = ?
            WHERE id = ?
            """,
            (fecha, motivo, diagnostico, tratamiento, id_mascota, id_consulta)
        )

        conexion.commit()
        print("✅ Consulta médica actualizada correctamente.")
        logging.info(f"Consulta con ID {id_consulta} actualizada.")
        conexion.close()

    except sqlite3.Error as e:
        logging.error(f"Error al actualizar consulta: {e}")
        print("❌ Error al actualizar la consulta.")


def eliminar_dueno_sqlite():
    try:
        conexion = sqlite3.connect(DB_NAME)
        cursor = conexion.cursor()

        id_dueno = input("🆔 Ingrese el ID del dueño a eliminar: ").strip()

        # Verificar si existe
        cursor.execute("SELECT nombre FROM duenos WHERE id = ?", (id_dueno,))
        dueno = cursor.fetchone()

        if not dueno:
            print("❌ No se encontró ningún dueño con ese ID.")
            return

        # Verificar si tiene mascotas asociadas
        cursor.execute(
            "SELECT COUNT(*) FROM mascotas WHERE id_dueño = ?",
            (id_dueno,)
        )
        cantidad = cursor.fetchone()[0]

        if cantidad > 0:
            print(f"⚠️ Este dueño tiene {cantidad} mascota(s) registradas.")
            print("❌ No se puede eliminar hasta que se eliminen "
                  "o reasignen sus mascotas.")
            return

        confirmacion = input(
            f"¿Estás seguro de eliminar al dueño '{dueno[0]}'? (s/n): "
        ).strip().lower()
        if confirmacion != 's':
            print("❎ Eliminación cancelada.")
            return

        cursor.execute("DELETE FROM duenos WHERE id = ?", (id_dueno,))
        conexion.commit()
        print("✅ Dueño eliminado correctamente.")
        logging.info(f"Dueño con ID {id_dueno} eliminado.")
        conexion.close()

    except sqlite3.Error as e:
        logging.error(f"Error al eliminar dueño: {e}")
        print("❌ Error al eliminar el dueño.")


def eliminar_mascota_sqlite():
    try:
        conexion = sqlite3.connect(DB_NAME)
        cursor = conexion.cursor()

        id_mascota = input(
            "🆔 Ingrese el ID de la mascota a eliminar: "
        ).strip()

        # Verificar si existe
        cursor.execute(
            "SELECT nombre FROM mascotas WHERE id = ?", (id_mascota,)
        )
        mascota = cursor.fetchone()

        if not mascota:
            print("❌ No se encontró ninguna mascota con ese ID.")
            return

        confirmacion = input(
            f"¿Estás seguro de eliminar la mascota '{mascota[0]}'? (s/n): "
        ).strip().lower()
        if confirmacion != 's':
            print("❎ Eliminación cancelada.")
            return

        cursor.execute("DELETE FROM mascotas WHERE id = ?", (id_mascota,))
        conexion.commit()
        print("✅ Mascota eliminada correctamente.")
        logging.info(f"Mascota con ID {id_mascota} eliminada.")
        conexion.close()

    except sqlite3.Error as e:
        logging.error(f"Error al eliminar mascota: {e}")
        print("❌ Error al eliminar la mascota.")


def eliminar_consulta_sqlite():
    try:
        conexion = sqlite3.connect(DB_NAME)
        cursor = conexion.cursor()

        id_consulta = input(
            "🆔 Ingrese el ID de la consulta a eliminar: "
        ).strip()

        # Verificar si existe
        cursor.execute(
            "SELECT fecha FROM consultas WHERE id = ?", (id_consulta,)
        )
        consulta = cursor.fetchone()

        if not consulta:
            print("❌ No se encontró ninguna consulta con ese ID.")
            return

        confirmacion = input(
            (
                f"¿Estás seguro de eliminar la consulta del día "
                f"'{consulta[0]}'? (s/n): "
            )
        ).strip().lower()
        if confirmacion != 's':
            print("❎ Eliminación cancelada.")
            return

        cursor.execute("DELETE FROM consultas WHERE id = ?", (id_consulta,))
        conexion.commit()
        print("✅ Consulta eliminada correctamente.")
        logging.info(f"Consulta con ID {id_consulta} eliminada.")
        conexion.close()

    except sqlite3.Error as e:
        logging.error(f"Error al eliminar consulta: {e}")
        print("❌ Error al eliminar la consulta.")