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

driver.get('https://www.exito.com/licores?_q=licores&map=ft')
wait = WebDriverWait(driver, 1) # espera explícita de 1 segundos

with open('productosExito.csv', mode='w', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['Id', 'Nombre', 'Descripcion', 'Mililitros', 'Precio', 'Descuento', 'PrecioConDescuento'])

sleep(5)
boton = driver.find_element(By.XPATH, '//div[@class="vtex-button__label flex items-center justify-center h-100 ph5 "]')

cerrarModal = driver.find_element(By.XPATH, '//span[@class="exito-geolocation-3-x-cursorPointer"]')
cerrarModal.click()

for i in range(40):
    try:
        boton.click()
        sleep(random.uniform(10.0, 20.0))
        boton = driver.find_element(By.XPATH, '//div[@class="vtex-button__label flex items-center justify-center h-100 ph5 "]')
        cerrarModal = driver.find_element(By.XPATH, '//span[@class="exito-geolocation-3-x-cursorPointer"]')
        cerrarModal.click()
    except:
        print("hubo un error")
        break

productos = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@id="gallery-layout-container"]//div[@class="pointer pt3 pb4 flex flex-column h-100"]')))

for i in range(10):
    driver.execute_script("window.scrollBy(0, 500);")
    time.sleep(1)

contador = 1
for producto in productos:
    print(contador)
    nombre = WebDriverWait(producto, 20).until(
        EC.presence_of_element_located((By.XPATH,
                                        '//div[@ class ="vtex-flex-layout-0-x-flexRow vtex-flex-layout-0-x-flexRow--product-info-container"]//div//div[@ class ="vtex-flex-layout-0-x-flexColChild vtex-flex-layout-0-x-flexColChild--product-info pb0"]//div//div//div[@ class ="pr0 items-stretch vtex-flex-layout-0-x-stretchChildrenWidth   flex"]//div[@ class ="vtex-product-summary-2-x-productBrandContainer"]//span[@class="vtex-product-summary-2-x-productBrandName"]'))
    )

    productosSplit = producto.text.split("\n")


    if len(productosSplit)>6:
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
    with open('productosExito.csv', mode='a', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([contador, productosSplit[0], productosSplit[1], mililitros, precio, descuento, precioDescuento])

    print(len(productosSplit))
    print(productosSplit)

    contador+=1

#driver.quit()