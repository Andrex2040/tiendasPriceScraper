# [UOC] Tipología y ciclo de vida de los datos | Práctica 1: Web scraping 

## Tecnologias

![technology Python](https://img.shields.io/badge/Python-3.x-blue.svg) ![technology Selenium](https://img.shields.io/badge/-Selenium-green?style=flat&logo=Selenium&logoColor=white)

# Integrantes

[![LinkedIn de Carlos Andrés Rivera Rivera](https://img.shields.io/badge/LinkedIn-Carlos_Andrés_Rivera_Rivera-blue?logo=linkedin&style=social)](https://www.linkedin.com/in/carlos-andres-rivera-rivera-72213069/)

[![Twitter de Gustavo Salgado Ocampo](https://img.shields.io/badge/Twitter-Gustavo_Salgado_Ocampo-blue?logo=twitter&style=social)](https://twitter.com/edgaso)

# Comparador de Precios de Supermercados con Selenium y Python

Este proyecto, desarrollado en Python utilizando la biblioteca Selenium, tiene como objetivo facilitar la comparación de precios en dos supermercados distintos para una categoría específica de productos. Mediante técnicas de web scraping, el programa identifica y extrae los precios de los productos en ambas tiendas, almacenándolos en un archivo de texto plano para su posterior análisis.

La finalidad de este proyecto es determinar en cuál de los supermercados se puede encontrar un producto específico a un precio más bajo, y además, permitir el estudio de tendencias en los precios a lo largo del tiempo. Esto puede ser útil para consumidores que buscan maximizar sus ahorros, así como para investigadores interesados en analizar patrones y fluctuaciones en el mercado de productos de consumo.

| https://www.exito.com/licores?_q=licores&map=ft| https://www.tiendasjumbo.co/licores?_q=licores&map=ft |
|-------|----------|
| ![img.png](img.png) | ![img_1.png](img_1.png) | 

### Características principales
* Comparación de precios en dos supermercados distintos para una categoría específica de productos.
* Extracción de datos mediante web scraping utilizando Selenium
* Almacenamiento de los precios extraídos en un archivo de texto plano
* Facilita el análisis de tendencias y patrones en los precios de los productos

### Posibles aplicaciones
* Ahorro en compras al identificar el supermercado con los precios más bajos.
* Estudio de tendencias de precios en el tiempo para una categoría específica de productos.
* Análisis de fluctuaciones en el mercado de productos de consumo.

# Ficheros del código fuente

* **src/shopExitoSelenium.py**: Realiza el proceso de scraping a site: https://www.exito.com/licores?_q=licores&map=ft  usando la librería de selenium y driver de navegador, se configuró para que realice el proceso en segundo plano. 
* **src/shopJumboSelenium.py**: Realiza el proceso de scraping a site: https://www.tiendasjumbo.co/licores?_q=licores&map=ft usando la librería de selenium y driver de navegador, se configuró para que realice el proceso en segundo plano.
* **src/compararPrecios.py**: Crea archivo csv comparando los dos precios en tiendas por coincidencias entre productos..

# Librerias Necesarias

Para ejecutar el script es necesario instalar la siguientes librerias:
```
pip install pandas
pip install webdriver
pip install selenium
```
Para facilitar la instalación se ha dispuesto archivo requirements.txt con todas las dependencias necesarias: 

```
pip install -r requirements.txt
```

Esta versión ha sido testeada con Firefox versión [111.0.1](https://ftp.mozilla.org/pub/firefox/releases/111.0.1/ "111.0.1") utilizado geckodriver [0.32.2](https://github.com/mozilla/geckodriver/releases/tag/v0.32.2 "0.32.2"). 

# Recursos
* **Web scraping - PID_00256970**:  Una guía interna de la Universitat Oberta de Catalunya (UOC) escrita por Laia Subirats Maté y Mireia Calvo González en 2019. Este documento proporciona una introducción al web scraping y sus aplicaciones, así como ejemplos y buenas prácticas para la extracción de datos en línea.
* **Selenium**:  Documentación oficial de Selenium para Python, que proporciona información detallada sobre cómo utilizar esta biblioteca para interactuar con navegadores web y extraer datos.  https://selenium-python.readthedocs.io/
* **Web Scraping con Selenium y Python**: Un tutorial que muestra cómo realizar web scraping utilizando Selenium y Python, incluyendo cómo navegar por páginas web y extraer información de ellas. https://realpython.com/modern-web-automation-with-python-and-selenium/
* **Geckodriver y Firefox**: Información sobre cómo configurar y utilizar Geckodriver y Firefox con Selenium para realizar web scraping.  https://firefox-source-docs.mozilla.org/testing/geckodriver/
* **Análisis de datos con Python**: Un recurso que cubre diversas bibliotecas y técnicas para analizar datos en Python, incluyendo la lectura y escritura de archivos de texto plano.  https://realpython.com/python-data-analysis/