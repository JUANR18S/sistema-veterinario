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