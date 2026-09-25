# Nexus Marketplace

[![Backend CI Pipeline](https://github.com/DenilsonCB/nexus-marketplace/actions/workflows/backend-ci.yml/badge.svg)](https://github.com/DenilsonCB/nexus-marketplace/actions/workflows/backend-ci.yml)
![Python Version](https://img.shields.io/badge/python-3.12-blue.svg)
![Django Version](https://img.shields.io/badge/django-6.1-green.svg)
![React](https://img.shields.io/badge/react-18%2B-61DAFB.svg)
![TypeScript](https://img.shields.io/badge/typescript-5-blue.svg)
![Status](https://img.shields.io/badge/status-active%20development-brightgreen.svg)

Plataforma Full-Stack de E-Commerce y Marketplace construida con arquitectura limpia, servicios desacoplados y transacciones ACID de alta concurrencia.

---

## 1. Arquitectura del Sistema

* **Backend:** Django REST Framework (DRF) + Python 3.12 con diseño modular en `apps/`.
* **Base de Datos:** PostgreSQL con control de concurrencia pesimista (`select_for_update`) para garantizar la atomicidad en el proceso de checkout.
* **Frontend:** Single Page Application (SPA) desacoplada construida con React, Vite, TypeScript y estilos con Tailwind CSS.
* **Integración Continua (CI):** Pipeline automatizado con GitHub Actions en entornos Linux (Ubuntu), ejecutando chequeos de integridad del sistema y suites de pruebas unitarias.
* **Gestión del Proyecto:** Metodología ágil Scrum / Personal Software Process (PSP) con historias de usuario y criterios de aceptación documentados en [`docs/BACKLOG.md`](docs/BACKLOG.md).

---

## 2. Estructura del Repositorio

```text
nexus-marketplace/
├── .github/
│   └── workflows/
│       └── backend-ci.yml    # Pipeline de Integración Continua (GitHub Actions)
├── backend/                  # Núcleo de la API REST (Django + DRF)
│   ├── apps/
│   │   └── authentication/   # Gestión de identidad, Custom User Model y roles
│   ├── core/                 # Configuración central del proyecto (settings, urls)
│   ├── manage.py
│   └── requirements.txt      # Dependencias fijadas del backend
├── docs/
│   └── BACKLOG.md            # Product Backlog, Sprints e Historias de Usuario
├── .gitignore                # Reglas de exclusión de Git (Node, Python, VS Code)
└── README.md                 # Documentación principal del proyecto
```

---

## 3. Módulos y Funcionalidades del Marketplace

1. **Gestión de Identidad y Roles (`apps/authentication`):**
   - Custom User Model basado en `AbstractUser`.
   - Autenticación mediante correo electrónico como identificador único.
   - Control de acceso basado en roles: Comprador (`is_customer`) y Vendedor (`is_merchant`).
2. **Catálogo de Productos (`apps/catalog`):**
   - Categorización jerárquica de productos, slugs SEO e imágenes.
   - Control de inventario en tiempo real.
3. **Carrito de Compras y Checkout Atómico (`apps/orders`):**
   - Persistencia de carritos de compra.
   - Transacciones atómicas de base de datos (`@transaction.atomic`).
   - Bloqueo pesimista de stock para prevención de condiciones de carrera (*race conditions*) en compras concurrentes.
   - Máquina de estados determinista para órdenes (`PENDING`, `PAID`, `SHIPPED`, `CANCELLED`).
4. **Documentación de API:**
   - Estandarización RESTful con códigos HTTP semánticos.
   - Esquemas OpenAPI 3.0 interactivos generados con Swagger UI / Redoc.

---

## 4. Guía de Instalación y Ejecución Local

### Prerrequisitos
* **Python:** 3.12 o superior.
* **Node.js:** 20 LTS o superior.
* **Git**

### Configuración del Backend

```bash
# 1. Clonar el repositorio
git clone https://github.com/DenilsonCB/nexus-marketplace.git
cd nexus-marketplace/backend

# 2. Crear y activar el entorno virtual
python -m venv .venv

# En Windows (PowerShell):
.\.venv\bin\Activate.ps1
# En Linux / macOS:
source .venv/bin/activate

# 3. Actualizar pip e instalar dependencias
python -m pip install --upgrade pip
pip install -r requirements.txt

# 4. Validar configuración y aplicar migraciones
python manage.py check
python manage.py migrate

# 5. Iniciar servidor de desarrollo
python manage.py runserver
```

El servidor quedará disponible en `http://127.0.0.1:8000/`.

---

## 5. Autor

* **Brayan Denilson Choquehuanca Bedoya** ([@DenilsonCB](https://github.com/DenilsonCB))
* Estudiante de Ingeniería de Sistemas — Universidad Nacional de San Agustín (UNSA), Arequipa, Perú.
