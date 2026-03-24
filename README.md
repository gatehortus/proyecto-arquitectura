# VeriPay — Sistema de Conciliación Automática de Pagos

Sistema web desarrollado con Django 6.0.3 y PostgreSQL para la conciliación automática de pagos entre facturas de proveedores, registros de pago bancarios y certificados bancarios.

## Requisitos

- Docker y Docker Compose
- Git

## Ejecución con Docker

```bash
# Clonar el repositorio
git clone https://github.com/gatehortus/proyecto-arquitectura.git
cd proyecto-arquitectura

# Levantar el proyecto
docker-compose up --build
```

El sistema estará disponible en: **http://localhost:8000**

### Credenciales por defecto

- **Usuario:** admin
- **Contraseña:** admin123

## Estructura del Proyecto

```
veripay_project/     # Configuración principal de Django
core/                # Dashboard, login, reportes, email, panel admin
proveedores/         # Gestión de proveedores (CRUD)
facturas/            # Gestión de facturas + OCR
pagos/               # Carga y procesamiento de archivos de pagos (CSV)
certificados/        # Certificados bancarios (CRUD)
conciliacion/        # Motor de conciliación automática
templates/           # Templates HTML (Bootstrap 5)
static/              # CSS, JS, imágenes
resources/lang/      # Archivos de internacionalización (es/en)
```

## Rutas Principales

| Ruta | Descripción |
|------|-------------|
| `/` | Dashboard principal |
| `/login/` | Inicio de sesión |
| `/proveedores/` | Lista de proveedores |
| `/facturas/` | Lista de facturas |
| `/facturas/ocr/` | Carga de facturas con OCR |
| `/pagos/` | Archivos de pagos |
| `/certificados/` | Certificados bancarios |
| `/conciliacion/` | Procesos de conciliación |
| `/conciliacion/ejecutar/` | Ejecutar nueva conciliación |
| `/reportes/` | Generación de reportes PDF |
| `/email-resumen/` | Envío de resumen por correo |
| `/admin-panel/` | Panel de administración |

## Funcionalidades Interesantes

1. **OCR para Facturas** (`facturas/services.py:15`) — Extrae automáticamente datos de imágenes de facturas usando Tesseract OCR.
2. **Conciliación Automática** (`conciliacion/services.py:13`) — Algoritmo que cruza facturas contra pagos y certificados con porcentaje de confianza configurable.
3. **Generación de Reportes PDF** (`core/services/pdf_generator.py:13`) — Genera reportes en PDF de facturas, conciliaciones y proveedores.
4. **Envío de Resumen por Email** (`core/services/email_service.py:8`) — Envía resúmenes del estado de pagos a los proveedores por correo electrónico.

## Tecnologías

- **Backend:** Django 6.0.3, Python 3.12
- **Base de datos:** PostgreSQL 16
- **Frontend:** Bootstrap 5.3, Chart.js
- **OCR:** Tesseract + pytesseract
- **PDF:** xhtml2pdf
- **Servidor:** Gunicorn
- **Contenedores:** Docker + Docker Compose

## Secciones

- **Usuario final** (`/`): Puede ver dashboard, facturas, pagos, certificados, conciliaciones y reportes. No puede crear, editar ni eliminar registros.
- **Administrador** (`/admin-panel/`): Acceso completo a CRUD, gestión de usuarios, ejecución de conciliaciones y configuración del sistema.
