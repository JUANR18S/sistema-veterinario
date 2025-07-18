import logging

# Configuración básica del logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Clases del sistema veterinario


class Dueno:
    def __init__(self, nombre, documento, correo, telefono):
        self.nombre = nombre
        self.documento = documento
        self.correo = correo
        self.telefono = telefono
        logging.info(f"Dueño creado: {self.nombre} ({self.documento})")

    def __str__(self):
        return f"{self.nombre} - Doc: {self.documento} - Tel: {self.telefono}"

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "documento": self.documento,
            "correo": self.correo,
            "telefono": self.telefono
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["nombre"],
            data["documento"],
            data["correo"],
            data["telefono"]
        )


class Mascota:
    def __init__(self, nombre, especie, raza, edad, peso, motivo, dueno):
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.edad = edad
        self.peso = peso
        self.motivo = motivo
        self.documento_dueno = dueno.documento
        self.consultas = []

        logging.info(
            (
                f"Mascota creada: {self.nombre} ({self.especie}) - "
                f"Dueño: {self.dueno.nombre}"
            )
        )

    def agregar_consulta(self, consulta):
        self.consultas.append(consulta)
        logging.info(f"Consulta agregada a {self.nombre}: {consulta}")

    def __str__(self):
        return (
            f"{self.nombre} ({self.especie}, {self.raza}, {self.edad} años, "
            f"{self.peso}kg) - Dueño: {self.dueno.nombre}"
        )

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "especie": self.especie,
            "raza": self.raza,
            "edad": self.edad,
            "peso": self.peso,
            "motivo": self.motivo,
            "dueno_documento": self.dueno.documento,
            "consultas": [consulta.to_dict() for consulta in self.consultas]
        }

    @classmethod
    def from_dict(cls, data, duenos):
        dueno = next(
            (d for d in duenos if d.documento == data["dueno_documento"]),
            None
        )
        mascota = cls(
            data["nombre"],
            data["especie"],
            data["raza"],
            data["edad"],
            data["peso"],
            data["motivo"],
            dueno
        )
        mascota.consultas = [Consulta.from_dict(c) for c in data["consultas"]]
        return mascota


class Consulta:
    def __init__(self, fecha, motivo, diagnostico, mascota):
        self.fecha = fecha
        self.motivo = motivo
        self.diagnostico = diagnostico
        self.mascota = mascota

    def __str__(self):
        return (
            f"📅 {self.fecha} - Motivo: {self.motivo} - "
            f"Diagnóstico: {self.diagnostico}"
        )

    def to_dict(self):
        return {
            "mascota": self.mascota.nombre,
            "fecha": self.fecha,
            "diagnostico": self.diagnostico,
            "tratamiento": self.tratamiento
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["fecha"],
            data["motivo"],
            data["diagnostico"],
            None  # El dueño ya estará conectado desde Mascota
        )
