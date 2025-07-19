import unittest
import json
import os
from sistema_vet import SistemaVeterinario
from clases import Dueno, Mascota, Consulta


def crear_consulta_prueba():
    return Consulta(
        "2025-07-18",
        "Revisión",
        "Antibiótico",
        "Tommy",
        "Antibiótico"
    )


def test_creacion_consulta(self):
    consulta = crear_consulta_prueba()
    self.assertEqual(consulta.motivo, "Revisión")
    self.assertEqual(consulta.tratamiento, "Antibiótico")


class TestDueno(unittest.TestCase):
    def test_creacion_dueno(self):
        dueno = Dueno("Camilo", "123", "camilo@mail.com", "3110000000")
        self.assertEqual(dueno.nombre, "Camilo")
        self.assertEqual(dueno.documento, "123")
        self.assertEqual(dueno.correo, "camilo@mail.com")
        self.assertEqual(dueno.telefono, "3110000000")


class TestMascota(unittest.TestCase):
    def test_creacion_mascota(self):
        mascota = Mascota(
            "Max", "Perro", "Labrador", 5, 25.0, "Vacunación", "123"
        )
        self.assertEqual(mascota.nombre, "Max")
        self.assertEqual(mascota.especie, "Perro")
        self.assertEqual(mascota.peso, 25.0)
        self.assertEqual(mascota.documento_dueno, "123")


class TestConsulta(unittest.TestCase):
    def test_creacion_consulta(self):
        consulta = Consulta(
            "2025-07-18", "Revisión", "Antibiótico", "Tommy", "Antibiótico"
        )
        self.assertEqual(consulta.fecha, "2025-07-18")
        self.assertEqual(consulta.motivo, "Revisión")
        self.assertEqual(consulta.tratamiento, "Antibiótico")


class TestSerializacion(unittest.TestCase):
    def test_serializacion_dueno(self):
        dueno_original = Dueno(
            "Juan Camilo", "12345", "camilo@mail.com", "3110000000"
        )
        dueno_dict = dueno_original.to_dict()
        dueno_recuperado = Dueno.from_dict(dueno_dict)

        self.assertEqual(dueno_recuperado.nombre, dueno_original.nombre)
        self.assertEqual(dueno_recuperado.documento, dueno_original.documento)
        self.assertEqual(dueno_recuperado.correo, dueno_original.correo)
        self.assertEqual(dueno_recuperado.telefono, dueno_original.telefono)

    def test_serializacion_mascota(self):
        mascota_original = Mascota(
            "Max", "Perro", "Labrador", 4, 22.5, "Vacunación", "12345"
        )

        mascota_dict = mascota_original.to_dict()
        mascota_recuperada = Mascota.from_dict(mascota_dict, [])

        self.assertEqual(mascota_recuperada.nombre, mascota_original.nombre)
        self.assertEqual(mascota_recuperada.especie, mascota_original.especie)
        self.assertEqual(mascota_recuperada.raza, mascota_original.raza)
        self.assertEqual(mascota_recuperada.edad, mascota_original.edad)
        self.assertEqual(mascota_recuperada.peso, mascota_original.peso)
        self.assertEqual(mascota_recuperada.motivo, mascota_original.motivo)
        self.assertEqual(
            mascota_recuperada.documento_dueno,
            mascota_original.documento_dueno
        )

    def test_serializacion_consulta(self):
        consulta_original = Consulta(
            "2025-07-18",
            "Revisión",
            "Diagnóstico leve",
            "Tommy",
            "Antibiótico"
        )

        consulta_dict = consulta_original.to_dict()
        consulta_recuperada = Consulta.from_dict(consulta_dict)

        self.assertEqual(consulta_recuperada.fecha, consulta_original.fecha)
        self.assertEqual(consulta_recuperada.motivo, consulta_original.motivo)
        self.assertEqual(
            consulta_recuperada.diagnostico, consulta_original.diagnostico
        )
        self.assertEqual(
            consulta_recuperada.mascota, consulta_original.mascota
        )
        self.assertEqual(
            consulta_recuperada.tratamiento, consulta_original.tratamiento
        )


def crear_dueno_prueba():
    return Dueno("Juan Camilo", "12345", "camilo@mail.com", "3110000000")


def crear_mascota_prueba():
    return Mascota("Max", "Perro", "Labrador", 4, 22.5, "Vacunación", "12345")


class TestGuardarDatos(unittest.TestCase):

    def test_guardar_datos(self):
        sistema = SistemaVeterinario()

        # Crea un dueño, mascota y consulta de prueba
        dueno = crear_dueno_prueba()
        mascota = crear_mascota_prueba()
        consulta = crear_consulta_prueba()

        sistema.duenos.append(dueno)
        sistema.mascotas.append(mascota)
        sistema.consultas.append(consulta)

        # Guardar los datos
        sistema.guardar_datos()

        # Validar que los archivos existen
        self.assertTrue(os.path.exists("data/duenos.json"))
        self.assertTrue(os.path.exists("data/mascotas.json"))
        self.assertTrue(os.path.exists("data/consultas.json"))

        # Validar que los archivos no están vacíos
        with open("data/duenos.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            self.assertTrue(len(data) > 0)

        with open("data/mascotas.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            self.assertTrue(len(data) > 0)

        with open("data/consultas.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            self.assertTrue(len(data) > 0)


if __name__ == '__main__':
    unittest.main()
