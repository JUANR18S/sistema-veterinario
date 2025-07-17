from sistema_vet import SistemaVeterinario


def main():
    sistema = SistemaVeterinario()
    sistema.cargar_datos()

    while True:
        print("\n===== 🏥 Sistema Veterinario =====")
        print("1. Registrar paciente completo")
        print("2. Registrar consulta")
        print("3. Listar mascotas")
        print("4. Ver historial")
        print("5. Salir")

        opcion = input("🔢 Seleccione una opción (1-5): ").strip()

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

                sistema.guardar_datos()
                print("\n✅ Datos guardados exitosamente.")

                print("👋 Saliendo del sistema... ¡Hasta luego!")
                break
            else:
                raise ValueError("Opción fuera del menú.")
        except Exception as e:
            print(
                f"❌ Error: {e}\n💡 Intenta con una opción válida entre 1 y 5."
            )


if __name__ == "__main__":
    main()
