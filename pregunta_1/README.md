# prueba_tecnica_DO

Requisitos:
- Python 3.8
- virtualenv
- pip3
  
***

## Instrucciones Para Ejecución:

* Desde el terminal o CMD, ejeucutar lo siguiente (Debe estar ubicado en el directorio "pregunta_1")

### Crear y activar virtual environment
```python3 -m venv env```
<br/>

```source ./env/bin/activate``` (mac y linux)

```./env/bin/activate``` (windows)


### Instalar Dependencias

```python3 -m pip install -r requirements.txt```

### Ejecutar API

```uvicorn main:app```