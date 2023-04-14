# Práctica 1: Web scraping 

## Tecnologias

![technology Python](https://img.shields.io/badge/Python-3.x-blue.svg) ![technology Selenium](https://img.shields.io/badge/-Selenium-green?style=flat&logo=Selenium&logoColor=white)

# Integrantes

[![LinkedIn de Carlos Andrés Rivera Rivera](https://img.shields.io/badge/LinkedIn-Carlos_Andrés_Rivera_Rivera-blue?logo=linkedin&style=social)](https://www.linkedin.com/in/carlos-andres-rivera-rivera-72213069/)

[![LinkedIn de Gustavo Salgado Ocampo](https://img.shields.io/badge/LinkedIn-Gustavo_Salgado_Ocampo-blue?logo=linkedin&style=social)](https://www.linkedin.com/in/carlos-andres-rivera-rivera-72213069/)

# Descripción

| https://www.exito.com/licores?_q=licores&map=ft| https://www.tiendasjumbo.co/licores?_q=licores&map=ft |
|-------|----------|
| ![img.png](img.png) | ![img_1.png](img_1.png) | 

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

# Recursos