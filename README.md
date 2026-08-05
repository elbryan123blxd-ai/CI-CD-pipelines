# Introducción a CircleCI 🚀

**CircleCI** es una plataforma basada en la nube de **CI/CD (Integración Continua y Entrega Continua)** diseñada para automatizar el proceso de compilación, prueba y despliegue de software.

## ¿Cómo Funciona?

Cada vez que envías código a tu repositorio (por ejemplo, a través de un `git push` en GitHub), CircleCI detecta los cambios automáticamente, ejecuta tus pruebas y valida que el código funcione antes de que llegue a producción. Todo se controla mediante un único archivo de configuración dentro de tu proyecto.

## Estructura del Archivo de Configuración (`.circleci/config.yml`)

El comportamiento de tus pipelines se define mediante tres conceptos clave:

* **Jobs (Trabajos):** Tareas individuales o bloques de acciones (como instalar dependencias, ejecutar tests o construir imágenes).
* **Steps (Pasos):** Los comandos secuenciales que ocurren dentro de cada job.
* **Workflows (Flujos de trabajo):** Controlan el orden, las reglas y las condiciones en las que se ejecutan los jobs.
