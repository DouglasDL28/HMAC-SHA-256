# HMAC-SHA-256
## Parte1:
Implementación de HMAC-SHA-256 para Cifrado de Información.
**Para ejecutarlo:**
* Correr el comando:
```
pip install pycryptodome
```
* Correr el programa con:
```
python lab3-parte2-1.py
```
## Parte2:
<p>Implementación de ambiente para simular un timing attack a un servidor.<br> 
Se implementó un simulador de servidor inseguro, otro seguro con el método 1 y otro seguro con el método 2.<br>
**Para instalar dependencias:**</p>
* Crear un entorno virtual, correr el código en la dirección del proyecto:
```
virtualenv venv
```
* Activar el entorno virtual:
```
mypthon\Scripts\activate
```
* Instalar dependencias:
```
pip install -r requirements.txt
```
### Simulador inseguro:
**Para ejecutarlo:**
* Correr (en el entorno virtual) el programa que levanta el simulador del servidor:
```
python unsafeApp.py
```
* Correr el programa que intenta hackear el simulador del servidor con:
```
python hacker.py
```
### Simulador seguro con el método 1:
**Para ejecutarlo:**
* Correr (en el entorno virtual) el programa que levanta el simulador del servidor:
```
python safeAppMethod1.py
```
* Correr el programa que intenta hackear el simulador del servidor con:
```
python hacker.py
```
### Simulador seguro con el método 2:
**Para ejecutarlo:**
* Correr (en el entorno virtual) el programa que levanta el simulador del servidor:
```
python safeAppMethod2.py
```
* Correr el programa que intenta hackear el simulador del servidor con:
```
python hacker.py
```
