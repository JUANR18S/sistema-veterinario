from db.db_manager import consultar_consultas_sqlite
from db.db_manager import actualizar_dueno
from db.db_manager import actualizar_mascota_sqlite
from db.db_manager import actualizar_consulta_sqlite
from db.db_manager import eliminar_dueno_sqlite
from db.db_manager import eliminar_mascota_sqlite
from db.db_manager import eliminar_consulta_sqlite
from sistema_vet import SistemaVeterinario
from db.db_manager import (
    crear_tablas,
    insertar_dueno,
    insertar_mascota,
    insertar_consulta,
    consultar_duenos_sqlite,
    consultar_mascotas_sqlite
)

import logging


def main():
    sistema = SistemaVeterinario()
    sistema.cargar_datos()

    while True:
        print("\n===== 🏥 Sistema Veterinario =====")
        print("1. Registrar paciente completo (JSON)")
        print("2. Registrar consulta (JSON)")
        print("3. Listar mascotas")
        print("4. Ver historial")
        print("5. Insertar dueño (SQLite)")
        print("6. Insertar mascota (SQLite)")
        print("7. Insertar consulta (SQLite)")
        print("8. Consultar dueños (SQLite)")
        print("9. Consultar mascotas (SQLite)")
        print("10. Consultar consultas (SQLite)")
        print("11. Actualizar dueño (SQLite)")
        print("12. Actualizar mascota (SQLite)")
        print("13. Actualizar consulta (SQLite)")
        print("14. Eliminar dueño (SQLite)")
        print("15. Eliminar mascota (SQLite)")
        print("16. Eliminar consulta (SQLite)")
        print("17. Salir")

        opcion = input("🔢 Seleccione una opción (1-17): ").strip()

        try:
            if opcion == "1":
                sistema.registrar_paciente_completo()
            elif opcion == "2":
                sistema.registrar_consulta()
            elif opcion == "3":
                sistema.listar_mascotas()
            elif opcion == "4":
                sistema.ver_historial()
            elif opcion == "5":
                nombre = input("Nombre del dueño: ")
                documento = input("Documento: ")
                correo = input("Correo: ")
                telefono = input("Teléfono: ")
                insertar_dueno(nombre, documento, correo, telefono)
            elif opcion == "6":
                nombre = input("Nombre de la mascota: ")
                especie = input("Especie: ")
                raza = input("Raza: ")
                edad = int(input("Edad: "))
                peso = float(input("Peso: "))
                motivo = input("Motivo: ")
                id_dueno = input("ID del dueño (documento): ")
                insertar_mascota(
                    nombre,
                    especie,
                    raza,
                    edad,
                    peso,
                    motivo,
                    id_dueno
                )
            elif opcion == "7":
                fecha = input("Fecha (YYYY-MM-DD): ")
                motivo = input("Motivo: ")
                diagnostico = input("Diagnóstico: ")
                tratamiento = input("Tratamiento: ")
                id_mascota = input("ID de la mascota: ")
                insertar_consulta(
                    fecha,
                    motivo,
                    diagnostico,
                    tratamiento,
                    id_mascota
                )
            elif opcion == "8":
                consultar_duenos_sqlite()
            elif opcion == "9":
                consultar_mascotas_sqlite()
            elif opcion == "10":
                consultar_consultas_sqlite()
            elif opcion == "11":
                actualizar_dueno()
            elif opcion == "12":
                actualizar_mascota_sqlite()
            elif opcion == "13":
                actualizar_consulta_sqlite()
            elif opcion == "14":
                eliminar_dueno_sqlite()
            elif opcion == "15":
                eliminar_mascota_sqlite()
            elif opcion == "16":
                eliminar_consulta_sqlite()
            elif opcion == "17":
                sistema.guardar_datos()
                print("\n✅ Datos guardados exitosamente (JSON).")
                print("👋 Saliendo del sistema... ¡Hasta luego!")
                break
            else:
                raise ValueError("Opción fuera del menú.")
        except Exception as e:
            print(f"❌ Error: {e}\n💡 Intenta con una opción válida "
                  "entre 1 y 13.")


if __name__ == "__main__":
    crear_tablas()
    logging.info("Sistema Veterinario iniciado correctamente.")
    main()
    logging.info("Sistema Veterinario finalizado.")
