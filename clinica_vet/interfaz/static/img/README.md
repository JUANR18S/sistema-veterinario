# 🐶 Clínica Veterinaria - Amigos Peludos

Aplicación web desarrollada con Django como parte de un ejercicio práctico siguiendo el patrón arquitectónico **Modelo-Vista-Plantilla (MVT)**.

## 🎯 Objetivos del Proyecto

- Aplicar los fundamentos del framework Django en el desarrollo web.
- Definir rutas y vistas utilizando URLs limpias.
- Implementar estructura modular con herencia de plantillas (`base.html`).
- Incorporar archivos estáticos (CSS, imágenes).
- Mostrar contenido con diseño visual básico, pero ordenado.

---

## 🧩 Funcionalidades implementadas

- **Página de bienvenida** con logo, navegación y mensaje introductorio.
- **Página de servicios veterinarios** con contenido ficticio.
- **Página placeholder** lista para contenido dinámico futuro.
- **Encabezado y navegación fija** con enlaces estilizados.
- **Footer con derechos reservados** fijo al fondo.
- **Imagen del logo centrada y proporcionada** visualmente.
- **Estilos CSS personalizados** para toda la app.

---

## 🧱 Estructura del Proyecto

```
clinica_vet/
├── interfaz/
│   ├── static/
│   │   ├── css/
│   │   │   └── estilos.css
│   │   └── img/
│   │       └── logo.png
│   ├── templates/
│   │   ├── base.html
│   │   ├── inicio.html
│   │   ├── servicios.html
│   │   └── placeholder.html
│   └── views.py
├── manage.py
├── requirements.txt
├── README.md
```

---

## 🚀 Instalación y ejecución

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/JUANR18S/clinica_vet.git
   ```

2. Crear y activar entorno virtual:
   ```bash
   python -m venv env
   source env/bin/activate  # o env\Scripts\activate en Windows
   ```

3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Ejecutar servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```

5. Abrir en el navegador:
   ```
   http://127.0.0.1:8000/
   ```

---

## 🛠️ Tecnologías usadas

- Python 3.13.5
- Django 5.2.4
- HTML5 + CSS3
- Estructura MVT

---

## 👤 Autor

**Juan Camilo Ríos Mesa**  
*Estudiante y desarrollador en formación apasionado por la tecnología, la ciberseguridad y el arte digital.*

---

## 📄 Licencia

Proyecto con fines académicos. Derechos reservados © 2025.
