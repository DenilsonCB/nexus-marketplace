# Product Backlog & Sprints - Nexus Marketplace

* **Autor / Responsable:** Brayan Denilson Choquehuanca Bedoya
* **Metodología:** Desarrollo Ágil basado en Scrum / PSP (Personal Software Process)

---

## 1. Épicas del Producto

* [EP-01] Autenticación, Identidad y Control de Acceso Basado en Roles (RBAC).
* [EP-02] Catálogo de Productos, Categorías y Gestión de Stock.
* [EP-03] Carrito de Compras y Motor Transaccional de Checkout (ACID).
* [EP-04] Pipeline de Integración y Entrega Continua (CI/CD) con GitHub Actions.
* [EP-05] Frontend SPA con React, Vite y TypeScript.

---

## 2. Sprint 1: Infraestructura Base, Identidad y CI

* **Sprint Goal:** Configurar el andamiaje del backend, establecer el pipeline de validación automática con GitHub Actions y desplegar el modelo de usuario personalizado con soporte de roles.

### Historias de Usuario

#### [US-01] Inicialización del Entorno y Arquitectura Base
* **Como:** Desarrollador del sistema.
* **Quiero:** Estructurar un espacio de trabajo modular con Django 5 y DRF.
* **Para:** Contar con una base reproducible y desacoplada para los módulos de negocio.
* **Criterios de Aceptación (DoD):**
  - [x] Entorno virtual `.venv` aislado con dependencias fijadas en `requirements.txt`.
  - [x] Proyecto Django `core` inicializado en la raíz del backend.
  - [x] Archivo `.gitignore` configurado para omitir archivos temporales y secretos.
  - [x] Servidor de desarrollo validado en ejecución local.

#### [US-02] Modelo de Usuario Personalizado (Custom User Model)
* **Como:** Usuario de la plataforma (comprador o vendedor).
* **Quiero:** Registrarme e iniciar sesión utilizando mi correo electrónico como identificador único.
* **Para:** Tener un acceso seguro y moderno sin requerir nombres de usuario obligatorios.
* **Criterios de Aceptación (DoD):**
  - [ ] Clase `User` heredando de `AbstractUser`.
  - [ ] Atributo `email` único configurado como `USERNAME_FIELD`.
  - [ ] Banderas booleanas para control de roles: `is_merchant` e `is_customer`.
  - [ ] Directiva `AUTH_USER_MODEL` registrada en `settings.py` previa a la migración inicial.
  - [ ] Migraciones generadas y aplicadas en base de datos.

#### [US-03] Pipeline de Integración Continua (CI) con GitHub Actions
* **Como:** Ingeniero a cargo del repositorio.
* **Quiero:** Un flujo automatizado que valide el código en cada commit y Pull Request.
* **Para:** Garantizar que ningún cambio rompa las pruebas o la configuración del sistema.
* **Criterios de Aceptación (DoD):**
  - [ ] Definición del workflow en `.github/workflows/backend-ci.yml`.
  - [ ] Configuración del runner sobre Ubuntu con la versión correcta de Python.
  - [ ] Instalación automática de dependencias desde `requirements.txt`.
  - [ ] Ejecución del comando de verificación del sistema (`python manage.py check`).
  - [ ] Ejecución de la suite de pruebas unitarias (`python manage.py test`).