from sistema_vet import SistemaVeterinario


def main():
    sistema = SistemaVeterinario()

    # Mensaje de bienvenida
    while True:
        print("\n===== 🏥 Sistema Veterinario =====")
        print("1. Registrar paciente completo")
        print("2. Registrar consulta")
        print("3. Listar mascotas")
        print("4. Ver historial")
        print("5. Salir")

        opcion = input("Seleccione opción: ")

        if opcion == "1":
            sistema.registrar_paciente_completo()
        elif opcion == "2":
            sistema.registrar_consulta()
        elif opcion == "3":
            sistema.listar_mascotas()
        elif opcion == "4":
            sistema.ver_historial()
        elif opcion == "5":
            print("👋 Saliendo del sistema...")
            break
        else:
            print("❌ Opción no válida")


if __name__ == "__main__":
    main()