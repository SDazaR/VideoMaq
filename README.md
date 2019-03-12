# VideoMaya
Programa para detectar piezas en el Robot Maya de la sala CAM de la UNiversidad Nacional de Colombia y establecer cordenadas respectivas.

Al correr el script Buscar pieza.py, teniendo en cuenta:

  usage: BuscarPieza.py [-h] Objetivo Color Camara Muestras

  Busca y determina la posicion de objetos circulares para ejecutar Pick and
  Place con el Robot Maya

  positional arguments:
    Objetivo    Objetivo de la Maya (SDV, Buffer)
    Color       Color del objeto a tomar (rojo, verde, azul)
    Camara      Marca de la camara usada
    Muestras    Cantidad de imagenes usadas para encontrar la pieza
  
  optional arguments:
   -h, --help  show this help message and exit

Por ejemplo:
python BuscarPieza.py Buffer rojo Foscam 50

Busca piezas rojas en el buffer utilizando una camara Foscam y tomando 50 muestras para promediar el resultado. Por el momento solo está configurado el espacio del Buffer y los comandos para una cámara Foscam.

En caso de existir multipieza, el programá mostrará una imagen con las piezas señaladas para que el usuario elija la pieza objetivo.
