from clases import Dueno, Mascota, Consulta
import logging
import json
import csv

logging.basicConfig(
    filename='log/clinica_veterinaria.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


class SistemaVeterinario:
    def __init__(self):
        self.mascotas = []
        self.duenos = []
        self.consultas = []
        logging.info("Sistema Veterinario iniciado.")
        self.cargar_datos()  # 🧠 Esto carga los datos al iniciar

    def cargar_datos(self):
        logging.info("Cargando datos del sistema...")
        # Cargar datos de los archivos JSON
        try:
            with open('data/duenos.json', 'r', encoding='utf-8') as f:
                self.duenos = [
                    Dueno.from_dict(data) for data in json.load(f)
                ]
            with open('data/mascotas.json', 'r', encoding='utf-8') as f:
                self.mascotas = [
                    Mascota.from_dict(data, self.duenos)
                    for data in json.load(f)
                ]
            logging.info("Datos cargados exitosamente.")
        except FileNotFoundError:
            logging.warning(
                "Archivos de datos no encontrados. Iniciando vacío."
            )
        except json.JSONDecodeError as e:
            logging.error(f"Error al cargar datos: {e}")

    def guardar_datos(self):
        try:
            logging.info("Guardando datos del sistema...")

            with open("data/duenos.json", "w", encoding="utf-8") as f:
                json.dump(
                    [dueno.to_dict() for dueno in self.duenos],
                    f,
                    indent=4
                )

            with open("data/mascotas.json", "w", encoding="utf-8") as f:
                json.dump(
                    [mascota.to_dict() for mascota in self.mascotas],
                    f,
                    indent=4
                )

            with open("data/consultas.json", "w", encoding="utf-8") as f:
                json.dump(
                    [consulta.to_dict() for consulta in self.consultas],
                    f,
                    indent=4
                )

            print("📦 Se ha guardado toda la información en JSON.")

        except Exception as e:
            logging.error(f"Error al guardar datos: {e}")

    def exportar_csv(self):
        logging.info("Exportando datos a CSV...")
        # Exportar datos a CSV
        try:
            with open(
                'data/mascotas.csv', 'w', newline='', encoding='utf-8'
            ) as f:
                writer = csv.writer(f)
                writer.writerow([
                    "Nombre", "Especie", "Raza", "Edad", "Peso",
                    "Motivo", "Dueño"
                ])
                for mascota in self.mascotas:
                    writer.writerow([
                        mascota.nombre, mascota.especie, mascota.raza,
                        mascota.edad, mascota.peso, mascota.motivo,
                        mascota.dueno.nombre
                    ])
            logging.info("Datos exportados a CSV exitosamente.")
        except Exception as e:
            print(f"Error al exportar a CSV: {e}")
            logging.error(f"Error al exportar a CSV: {e}")

    def registrar_paciente_completo(self):

        print("\n🐾 Inicio de registro 🐾")

        print("\n👤 Datos del humano a cargo:")
        nombre = input("Nombre completo: ").strip()
        documento = input("Número de documento: ").strip()
        correo = input("Correo electrónico: ").strip()
        telefono = input("Celular: ").strip()

        if not nombre or not documento or not correo or not telefono:
            print("⚠️ Todos los campos del dueño son obligatorios.")
            return

        # 🔍 Validar documento duplicado
        for dueno in self.duenos:
            if dueno.documento == documento:
                print(
                    (
                        f"🚫 Ya existe un dueño registrado con el documento "
                        f"'{documento}'.\n"
                        "💡 Si es un error, por favor verifica los datos."
                    )
                )
                return

        dueno = Dueno(nombre, documento, correo, telefono)
        self.duenos.append(dueno)

        print("\n🐶 Datos de la mascota:")
        nombre_mascota = input("Nombre: ").strip()
        especie = input("Especie: ").strip()
        raza = input("Raza: ").strip()
        edad = input("Edad: ").strip()
        peso = input("Peso: ").strip()
        motivo = input("Motivo de registro: ").strip()

        # 🔁 Validar si el dueño ya tiene una mascota con el mismo nombre
        for mascota_existente in self.mascotas:
            if (
                mascota_existente.nombre.lower() == nombre_mascota.lower()
                and mascota_existente.dueno.documento == documento
            ):
                print(
                    f"⚠️ Ya tienes una mascota registrada con el nombre "
                    f"'{nombre_mascota}'.\n"
                    "💡 Si es otra mascota, por favor usa un apodo o "
                    "añade una distinción."
                )
                return

        if (
            not nombre_mascota or not especie or not raza or
            not edad or not peso or not motivo
        ):
            print("⚠️ Todos los campos de la mascota son obligatorios.")
            return

        mascota = Mascota(
            nombre_mascota, especie, raza, edad, peso, motivo, documento
        )

        self.mascotas.append(mascota)

        print(
            f"✅ ¡Paciente {nombre_mascota} registrado exitosamente "
            f"con su humano {nombre}! 🐕‍🦺💙"
        )
        logging.info(f"Paciente registrado: {nombre_mascota}, dueño: {nombre}")

        self.guardar_datos()
        print("📦 Se ha guardado toda la información en JSON.")

    def registrar_consulta(self):
        if not self.mascotas:
            print("😕 Aún no hay mascotas registradas. Registra al menos una.")
            return

        print("\n📋 Por favor selecciona la mascota a la que deseas registrar:")
        for i, mascota in enumerate(self.mascotas, 1):
            print(f"{i}. {mascota.nombre} ({mascota.especie})")

        try:
            op = int(input("🔢 Ingresa el número correspondiente: ")) - 1
            if op < 0 or op >= len(self.mascotas):
                raise IndexError("Número fuera de rango.")
            mascota = self.mascotas[op]
        except ValueError:
            print("❌ Ups, eso no parece un número válido. Intenta de nuevo.")
            return
        except IndexError:
            print(
                "❌ El número que ingresaste no corresponde a ninguna mascota."
            )
            return

        print(f"\n✍️ Registrando consulta para {mascota.nombre}:")
        fecha = input("📅 Fecha (dd/mm/aaaa): ").strip()
        motivo = input("🩺 Motivo de la consulta: ").strip()
        diagnostico = input("🧾 Diagnóstico: ").strip()

        if not fecha or not motivo or not diagnostico:
            print(
                "⚠️ Todos los campos son obligatorios para "
                "registrar la consulta."
            )
            return

        consulta = Consulta(fecha, motivo, diagnostico, mascota)
        mascota.agregar_consulta(consulta)
        self.consultas.append(consulta)

        print(f"✅ ¡Consulta registrada exitosamente para {mascota.nombre}! 💙")
        logging.info(f"Consulta registrada para: {mascota.nombre}")

    def listar_mascotas(self):
        print("\n🐶 Mascotas registradas:")
        if not self.mascotas:
            print("No hay mascotas.")
            return

        for mascota in self.mascotas:
            print(mascota)

    def ver_historial(self):

        if not self.mascotas:
            print("🐾 Aún no tienes pacientes registrados.")
            return

        print("\n📋 Selecciona la mascota para ver su historial:")
        for i, mascota in enumerate(self.mascotas, 1):
            print(f"{i}. {mascota.nombre} ({mascota.especie})")

        try:
            op = int(input("🔢 Ingresa el número correspondiente: ")) - 1
            if op < 0 or op >= len(self.mascotas):
                raise ValueError(
                    "Número de mascota fuera de rango o inválido."
                )
            mascota = self.mascotas[op]
        except ValueError as e:
            print(f"❌ {e}. Intenta nuevamente con un número válido.")
            return

        print(f"\n📋 Historial de {mascota.nombre}:")
        if not mascota.consultas:
            print("ℹ️ Aún no hay consultas registradas para esta mascota.")
        else:
            for consulta in mascota.consultas:
                print(consulta)

    def guardar_consultas_json(self):
        try:
            with open('data/consultas.json', 'w') as f:
                json.dump(
                    [consulta.to_dict() for consulta in self.consultas],
                    f,
                    indent=4
                )
            logging.info("Consultas guardadas exitosamente en JSON.")
        except Exception as e:
            logging.error(f"Error al guardar consultas en JSON: {e}")
