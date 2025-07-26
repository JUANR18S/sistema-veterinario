🏥 Sprint 6 – Validaciones y experiencia de usuario
==================================================

🎯 Objetivo general:
Fortalecer la robustez y usabilidad del sistema veterinario mediante validaciones, control de errores y mensajes empáticos.

📋 Check list de tareas implementadas:

✅ 1. Validar selección de mascota al registrar consulta
    - try/except para evitar errores al ingresar número
    - mensajes claros si el número no es válido

✅ 2. Validar documento de dueño único
    - Previene registros duplicados
    - Mensaje empático si ya existe

✅ 3. Validar nombre único de mascota por dueño
    - Evita duplicidad por nombre
    - Sugiere usar apodo si es necesario

✅ 4. Mejorar mensajes del sistema
    - Se revisaron mensajes de error y validación
    - Se usó tono humano, útil y empático

✅ 5. Manejo de errores en menú principal
    - try/except en `main.py` para evitar caídas
    - Informa con ternura si el usuario se equivoca

💾 Archivos usados:
- clases.py
- sistema_vet.py
- main.py
- clinica_veterinaria.log (se genera automáticamente)

✨ Resultado:
Sistema más estable, amigable y resistente a errores del usuario.

👣 Próximo Sprint sugerido:
Agregar persistencia con archivos `.json` y `.csv` (guardar y cargar datos).

# 🐾 Sistema de Gestión Veterinaria - Sprint 10

Este proyecto es una aplicación web desarrollada en Django que permite gestionar una clínica veterinaria. Fue creado como parte del Sprint 10 del curso de desarrollo de software.

## 🚀 Funcionalidades implementadas

- Registro de **Propietarios** (nombre, teléfono, correo electrónico).
- Registro de **Mascotas** (nombre, especie, edad, propietario).
- Listado de propietarios y mascotas.
- Formularios estilizados con CSS.
- Menú de navegación superior y logo personalizado.
- Panel de administración de Django activado.

## 🛠️ Tecnologías utilizadas

- Python 3.13
- Django 5.2.4
- HTML + CSS
- SQLite (base de datos por defecto)

## ⚙️ Instrucciones para ejecutar el proyecto localmente

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu_usuario/tu_repositorio.git
   cd tu_repositorio


Aplicación: http://127.0.0.1:8000/

Admin: http://127.0.0.1:8000/admin/