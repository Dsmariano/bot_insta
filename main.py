from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
#import pandas as pd
import os
from time import sleep
from random import randint
import requests

options = webdriver.ChromeOptions()
# options.add_argument("--headless=false")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

url = 'https://www.instagram.com/'

driver.get(url)
sleep(5)
INSTAGRAM_USER_NAME = os.environ['INSTAGRAM_USER_NAME']
INSTAGRAM_PASSWORD = os.environ['INSTAGRAM_PASSWORD']

usuario = driver.find_element('name', "username")
sleep(2)
usuario.send_keys(INSTAGRAM_USER_NAME) # aqui vai seu usuario do instragram
sleep(3)
senha = driver.find_element('name', "password")
senha.send_keys(INSTAGRAM_PASSWORD) # aqui vai sua senha do instragram

sleep(3)

driver.find_element('xpath','//*[@id="loginForm"]/div/div[3]/button/div').click()

hashtag_list = ['betimcity']

novos_users_seguidos = []

tag = -1
seguindo = 0
likes = 0
comentarios = 0



for hashtag in hashtag_list:
    tag = tag + 1
    tamb = '(//*[@class="_aagw"])[1]'
    texto_seguir = "//*[@class='_aacl _aaco _aacw _aad6 _aade']"
    # curti = "(//*[@class='x6s0dn4 x78zum5 xdt5ytf xl56j7k'])[3]"
    # comentar = "(//*[@class='x6s0dn4 x78zum5 xdt5ytf xl56j7k'])[4]"
    primeira_avanca = '(//*[@class="_abm0"])[1]'
    avanca = '(//*[@class="_abm0"])[2]'
    #tamb = "//*[@class='_aagw'][1]"
    sleep(3)
    driver.get('https://www.instagram.com/explore/tags/' + hashtag_list[tag] + '/')
    sleep(5)
    
    driver.find_element('xpath', tamb).click()
    driver.find_element('xpath', primeira_avanca).click()
    #primeira_thumb.click()
    
    sleep(randint(2,3))
    try:
        for _ in range(1,25):
            try:
                follow_usuario = driver.find_element('xpath', texto_seguir).text
            except:
                print("Já seguindo")
                driver.find_element('xpath', avanca).click()
                continue
            
            if follow_usuario is not None:
                if driver.find_element('xpath', texto_seguir).text == 'Seguir' or 'Follow':
                    driver.find_element('xpath', texto_seguir).click()
                    novos_users_seguidos.append(follow_usuario)
                    seguindo = seguindo + 1
                    #Like
                    curti = "(//*[@class='x6s0dn4 x78zum5 xdt5ytf xl56j7k'])[3]"
                    buttton_like = driver.find_element('xpath', curti).click()
                    # buttton_like.click()
                    likes = likes + 1
                    sleep(randint(2,3))
                    driver.find_element('xpath', avanca).click()
                    sleep(randint(1, 2))   
                    # break 
            else:
                driver.find_element('xpath', avanca).click()
                sleep(randint(1, 2)) 
                #driver.find_element_by_link_text('Avançar').click()
                #sleep(randint(1, 2))
                #driver.find_element_by_link_text('Próximo').click()
                #sleep(randint(1, 2))
    
    except:
        continue

print('Liked {} fotos.'.format(likes))
print('Comentários {} fotos.'.format(comentarios))
print('Seguindo {} pessoas novas.'.format(seguindo))

likeds = 'Liked {} fotos.'.format(likes)
total_comentarios = 'Comentários {} fotos.'.format(comentarios)
total_seguindos = 'Seguindo {} pessoas novas.'.format(seguindo)

print(likes, total_comentarios, total_seguindos)