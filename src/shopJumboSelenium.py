import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

# xattr -d com.apple.quarantine chromedriver - activar driver en mac
driver = webdriver.Firefox(executable_path='./geckodriver')

driver.get('https://www.tiendasjumbo.co/licor?_q=licor&map=ft')
wait = WebDriverWait(driver, 1) # espera explícita de 10 segundos

with open('productosJumbo.csv', mode='w', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['Id', 'Nombre', 'Descripcion', 'Mililitros', 'Precio', 'Descuento', 'PrecioConDescuento'])

productos = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@id="gallery-layout-container"]')))

posicion = 2
contador = 1
while True:
    for i in range(10):
        driver.execute_script("window.scrollBy(0, 500);")
        time.sleep(1)

    for producto in productos:
        productosSplit = producto.text.split("Comparar")

        productosSplit.pop()

        contadorSplit = 1

        for proSplit in productosSplit:
            productoSplit = proSplit.split("\n")
            print(productoSplit)
            if contadorSplit == 1:
                if len(productoSplit) > 10:
                    descuento = productoSplit[0]
                    nombreProducto = productoSplit[2]
                    descripcion = productoSplit[3]
                    precio = productoSplit[5]
                    precioDescuento = productoSplit[7]
                    ultima = productoSplit[1].split()
                    mililitros = " ".join(ultima[-1:])
                else:
                    descuento = 0
                    nombreProducto = productoSplit[1]
                    descripcion = productoSplit[0]
                    precio = productoSplit[2]
                    ultima = productoSplit[0].split()
                    mililitros = " ".join(ultima[-1:])
                    precioDescuento = productoSplit[2]
            else:
                if len(productoSplit) > 10:
                    descuento = productoSplit[1]
                    nombreProducto = productoSplit[3]
                    descripcion = productoSplit[2]
                    precio = productoSplit[5]
                    precioDescuento = productoSplit[8]
                    ultima = productoSplit[2].split()
                    mililitros = " ".join(ultima[-1:])
                else:
                    descuento = productoSplit[0]
                    nombreProducto = productoSplit[2]
                    descripcion = productoSplit[1]
                    precio = productoSplit[3]
                    ultima = productoSplit[1].split()
                    mililitros = " ".join(ultima[-1:])

            contadorSplit += 1

            # Escribir la información en el archivo CSV
            with open('productosJumbo.csv', mode='a', encoding='utf-8') as file:
                writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                writer.writerow([contador, nombreProducto, descripcion, mililitros, precio, descuento, precioDescuento])

            contador += 1

    try:
        botonPagina = driver.find_element(By.XPATH, '//li[@class="inline-flex h-100 relative overflow-hidden"][' + str(posicion) + ']')
        botonPagina.click()
        posicion += 1
    except:
        break

#driver.quit()