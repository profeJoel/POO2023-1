# Instrucciones para crear ejecutables de python con pyinstaller

1 - Installar el paquete
> pip install pyinstaller

2 - Crear ejecutable (Empaquetar)
+ situarse en el repositorio de la aplicación en terminal
+ lanzar comando:
> pyinstaller --onefile --noconsole archivo_aplicacion.py

3 - Situar aplicación en el computador (Empotrar)
+ Ir a la repositorio de aplicaciones y situarlo junto a las demás (MacOS)
+ (Win) Ir a C://Archivos de Programas//
+ Crear carpeta de su aplicación
+ Situar aplicación en esa carpeta con todo el material necesario.
+ Crear Acceso directo desde un ícono en el escritorio.


Observaciones:
- Revisar las rutas a sus recursos (imágenes, archivos de texto, otros programas...)
- El ejecutable solamente es funcional en el sistema operativo para el que se creó