from clases import Dueno, Mascota, Consulta
import logging

logging.basicConfig(
    filename='clinica_veterinaria.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


class SistemaVeterinario:
    def __init__(self):
        self.mascotas = []
        self.duenos = []

    def registrar_paciente_completo(self):
        print("\n🐾 Registro completo de paciente 🐾")

        print("\n👤 Datos del humano a cargo:")
        nombre = input("Nombre completo: ").strip()
        documento = input("Número de documento: ").strip()
        correo = input("Correo electrónico: ").strip()
        telefono = input("Celular: ").strip()

        if not nombre or not documento or not correo or not telefono:
            print("❌ Todos los campos del dueño son obligatorios.")
            return

        dueno = Dueno(nombre, documento, correo, telefono)
        self.duenos.append(dueno)

        print("\n🐶 Datos de la mascota:")
        nombre_mascota = input("Nombre: ").strip()
        especie = input("Especie: ").strip()
        raza = input("Raza: ").strip()

        try:
            edad = int(input("Edad (en años): ").strip())
            if edad < 0:
                print("❌ La edad no puede ser negativa.")
                return
        except ValueError:
            print("❌ Ingresa un número válido.")
            return

        try:
            peso = float(input("Peso (en kg): ").strip())
            if peso <= 0:
                print("❌ El peso debe ser mayor que cero.")
                return
        except ValueError:
            print("❌ Peso inválido. Debe ser un número.")
            return

        motivo = input("Motivo de consulta: ").strip()

        if not nombre_mascota or not especie or not raza or not motivo:
            print("❌ Todos los campos de la mascota son obligatorios.")
            return

        mascota = Mascota(
            nombre_mascota, especie, raza, edad, peso, motivo, dueno
        )
        self.mascotas.append(mascota)

        logging.info(
            f"Mascota registrada: {mascota.nombre} ({mascota.especie}) "
            f"- Dueño: {dueno.nombre}"
        )
        print("\n✅ Paciente registrado correctamente.")

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
