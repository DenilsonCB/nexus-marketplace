# Product Backlog & Sprints - Nexus Marketplace

* **Autor / Responsable:** Brayan Denilson Choquehuanca Bedoya
* **Metodología:** Desarrollo Ágil basado en Scrum / Kanban

---

## 1. Épicas del Producto (Product Backlog)

Estas son las piezas estructurales de alto nivel del proyecto. Cada una se descompone en Historias de Usuario más pequeñas.

1. **[EPIC] Foundation & Core Infrastructure** (Configuración base, CI/CD, Base de datos).
2. **[EPIC] Módulo de Autenticación y Perfiles de Usuario** (JWT, Roles, Registro).
3. **[EPIC] Módulo de Catálogo y Búsqueda de Productos** (CRUD de productos, Filtros).
4. **[EPIC] Módulo de Carrito y Checkout Transaccional** (Gestión de órdenes, Pagos).
5. **[EPIC] Módulo de Panel de Vendedor / Merchant Dashboard** (Estadísticas, Inventario).

---

## 2. Historial de Sprints

### Sprint 1: Infraestructura Base e Identidad
* **Sprint Goal:** Configurar el andamiaje del backend, establecer el pipeline de validación automática (CI) con GitHub Actions y desplegar el modelo de usuario personalizado con soporte de roles.
* **Status:** Terminado
* **Velocidad (Story Points):** N/A (Sprint inicial de configuración)
* **Historias Completadas:**
  * `[P2 - 3 pts]` **US-01**: Inicialización de Arquitectura Base y CI/CD.
  * `[P1 - 5 pts]` **US-02**: Modelo de Usuario Personalizado y Control de Roles.
  * `[P2 - 3 pts]` **US-03**: Pipeline de Integración Continua (CI) con GitHub Actions.

### Sprint 2: Autenticación y Registro REST
* **Sprint Goal:** Habilitar el registro público de usuarios y asegurar la API REST mediante un flujo completo de JSON Web Tokens (JWT).
* **Status:** En Progreso
* **Puntos Comprometidos:** 13 pts estimados
* **Historias de Usuario:**
  * `[P1 - 3 pts]` **US-04:** Implementación de Seguridad y emisión de JWT (Login). *(Terminada)*
  * `[P1 - 5 pts]` **US-05:** Endpoint de Registro de Nuevos Usuarios (/register). *(En Progreso)*
  * `[P2 - 5 pts]` **US-06:** Endpoint Protegido de Perfil (/me). *(Sprint Backlog)*
