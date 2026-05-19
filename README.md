# VeriPay — Sistema de Conciliación Automática de Pagos

Sistema web desarrollado con Django 6.0.3 y PostgreSQL para la conciliación automática de pagos entre facturas de proveedores, registros de pago bancarios y certificados bancarios.

Entrega 2: Arquitectura MVC + Servicios + Inversión de Dependencias + Docker + i18n + Cloud Run.

## Requisitos

- Docker y Docker Compose (local)
- Cuenta GCP con Cloud Run, Cloud SQL y Cloud Build habilitados (producción)
- Git

## Ejecución local con Docker

```bash
git clone https://github.com/gatehortus/proyecto-arquitectura.git
cd proyecto-arquitectura
docker-compose up --build
```

Aplicación disponible en **http://localhost:8000**.

### Credenciales por defecto

| Usuario  | Contraseña  | Rol            |
|----------|-------------|----------------|
| admin    | admin123    | Administrador  |
| usuario  | usuario123  | Usuario final  |

## Estructura del Proyecto

```
veripay_project/      Configuración Django (settings, urls, wsgi)
core/                 Dashboard, login, reportes, email, panel admin, servicios externos
proveedores/          CRUD de proveedores + API JSON pública
facturas/             CRUD de facturas + OCR (Tesseract)
pagos/                Carga y procesamiento de archivos de pagos (CSV)
certificados/         CRUD de certificados bancarios
conciliacion/         Motor de conciliación automática
reportes/             Inversión de dependencias para reportes (PDF + Excel)
templates/            Templates HTML (Bootstrap 5)
static/               CSS, JS, imágenes
locale/{es,en}/       Archivos de internacionalización
docs/                 Diagramas de clases y arquitectura
```

## Rutas Principales

| Ruta                          | Descripción                                  |
|-------------------------------|----------------------------------------------|
| `/`                           | Dashboard principal                          |
| `/login/`                     | Inicio de sesión                             |
| `/proveedores/`               | Lista de proveedores                         |
| `/facturas/`                  | Lista de facturas                            |
| `/facturas/ocr/`              | Carga de facturas con OCR                    |
| `/pagos/`                     | Archivos de pagos                            |
| `/certificados/`              | Certificados bancarios                       |
| `/conciliacion/`              | Procesos de conciliación                     |
| `/conciliacion/ejecutar/`     | Ejecutar nueva conciliación                  |
| `/reportes/`                  | Generación de reportes PDF / Excel           |
| `/email-resumen/`             | Envío de resumen por correo                  |
| `/aliados/`                   | Consumo del servicio del equipo precedente   |
| `/admin-panel/`               | Panel de administración                      |
| `/api/proveedores-publicos/`  | Servicio JSON expuesto al equipo siguiente   |
| `/i18n/setlang/`              | Cambio de idioma (ES / EN)                   |

## Servicios y consumos externos

### Servicio JSON propio (lo consume el equipo siguiente)

`GET /api/proveedores-publicos/` → arreglo JSON con `id`, `nombre`, `nit`, `email` de cada proveedor.

### Consumo del equipo precedente

La vista `/aliados/` consume el JSON expuesto por el equipo precedente. Para activarlo, definir la variable de entorno `EQUIPO_PREVIO_API_URL` con la URL completa del servicio.

### Servicio de tercero — TRM USD/COP (Superfinanciera)

`core/services/trm_service.py` consume el dataset oficial de la Superintendencia Financiera de Colombia (`https://www.datos.gov.co/resource/32sa-8pi3.json`) y muestra la **Tasa Representativa del Mercado** vigente en la barra superior. Sirve de referencia para conciliar facturas en moneda extranjera. No requiere API key. Cacheado 60 minutos.

## Inversión de dependencias

`reportes/services/report_generators.py` define la interfaz `ReportGenerator` con dos implementaciones concretas:

- `PDFReportGenerator` — usa **reportlab** y delega en `core/services/pdf_generator.py`.
- `ExcelReportGenerator` — usa **openpyxl** y genera un `.xlsx` real.

`core.views.ReportsView` selecciona la implementación según el campo `formato` del formulario, sin acoplarse a ninguna clase concreta.

## Internacionalización

- Idiomas soportados: español (default) e inglés.
- Switcher en la barra superior y en la pantalla de login.
- Mensajes traducidos en `locale/es/LC_MESSAGES/django.po` y `locale/en/LC_MESSAGES/django.po`.
- Para regenerar:

```bash
python manage.py makemessages -l es -l en
python manage.py compilemessages
```

## Pruebas

```bash
docker-compose exec web python manage.py test
```

Cubren modelos, vistas, API JSON y los dos generadores de reportes.

## Variables de entorno

| Variable                  | Default                       | Descripción                                       |
|---------------------------|-------------------------------|---------------------------------------------------|
| `DJANGO_SECRET_KEY`       | (insecure dev key)            | Clave secreta de Django                           |
| `DJANGO_DEBUG`            | `True`                        | `False` en producción                             |
| `DJANGO_ALLOWED_HOSTS`    | `localhost,127.0.0.1,*`       | Hosts permitidos (csv)                            |
| `CSRF_TRUSTED_ORIGINS`    | `''`                          | Orígenes confiables para CSRF (csv, con https://) |
| `DATABASE_URL`            | (sqlite local)                | URL de Postgres / Cloud SQL                       |
| `EQUIPO_PREVIO_API_URL`   | `''`                          | URL del JSON del equipo precedente                |
| `RUN_SEED`                | `true`                        | Si `true`, ejecuta `seed_data` al arrancar        |
| `PORT`                    | `8000`                        | Puerto de gunicorn (Cloud Run lo inyecta)         |

## Despliegue en Google Cloud Run

```bash
gcloud services enable run.googleapis.com sqladmin.googleapis.com \
  artifactregistry.googleapis.com cloudbuild.googleapis.com

gcloud sql instances create veripay-db \
  --database-version=POSTGRES_16 \
  --tier=db-f1-micro \
  --region=us-central1

gcloud sql databases create veripay --instance=veripay-db
gcloud sql users create veripay_user --instance=veripay-db --password=<CHOOSE>

gcloud builds submit --config=cloudbuild.yaml
```

Configurar después de la primera ejecución la env var `DATABASE_URL` en Cloud Run con el formato:

```
postgres://veripay_user:<pwd>@/veripay?host=/cloudsql/<PROJECT_ID>:us-central1:veripay-db
```

## Equipo

- **Gabriel Atehortua Spoor** — Arquitecto principal
- **Isabel Acevedo Acosta** — Arquitecta de usabilidad
- **Samuel Granados Lopez** — Desarrollador

## Tecnologías

- Backend: Django 6.0.3, Python 3.12
- Base de datos: PostgreSQL 16 (Cloud SQL en producción)
- Frontend: Bootstrap 5.3, Chart.js
- OCR: Tesseract + pytesseract
- PDF: reportlab
- Excel: openpyxl
- HTTP cliente: requests
- Servidor: Gunicorn
- Contenedores: Docker + Docker Compose
- Despliegue: Google Cloud Run + Cloud SQL
