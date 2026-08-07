# Introducción a CircleCI 🚀

**CircleCI** es una plataforma basada en la nube de **CI/CD (Integración Continua y Entrega Continua)** diseñada para automatizar el proceso de compilación, prueba y despliegue de software.

## ¿Para qué sirve?
Permite a los desarrolladores detectar errores de manera temprana y entregar nuevas funcionalidades a producción de forma rápida y segura. Cada vez que subes código nuevo a tu repositorio (como en GitHub), CircleCI ejecuta automáticamente flujos de trabajo (*pipelines*) definidos por ti para verificar que todo funcione correctamente antes de fusionarlo o desplegarlo.

## Características principales:
* **Automatización rápida:** Configura pipelines mediante archivos YAML sencillos (ubicados en la carpeta `.circleci/config.yml`).
* **Integración nativa:** Se conecta de forma fluida y automática con plataformas como GitHub y Bitbucket.
* **Ejecución en contenedores:** Permite correr tus pruebas dentro de contenedores **Docker**, garantizando que el entorno de pruebas sea idéntico al de producción.
* **Optimización y velocidad:** Cuenta con sistemas de caché inteligentes para acelerar las compilaciones y ahorrar tiempo de ejecución.
