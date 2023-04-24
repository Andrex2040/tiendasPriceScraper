import random
import time
from time import sleep
import csv
import os
import platform
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Inicializar el contador que servira como id de registro
contador = 1

def get_driver():
    print('-> Ejecutando en Plataforma: ' + platform.system())
    print('[Exito] Espere unos segundos mientras inicia el Navegador y comienza el escaneo ...')

    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"

    options = FirefoxOptions()
    options.add_argument("--headless")  # Ejecutar en segundo plano
    options.add_argument(f'user-agent={user_agent}')

    if platform.system() == 'Windows':
        service = FirefoxService(executable_path='./geckodriver.exe')
        return webdriver.Firefox(service=service, options=options)
    elif platform.system() == 'Linux':
        service = FirefoxService(executable_path='./geckodriver_0.32.2_ubuntu')
        return webdriver.Firefox(service=service, options=options)
    else: # macOS
        service = FirefoxService(executable_path='./geckodriver_mac')
        return webdriver.Firefox(service=service, options=options)
    

def click_mostrar_mas(driver):
    boton = driver.find_element(By.XPATH, '//div[@class="vtex-button__label flex items-center justify-center h-100 ph5 "]')
    cerrarModal = driver.find_element(By.XPATH, '//span[@class="exito-geolocation-3-x-cursorPointer"]')
    cerrarModal.click()

    for i in range(40):
        try:
            boton.click()
            time.sleep(random.uniform(10.0, 20.0))
            boton = driver.find_element(By.XPATH, '//div[@class="vtex-button__label flex items-center justify-center h-100 ph5 "]')
            cerrarModal = driver.find_element(By.XPATH, '//span[@class="exito-geolocation-3-x-cursorPointer"]')
            cerrarModal.click()
        except Exception as e:
            print("hubo un error: " + str(e))
            break

def scrape_productos(driver):
    wait = WebDriverWait(driver, 1)
    productos = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@id="gallery-layout-container"]//div[@class="pointer pt3 pb4 flex flex-column h-100"]')))

    for i in range(10):
        driver.execute_script("window.scrollBy(0, 500);")
        time.sleep(1)

    return productos

def guardar_productos(productos):
    global contador
    fecha_scraping = datetime.now().strftime('%Y-%m-%d %H:%M:%S')    
    for producto in productos:
        print(contador)
        nombre = WebDriverWait(producto, 20).until(
            EC.presence_of_element_located((By.XPATH,
                                            '//div[@ class ="vtex-flex-layout-0-x-flexRow vtex-flex-layout-0-x-flexRow--product-info-container"]//div//div[@ class ="vtex-flex-layout-0-x-flexColChild vtex-flex-layout-0-x-flexColChild--product-info pb0"]//div//div//div[@ class ="pr0 items-stretch vtex-flex-layout-0-x-stretchChildrenWidth   flex"]//div[@ class ="vtex-product-summary-2-x-productBrandContainer"]//span[@class="vtex-product-summary-2-x-productBrandName"]'))
        )

        productosSplit = producto.text.split("\n")

        if len(productosSplit) > 6:
            if len(productosSplit) == 7:
                precio = productosSplit[3]
                descuento = productosSplit[4]
                precioDescuento = productosSplit[4]
            else:
                precio = productosSplit[4]
                descuento = productosSplit[3]
                precioDescuento = productosSplit[5]
        else:
           
            precio = productosSplit[3]
            descuento = 0
            precioDescuento = productosSplit[3]

        ultimas_dos = productosSplit[1].split()
        mililitros = " ".join(ultimas_dos[-2:])

        # Escribir la información en el archivo CSV
        with open('../dataset/productosExito.csv', mode='a', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow([contador, productosSplit[0], productosSplit[1], mililitros, precio, descuento, precioDescuento, fecha_scraping])

        print(len(productosSplit))
        print(productosSplit)

        contador += 1

def main():
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    driver = get_driver()
    base_url = "https://www.exito.com/licores?_q=licores&map=ft&page="

    with open('../dataset/productosExito.csv', mode='w', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['Id', 'Nombre', 'Descripcion', 'Mililitros', 'Precio', 'Descuento', 'PrecioConDescuento', 'FechaHoraScraping'])

    for page in range(1, 41):
        driver.get(base_url + str(page))
        # Tiempo de espera para carga pagina
        time.sleep(30)
        productos = scrape_productos(driver)
        guardar_productos(productos)

    driver.quit()


if __name__ == "__main__":
    main()
