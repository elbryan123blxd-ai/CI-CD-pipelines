# Continuos delivery
* veremos desde la creacion de nuestro vs code hasta el contenedor en docker hub , en este mismo repo estaras los archivos para que hagan push y los analizen ustedes tambien
*   VS Code => Github => Circle CI => Docker hub


## documentacion 
* empeze creando archivos en vs code (estan documentados en este repo de github)

* la primera parte del conjunto de archivos es el nucleo de la app, las librerias y empaquetamiento del codigo
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/66778576-5622-4a85-acdb-833d1e064c88" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/f9288bd1-77a4-4354-a631-ff538b3e92bd" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/f70f6f8e-fa91-4a28-8bc0-111355e5e133" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/e0d52ac3-678a-498d-ab3f-403bbe482503" />

* la segunda es el mas importante , pues es el config.yaml  ,esta sera como la receta que recibira circle CI para que haga prueba solas ,test y empaquete para enviarlo a dockerhub para posteriormente comenzar el CD
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/70a98a6f-6570-474e-85df-92ee83e72ca6" />

* el siguiente paso es crearse un repo en github donde pusheemos todos estos commits , al inicioo tuve varios problemas para pushearlo
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/8ae5d13b-b36b-4617-9a21-a269267c34d4" />

* pero finalmente lo logre
<img width="1920" height="1080" alt="image" src="https://github.com/user-atstachments/assets/5ad6f3cd-e678-48dc-81a3-fc34426db8d9" />

* AHORA teniendo todo pusheado a github vamos a la pagina de circle CI y creamos un proyecto vinculandolo
<img width="1024" height="576" alt="image" src="https://github.com/user-attachments/assets/db69d030-de76-47a4-94cf-252eab14d4d1" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/c5bbf7d7-001c-4889-816a-7ac08e2634ce" />

* hasta ahora nuestro flujo va asi:   vs code => github => circle ci   , ahora lo que haremos sera vincular nuestro circle con dockerhub , para eso debemos configurar las variables de entorno que usamos en nuestro archivo .yaml

*vinculamos con los datos de docker hub
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/5f332ff1-e9e5-4779-832b-6d157fac542a" />

*ahora empezamos con el pipeline
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/7569276f-c17f-47ba-b177-9cef9591bd5b" />

* bueno fallo , nose porque talvez puse mal el .yaml
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/c46555d3-9ad2-45be-8cb9-1c418ec63e18" />

* para sacar mas informacion sobre el error debemos entrar y leer el codigo , ahora sabemos que lo que estaba mal es que mi version ubuntu (reciente) no puede instalar paquetes requirements , con este nuevo codigo modificado si podre
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/376dc5c1-1fca-4b2e-81cd-6812ccff57cb" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/d246b5ad-9da7-4a39-90a1-f32810c801bc" />

*pusheamos y circle CI hara su magia
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/b6d326bd-34fd-4950-9f42-134d0339f1ab" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/73e37b11-95f1-4ca7-bf60-a64e6127a2ab" />

* si revisamos docker hub veeremos como se almaceno nuestra hermosa y bella imagen con exito para posteriormente convertir un container y pullearlo
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/f7289360-4f82-4617-afef-c061ee7b428e" />
* este fue todo el recorrido de CI , desde nuestra maquina local hasta automatizar pruebas en dockerhub , lo siguiente seria el CD , lo haremo proximamente , graciass
* hgga
