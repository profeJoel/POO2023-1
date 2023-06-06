# Cómo instalar entorno virtual de python

- crear entorno virtual
 > python3 -m venv nombre_entorno
- ejecutar entorno
 > ./nombre_entorno/bin/Activate.ps1 # para Windows
Si tienes problemas con la ejecución de comandos .ps1 utiliza:
 > Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted

En caso de ser usuario de linux y mac:
 > source nombre_entorno/bin/activate

- Para finalizar el entorno:
 > deactivate  