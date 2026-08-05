<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/5846fc19-81c5-40c4-add5-b661f83f0e04" /># Introducción a CircleCI 🚀

**CircleCI** es una plataforma basada en la nube de **CI/CD (Integración Continua y Entrega Continua)** diseñada para automatizar el proceso de compilación, prueba y despliegue de software.

## ¿Cómo Funciona?

Cada vez que envías código a tu repositorio (por ejemplo, a través de un `git push` en GitHub), CircleCI detecta los cambios automáticamente, ejecuta tus pruebas y valida que el código funcione antes de que llegue a producción. Todo se controla mediante un único archivo de configuración dentro de tu proyecto.

## Estructura del Archivo de Configuración (`.circleci/config.yml`)

El comportamiento de tus pipelines se define mediante tres conceptos clave:

* **Jobs (Trabajos):** Tareas individuales o bloques de acciones (como instalar dependencias, ejecutar tests o construir imágenes).
* **Steps (Pasos):** Los comandos secuenciales que ocurren dentro de cada job.
* **Workflows (Flujos de trabajo):** Controlan el orden, las reglas y las condiciones en las que se ejecutan los jobs.


## Trabajando con circle CI
* primero crearemos un repositorio temporal de github

*Nos creamos una cuenta en Circle CI y le damos a create project
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/ce21826d-99a0-4c26-a8a9-1ef9815e6d00" />


*Le damos a contruye ,prueba e implementa software
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/b2f503f9-8801-4457-be87-93791b98ea21" />


* Le ponemos un nombre
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/1a9f2157-7e2f-48aa-87db-c3a469317671" />


*le damos a siguiente
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/332ac2ad-ee08-4fea-81b0-ba2c9c2c0c4d" />


*Seleccionamos un repositorio , en mi caso el que dice pruebas , pues es el que cree
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/ab5950f9-7dc2-4195-93ce-5bf561178756" />


*continuamos
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/5a3cba85-ec1b-460c-bca2-a9c3d3ea822e" />


*aca circle CI detecto que mi repo esta vacio y simplemente me dio una plantilla predeterminada para que no se vea vacio , solo son temas visuales no se preocupen
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/78e72082-6c84-4626-a6ae-6a566f277ecf" />


*Aca esta la magia de los disparadores , estos se disparan cuando hagamos un push y analizaran si estan bien o mal , le damos a siguiente
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/26e0d761-9eb8-45a0-8669-47f064e6b989" />


*aca nos sale nuestra configuracion principal , simplemento le damos a confirmar y ejecutar
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/7da07b89-fa77-4b97-80bc-ef653ff27dfb" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/edfb0018-7ffa-4963-b961-d064a7562db5" />


*Listo tenemos nuestro Circle CI con exito
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/be410ca5-f4d3-4787-8f5e-01246e6ff347" />




