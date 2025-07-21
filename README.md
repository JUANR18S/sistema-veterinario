# 🐾 Sistema de Gestión Veterinaria

Este proyecto es una aplicación de escritorio desarrollada en **Python**, enfocada en la gestión integral de una clínica veterinaria. Permite registrar pacientes, consultas, y gestionar la información de dueños y mascotas, utilizando archivos **JSON** y una base de datos **SQLite** para la persistencia de datos.

---

## 🚀 Funcionalidades principales

- Registrar dueños, mascotas y consultas
- Guardar y cargar datos desde archivos JSON
- Insertar, consultar, actualizar y eliminar registros en base de datos SQLite
- Validación básica de integridad (no eliminar dueños con mascotas asociadas)
- Interfaz por consola amigable y clara
- Registro de logs para seguimiento de eventos y errores

---

## 🧱 Tecnologías utilizadas

### 🗂 JSON
- Utilizado para guardar datos temporales y respaldos de dueños, mascotas y consultas.
- Fácil de transportar y legible por humanos.

### 🗃 SQLite
- Base de datos embebida que permite persistencia real.
- Todas las tablas se crean automáticamente si no existen:
  - `duenos`
  - `mascotas`
  - `consultas`

---

## 🛠 Estructura de tablas

### 📋 Tabla: `duenos`
| Campo     | Tipo    |
|-----------|---------|
| id        | INTEGER (PK) |
| nombre    | TEXT    |
| documento | TEXT    |
| correo    | TEXT    |
| telefono  | TEXT    |

### 🐶 Tabla: `mascotas`
| Campo     | Tipo    |
|-----------|---------|
| id        | INTEGER (PK) |
| nombre    | TEXT    |
| especie   | TEXT    |
| raza      | TEXT    |
| edad      | INTEGER |
| peso      | REAL    |
| motivo    | TEXT    |
| id_dueño  | INTEGER (FK) |

### 🩺 Tabla: `consultas`
| Campo       | Tipo    |
|-------------|---------|
| id          | INTEGER (PK) |
| fecha       | TEXT    |
| motivo      | TEXT    |
| diagnostico | TEXT    |
| tratamiento | TEXT    |
| id_mascota  | INTEGER (FK) |

---

## 🧪 Funcionalidades implementadas (CRUD SQLite)

| Entidad  | Insertar | Consultar | Actualizar | Eliminar |
|----------|----------|-----------|------------|----------|
| Dueños   | ✅        | ✅         | ✅          | ✅        |
| Mascotas | ✅        | ✅         | ✅          | ✅        |
| Consultas| ✅        | ✅         | ✅          | ✅        |

---

## 🧭 Menú principal (por consola)

```text
===== 🏥 Sistema Veterinario =====
1. Registrar paciente completo (JSON)
2. Registrar consulta (JSON)
3. Listar mascotas
4. Ver historial
5. Insertar dueño (SQLite)
6. Insertar mascota (SQLite)
7. Insertar consulta (SQLite)
8. Consultar dueños (SQLite)
9. Consultar mascotas (SQLite)
10. Consultar consultas (SQLite)
11. Actualizar dueño (SQLite)
12. Actualizar mascota (SQLite)
13. Actualizar consulta (SQLite)
14. Eliminar dueño (SQLite)
15. Eliminar mascota (SQLite)
16. Eliminar consulta (SQLite)
17. Salir


## 🧪 Ejecutar el programa

1. Clona o descarga el repositorio.
2. Activa tu entorno virtual:
   ```bash
   .\env\Scripts\Activate.ps1   # Windows PowerShell
