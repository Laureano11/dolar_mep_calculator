# Calculator MEP

Este repositorio contiene un script en Python llamado `gap_detecter.py` que consulta cotizaciones públicas, calcula un valor aproximado del MEP y lo compara con el dólar blue. El objetivo es mostrar la diferencia entre ambos valores y estimar una ganancia potencial para un saldo fijo.

## Qué hace `gap_detecter.py`

El script hace lo siguiente:

1. Consulta el precio del dólar blue desde un sitio público.
2. Consulta las cotizaciones de los bonos GD30 y GD30D desde otro sitio.
3. Calcula un valor MEP aproximado usando esas cotizaciones.
4. Obtiene la diferencia entre el blue y el MEP.
5. Calcula una ganancia estimada usando un saldo fijo de 10000.
6. Muestra todos esos valores en consola.

## Requisitos

- Python 3.10 o superior.
- Conexión a internet para que el script pueda consultar los sitios externos.
- Tener instaladas las dependencias `requests` y `beautifulsoup4` en el entorno Python que uses.

## Paso a paso para correrlo

1. Cloná el repositorio.

```bash
git clone <url-del-repositorio>
cd dolar_mep_calculator
```

2. Activá tu entorno virtual de Python.

Si ya tenés uno creado, activalo. Si no, crealo con el Python que uses habitualmente.

```bash
source .venv/bin/activate
```

3. Instalá las dependencias necesarias.

```bash
pip install requests beautifulsoup4
```

4. Ejecutá el script desde la raíz del proyecto.

```bash
python gap_detecter.py
```

5. Leé la salida en terminal.

Vas a ver impreso el valor del dólar blue, el valor MEP calculado, la diferencia entre ambos y la ganancia estimada.

## Observaciones

- El script depende de la estructura HTML de sitios externos; si cambian su diseño, puede fallar o devolver datos incorrectos
