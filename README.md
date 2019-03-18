# VideoMaya
Programa para detectar piezas en diferentes celdas de la sala CAM de la UNiversidad Nacional de Colombia y establecer cordenadas respectivas para diferentes máquinas.

Al correr el script Buscar pieza.py, tener en cuenta:

  usage: BuscarPieza.py [-h] Objetivo Color Camara Muestras

  Busca y determina la posicion de objetos circulares para ejecutar Pick and
  Place.

  positional arguments:
    Objetivo    Objetivo de la Maya

    Color       Color del objeto a tomar
    
    Camara      Camara usada
    
    Muestras    Cantidad de imagenes usadas para encontrar la pieza
  
  optional arguments:
   -h, --help  show this help message and exit

Por ejemplo:
python BuscarPieza.py Buffer rojo Foscam 50

Busca piezas rojas en el buffer utilizando una camara Foscam y tomando 50 muestras para promediar el resultado. 

Por el momento solo se ha establecido los atributos para:

  Objetivos:
  
  - Buffer
  
  - SDVMotoman
  
  Camaras:
  
  - Web
  
  - FoscamMotoman
  
  - FoscamMaya
  

Para añadir nuevas mquinas o cámaras se puede a través del script Configuraciones siguiendo los lineamientos en él explicados.

En caso de existir multipieza, el programá mostrará una imagen con las piezas señaladas para que el usuario elija la pieza objetivo.
