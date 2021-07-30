# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def test_is_contain_BEST():
    options = webdriver.ChromeOptions()
    options.add_argument("--remote-debugging-port=9225")
    options.binary_location = 'C:\\Users\\Sultan\\Downloads\\GoogleChromePortable\\GoogleChromePortable.exe'
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    #options.debugger_address="127.0.0.1:9225"
    driver = webdriver.Chrome(executable_path='C:\\chromedriver', chrome_options=options)
    driver.implicitly_wait(30)
    driver.get("http://127.0.0.1:5000/")
    driver.find_element_by_link_text("Contact").click()
    codehtml = driver.page_source

    #Cherche 'BEST' dans le code source de la page
    assert 'BEST' in codehtml

    #Lister les élements qui continnent 'BEST'
    list_elements = driver.find_elements_by_xpath("//*[contains(text(), 'BEST')]")
    assert len(list_elements) > 0

    #Lister les élements qui sont de type p
    list_elements = driver.find_elements_by_css_selector("p")
    #2ème élément
    assert 'BEST' in list_elements[1].text

    #Récupérer le 2ème paragraphe qui lui contient 'BEST'
    assert 'BEST' in driver.find_element_by_css_selector('p:nth-child(2)').text

    #Bonne pratique : utiliser les id dans le code HTML car plus simple et plus efficace 
    #Récupérer l'élément dont l'id = pbest  <p id="pbest"></p>
    assert 'BEST' in driver.find_element_by_css_selector('#pbest').text


    driver.close()
