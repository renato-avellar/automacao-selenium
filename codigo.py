from selenium import webdriver
import time
import pandas as pd

driver = webdriver.Firefox()
driver.get('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
time.sleep(0.3)
driver.find_element('xpath', '//*[@id="email"]').send_keys('email@email.com')
time.sleep(0.3)
driver.find_element('xpath', '//*[@id="password"]').send_keys('123456')
time.sleep(0.3)
driver.find_element('xpath', '//*[@id="pgtpy-botao"]').click()

produtos = pd.read_csv('produtos.csv')

for produto in produtos.index:   
    driver.find_element('xpath', '//*[@id="codigo"]').send_keys(str(produtos.loc[produto, 'codigo']))
    time.sleep(0.3)
    driver.find_element('xpath', '//*[@id="marca"]').send_keys(str(produtos.loc[produto, 'marca']))
    time.sleep(0.3)
    driver.find_element('xpath', '//*[@id="tipo"]').send_keys(str(produtos.loc[produto, 'tipo']))
    time.sleep(0.3)
    driver.find_element('xpath', '//*[@id="categoria"]').send_keys(str(produtos.loc[produto, 'categoria']))
    time.sleep(0.3)
    driver.find_element('xpath', '//*[@id="preco_unitario"]').send_keys(str(produtos.loc[produto, 'preco_unitario']))
    time.sleep(0.3)
    driver.find_element('xpath', '//*[@id="custo"]').send_keys(str(produtos.loc[produto, 'custo']))
    time.sleep(0.3)
    if not pd.isna(produtos.loc[produto, 'obs']):
        driver.find_element('xpath', '//*[@id="obs"]').send_keys(str(produtos.loc[produto, 'obs']))
        time.sleep(0.3)
    driver.find_element('xpath', '//*[@id="pgtpy-botao"]').click() 

#time.sleep(0.3)
#driver.find_element('xpath', '//*[@id="pgtpy-botao-limpar"]').click() 