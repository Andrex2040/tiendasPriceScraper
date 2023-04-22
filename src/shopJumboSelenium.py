import csv
import os
import platform
import random
from datetime import datetime
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def random_sleep(min_sec=3, max_sec=10):
    sleep(random.uniform(min_sec, max_sec))

def get_driver(user_agent):
    print('-> Ejecutando en Plataforma: ' + platform.system())
    print('[Jumbo] Espere unos segundos mientras inicia el Navegador y comienza el escaneo ...')

    options = FirefoxOptions()
    #options.add_argument("--headless")  # Ejecutar en segundo plano
    options.add_argument(f'user-agent={user_agent}')  # Agregar el user agent

    if platform.system() == 'Windows':
        service = FirefoxService(executable_path='./geckodriver.exe')
        return webdriver.Firefox(service=service, options=options)
    elif platform.system() == 'Linux':
        service = FirefoxService(executable_path='./geckodriver_0.32.2_ubuntu')
        return webdriver.Firefox(service=service, options=options)
    else:  # macOS
        service = FirefoxService(executable_path='./geckodriver_mac')
        return webdriver.Firefox(service=service, options=options)


def get_user_agents():
    return [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.1 Safari/605.1.15',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:61.0) Gecko/20100101 Firefox/61.0',
        'Mozilla/5.0 (X11; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0',
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0',        
    ]

def get_random_user_agent():
    user_agents = get_user_agents()
    return random.choice(user_agents)

def update_user_agent(driver):
    random_user_agent = get_random_user_agent()
    driver.execute_script(f"Object.defineProperty(navigator, 'userAgent', {{get: function () {{return '{random_user_agent}';}},}});")


def scrape_productos(driver):
    wait = WebDriverWait(driver, 60)
    productos = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@id="gallery-layout-container"]')))
    return productos

def guardar_productos(driver):
    posicion = 2
    contador = 1
    fecha_scraping = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    while True:
        for i in range(4):
            driver.execute_script("window.scrollBy(0, 500);")
            random_sleep(18, 30)

        productos = scrape_productos(driver)

        for producto in productos:
            productos_split = producto.text.split("Comparar")
            productos_split.pop()
            contador_split = 1

            for pro_split in productos_split:
                producto_split = pro_split.split("\n")
                print(producto_split)
                if contador_split == 1:
                    if len(producto_split) > 10:
                        descuento = producto_split[0]
                        nombre_producto = producto_split[2]
                        descripcion = producto_split[3]
                        precio = producto_split[5]
                        precio_descuento = producto_split[7]
                        ultima = producto_split[1].split()
                        mililitros = " ".join(ultima[-1:])
                    else:
                        descuento = 0
                        nombre_producto = producto_split[1]
                        descripcion = producto_split[0]
                        precio = producto_split[2]
                        ultima = producto_split[0].split()
                        mililitros = " ".join(ultima[-1:])
                        precio_descuento = producto_split[2]
                else:
                    if len(producto_split) > 10:
                        descuento = producto_split[1]
                        nombre_producto = producto_split[3]
                        descripcion = producto_split[2]
                        precio = producto_split[5]
                        precio_descuento = producto_split[8]
                        ultima = producto_split[2].split()
                        mililitros = " ".join(ultima[-1:])
                    else:
                        descuento = producto_split[0]
                        nombre_producto = producto_split[2]
                        descripcion = producto_split[1]
                        precio = producto_split[3]
                        ultima = producto_split[1].split()
                        mililitros = " ".join(ultima[-1:])

                contador_split += 1

                # Escribir la información en el archivo CSV
                with open('productosJumbo.csv', mode='a', encoding='utf-8') as file:
                    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    writer.writerow([contador, nombre_producto, descripcion, mililitros, precio, descuento, precio_descuento, fecha_scraping])

                contador += 1

        try:
            boton_pagina = driver.find_element(By.XPATH, '//li[@class="inline-flex h-100 relative overflow-hidden"][' + str(posicion) + ']')           
            boton_pagina.click()
            posicion += 1
        except:
            break

        print('pagina ? ' + str(posicion))    

def main():
    base_url = "https://www.tiendasjumbo.co/licor?_q=licor&map=ft"

    # Agregar encabezado
    with open('productosJumbo.csv', mode='w', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['Id', 'Nombre', 'Descripcion', 'Mililitros', 'Precio', 'Descuento', 'PrecioConDescuento', 'FechaHoraScraping'])

    # Crear un controlador con un user agent aleatorio y cargar la primera página
    driver = get_driver(get_random_user_agent())
    driver.get(base_url)    

    guardar_productos(driver)
    
    driver.quit()

    posicion = 2
    while True:
        # Crear un nuevo controlador con un user agent aleatorio y cargar la siguiente página
        driver = get_driver(get_random_user_agent())
        driver.get(f"{base_url}&page={posicion}")
        
        guardar_productos(driver)
        
        driver.quit()

        # Incrementar la posición para la siguiente página
        posicion += 1


if __name__ == "__main__":
    main()

