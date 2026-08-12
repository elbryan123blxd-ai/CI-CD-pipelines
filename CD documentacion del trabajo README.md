
# CD despliegue a AWS
* ya tenemos nuestro proceso CI la idea ahora el objetivo es que el codigo llegue a entornos donde podremos subirlos a produccion ( nube de AWS) , en mi caso es el eks-user con permisos
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/d508e3bc-5305-422e-83fa-6948bd9729e2" />

## llevando nuestro entorno a la nube 
* debemos crear un usuario IAM y tener anotadas sus credenciales
* para llevarlo a la nube a continuacion cree mi ECR en AWS que es el equivalente a docker hub
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/c8304f87-62e7-4af4-a4e7-9f53ab785c26" />

* ahora queremos que  Circle CI apunte a AWS ECR en vez de docker hub , les pondremos las credenciales de nuestro user , contraseña , region y el link del ecr
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/7d12eebc-ea67-4fa9-883b-ad915736958a" />

* el archivo se modfico , antes apuntada todo a docker hub , ahora instala herramientas CLI , ejecuta las pruebas, usa las credenciales de aws y hace push en ECR
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/bb0bf82c-98cb-45b5-872e-5a525615d1fe" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/c1b8f611-fc43-44f0-a36c-36e100670009" />

* ahora asi pusheamos y fallo el push porque el github tiene cambios que no estan en mi pc , pero nada que unos comandos arreglen
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/38034edd-bc5a-4d3c-ae73-96a579ad93c8" />

* ok el circle ci esta empezando con las pruebas pero tuvimos fallas en las variables de aws que pusimos , a solucionar
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/944c2e64-3e35-46a5-a592-d13f6b373588" />

* VAMOS CARAJO el problema era que las credenciales estaban mal puestas
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/f918296f-18bb-4a2a-a423-7e55a6c1f68f" />

* Ahora en ECR logramos tener nuestra imagen guardada , en una infraestructura muy robusta y que cumple con requisitos de seguirdad de grandes empresas
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/b40b6284-fb78-4715-9a81-540196232e96" />

* ahora usaremos AWS ecs express mode para desplegar nuestra aplicacion
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/12f59bb6-d9db-4b01-84ab-b402f4880534" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/437a2311-c019-4ec0-876b-bc84aa9c2a23" />

* ya tenemos nuestro express mode en aws
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/e5e8f2e4-eb00-4f98-bee9-9b2e9a3595f4" />

* FUNCIOONOOOOO LO HICEEEEE , AHORA ENTRAMOS Y DEBERIA SALIR EL MENSAJE
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/05c1fad0-7f26-4881-9da7-d56bd4d4f96e" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/dd87017f-5f08-4ada-9ff9-8b7af680f25a" />
* dios mio que felicidad


* haremos algo interesante , modificaremos mi archivo , le haremos push y ocurrira toda la magia , vamos a cambiarle el texto y solo haremos un push y la magia vendraaaa
*  vs code => github => circle CI =>ECR => ECS exprees mode => produccion
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/10359952-e556-47f3-a97b-c2e02576e0f1" />
<img width="1024" height="576" alt="image" src="https://github.com/user-attachments/assets/7976d39f-6371-429d-a135-e55d06ce0610" />
<img width="1024" height="576" alt="image" src="https://github.com/user-attachments/assets/2ee7c719-5a6a-42ce-a28c-e9432bd1a951" />
<img width="1024" height="576" alt="image" src="https://github.com/user-attachments/assets/0641e4f0-95d2-45c8-9d84-15970070bb84" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/7aded80e-a53e-48c7-a2c9-7cdf60f40de0" />

* disculpen la demora pero mi wifi es lento :C me mude con mi madre y mis hermanos y en esta zona el wifi esta pesimo pero ya cargara
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/abf950ce-486b-4f61-87f5-6e794c8d4fa1" />

* le voy a mandar otro push mi laptop ta modo tostadora :C
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/d75dab68-34c1-47a2-8711-5a84465f0131" />


*PORFIN LO LOGRE CARAJO VAMOOOS
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/ddd43d5a-65b2-416a-aa9c-bf7b506dc6bd" />

* encontre el problemas despues de muchos force sin sentido el problema era el @sash que hacia que mi codigo se quedara amarrada a la imagen principal y en circle ci modifique el pipeline para que apuntara
a $CIRCLE_SHA1
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/0e4466d9-baf2-44bc-b59c-e8dff50c7ae9" />
* en resumen solucione el problema de los caches viejos
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/1843f4ca-a5b7-4968-9001-783eba5d43ac" />

* miren ahora hice un push y ahora sin tocar nada solito sale la nuevai magen
