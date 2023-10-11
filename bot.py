from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
#import pandas as pd
import os
from time import sleep
from random import randint
import requests

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

url = 'https://www.instagram.com/'

driver.get(url)

sleep(10)

usuario = driver.find_element('name', "username")
sleep(2)
usuario.send_keys('globalplusmg')
sleep(3)
senha = driver.find_element('name', "password")
senha.send_keys('@globaloz')

sleep(3)

driver.find_element('xpath','//*[@id="loginForm"]/div/div[3]/button/div').click()

hashtag_list = ['igarape']

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
    driver.get('https://www.instagram.com/explore/tags/' + hashtag_list[tag] + '/')
    sleep(5)
    
    driver.find_element('xpath', tamb).click()
    driver.find_element('xpath', primeira_avanca).click()
    #primeira_thumb.click()
    
    sleep(randint(2,3))
    try:
        for _ in range(1,200):
            
            
            sleep(randint(1, 2)) 
            usuario = driver.find_element('xpath', texto_seguir).text
            
            if usuario not in novos_users_seguidos:
                
                if driver.find_element('xpath', texto_seguir).text == 'Seguir':
                    driver.find_element('xpath', texto_seguir).click()
                    novos_users_seguidos.append(usuario)
                    seguindo = seguindo + 1
                    
                    #Like
                    curti = "(//*[@class='x6s0dn4 x78zum5 xdt5ytf xl56j7k'])[3]"
                    buttton_like = driver.find_element('xpath', curti).click()
                    buttton_like.click()
                    likes = likes + 1
                    sleep(randint(2,3))

                    #comentario
                    # driver.find_element('xpath', "(//*[@class='x6s0dn4 x78zum5 xdt5ytf xl56j7k'])[4]").click()
                    # comment_box = driver.find_element('xpath','/html/body/div[5]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/div/textarea')

                    # com = randint(1, 10)
                    # if com < 6:
                    #     comment_box.send_keys('Muito  Legal!')
                    #     sleep(2)
                    # elif com > 6 and com < 9:
                    #     comment_box.send_keys('Top!')
                    #     sleep(2)    
                    # elif com == 10:
                    #     comment_box.send_keys('Muito Top!')
                    #     sleep(2)    
                    # comment_box.send_keys(Keys.ENTER)
                    # comentarios = comentarios +1
                    # sleep(randint(1,3))

                driver.find_element('xpath', avanca).click()
                sleep(randint(1, 2))    
                # elif driver.find_element('xpath', texto_seguir):
                #     driver.find_element('xpath', avanca).click()
                #     sleep(randint(1, 2)) 
                # else:
                #     driver.find_element('xpath', avanca).click()
                #     sleep(randint(1, 2)) 
          
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