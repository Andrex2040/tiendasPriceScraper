import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# xattr -d com.apple.quarantine chromedriver - activar driver en mac
driver = webdriver.Firefox(executable_path='./geckodriver')


driver.get('https://www.exito.com/licores?_q=licores&map=ft')
wait = WebDriverWait(driver, 60) # espera explícita de 10 segundos

#productos = driver.find_elements_by_xpath('//div[@id="gallery-layout-container"]//div[@class="pointer pt3 pb4 flex flex-column h-100"]')
productos = driver.find_elements(By.XPATH, '//div[@id="gallery-layout-container"]//div[@class="pointer pt3 pb4 flex flex-column h-100"]')

for producto in productos:

    nombre = WebDriverWait(producto, 20).until(
        EC.presence_of_element_located((By.XPATH,
                                        '//div[@ class ="vtex-flex-layout-0-x-flexRow vtex-flex-layout-0-x-flexRow--product-info-container"]//div//div[@ class ="vtex-flex-layout-0-x-flexColChild vtex-flex-layout-0-x-flexColChild--product-info pb0"]//div//div//div[@ class ="pr0 items-stretch vtex-flex-layout-0-x-stretchChildrenWidth   flex"]//div[@ class ="vtex-product-summary-2-x-productBrandContainer"]//span[@class="vtex-product-summary-2-x-productBrandName"]'))
    )

    #nombre = producto.find_element(By.XPATH, '//div[@ class ="vtex-flex-layout-0-x-flexRow vtex-flex-layout-0-x-flexRow--product-info-container"]//div//div[@ class ="vtex-flex-layout-0-x-flexColChild vtex-flex-layout-0-x-flexColChild--product-info pb0"]//div//div//div[@ class ="pr0 items-stretch vtex-flex-layout-0-x-stretchChildrenWidth   flex"]//div[@ class ="vtex-product-summary-2-x-productBrandContainer"]//span[@class="vtex-product-summary-2-x-productBrandName"]')
    #print(nombre)
    print(producto.text)

driver.quit()