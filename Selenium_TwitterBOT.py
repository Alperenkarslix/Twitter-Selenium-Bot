# Gerekli kütüphaneleri yükle
from selenium import webdriver
import time
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
# Ana Pencere
def tweetat(kullaniciadi,sifre,tweet):
    driver = webdriver.Chrome()
    driver.get("https://twitter.com/login")
    time.sleep(3)
# Kullanıcı adı ve şifrenizi girin
    username = driver.find_element(by="xpath", value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
    username.send_keys(kullaniciadi)

    next_button = driver.find_element(by="xpath", value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]')
    next_button.click()
    time.sleep(2)

    password = driver.find_element(by="xpath", value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
    password.send_keys(sifre)

    login_button = driver.find_element(by="xpath", value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div')
    login_button.click()
    time.sleep(2)
# Tweet yazın ve gönderin
    driver.get("https://twitter.com/home")
    time.sleep(3)
    tweet_box = driver.find_element(by="xpath", value="//div[@aria-label='Tweet text']//span")
    tweet_box.send_keys(tweet)
    time.sleep(3)

    tweet_button = driver.find_element(by="xpath", value="//body/div[@id='react-root']/div[1]/div[1]/div[2]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[2]/div[3]/div[1]/span[1]/span[1]")
    tweet_button.click()
    time.sleep(5)
    
def takipat(kullaniciadi,sifre,kullanici):
    driver = webdriver.Chrome()
    driver.get("https://twitter.com/login")
    time.sleep(3)
# Kullanıcı adı ve şifrenizi girin
    username = driver.find_element(by="xpath", value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
    username.send_keys(kullaniciadi)

    next_button = driver.find_element(by="xpath", value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]')
    next_button.click()
    time.sleep(2)

    password = driver.find_element(by="xpath", value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
    password.send_keys(sifre)

    login_button = driver.find_element(by="xpath", value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div')
    login_button.click()
    time.sleep(2)
# Bir Kullanıcıyı Takip Et
    driver.get("https://twitter.com/" + kullanici)
    time.sleep(3)
    driver.find_elements(by="xpath", value="//body/div[@id='react-root']/div[1]/div[1]/div[2]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]").click()
    time.sleep(3)
    
def sikayetet(kullaniciadi,sifre,kullanici):
    driver = webdriver.Chrome()
    driver.get("https://twitter.com/login")
    time.sleep(3)
# Kullanıcı adı ve şifrenizi girin
    username = driver.find_element(by="xpath", value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
    username.send_keys(kullaniciadi)

    next_button = driver.find_element(by="xpath", value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]')
    next_button.click()
    time.sleep(2)

    password = driver.find_element(by="xpath", value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
    password.send_keys(sifre)

    login_button = driver.find_element(by="xpath", value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div')
    login_button.click()
    time.sleep(2)
# Bir Kullanıcıyı Şikayet Et
    driver.get("https://twitter.com/" + kullanici)
    time.sleep(3)
    driver.find_elements(by="xpath", value="//body/div[@id='react-root']/div[1]/div[1]/div[2]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]")[0].click() # More tuşuna bas
    time.sleep(1)
    driver.find_element(by="xpath", value="//body/div[@id='react-root']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[4]").click() # Şikaye et tuşuna bas
    time.sleep(1)
    driver.find_element(by="xpath", value="//body/div[@id='react-root']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]").click() # Start a new report tuşuna bas
    time.sleep(1)
    driver.find_element(by="xpath", value="//body/div[@id='react-root']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/label[3]/div[2]/input[1]").click() # Everyone on Twitter tuşuna bas
    time.sleep(1)
    driver.find_element(by="xpath", value="//body/div[@id='react-root']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]").click() #Next tuşuna bas
    time.sleep(1)
    driver.find_element(by="xpath", value="//body/div[@id='react-root']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/label[3]/div[2]/input[1]").click() #Spammed tuşuna bas
    time.sleep(1)
    driver.find_element(by="xpath", value="//body/div[@id='react-root']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]").click() #Next tuşuna bas
    time.sleep(1)
    driver.find_element(by="xpath", value="//body/div[@id='react-root']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/label[7]/div[2]/input[1]").click() # Somthing else tuşuna bas
    time.sleep(1)
    driver.find_element(by="xpath", value="//body/div[@id='react-root']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]").click() # Next tuşuna bas
    time.sleep(1)
    driver.find_element(by="xpath", value="//body/div[@id='react-root']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]").click() # Yes Confirm tuşuna bas
    time.sleep(1)
    driver.find_element(by="xpath", value="//body/div[@id='react-root']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]").click() # Submit tuşuna bas
    time.sleep(1)
    driver.find_element(by="xpath", value="//body/div[@id='react-root']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]").click() # Done tuşuna bas
    time.sleep(3)
    
def tweetelikeat(kullaniciadi,sifre,kullanici, tweet):
    driver = webdriver.Chrome()
    driver.get("https://twitter.com/login")
    time.sleep(3)
# Kullanıcı adı ve şifrenizi girin
    username = driver.find_element(by="xpath", value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
    username.send_keys(kullaniciadi)

    next_button = driver.find_element(by="xpath", value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]')
    next_button.click()
    time.sleep(2)

    password = driver.find_element(by="xpath", value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
    password.send_keys(sifre)

    login_button = driver.find_element(by="xpath", value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div')
    login_button.click()
    time.sleep(2)
    driver.get("https://twitter.com/"+kullanici + "/status/" + tweet)
    time.sleep(3)
    driver.find_element(by="xpath", value="//body/div[@id='react-root']/div[1]/div[1]/div[2]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/article[1]/div[1]/div[1]/div[3]/div[7]/div[1]/div[3]/div[1]").click()
    time.sleep(3)   
    
def ilktweetelikeat(kullaniciadi,sifre,kullanici):
    driver = webdriver.Chrome()
    driver.get("https://twitter.com/login")
    time.sleep(3)
# Kullanıcı adı ve şifrenizi girin
    username = driver.find_element(by="xpath", value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
    username.send_keys(kullaniciadi)

    next_button = driver.find_element(by="xpath", value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]')
    next_button.click()
    time.sleep(2)

    password = driver.find_element(by="xpath", value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
    password.send_keys(sifre)

    login_button = driver.find_element(by="xpath", value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div')
    login_button.click()
    time.sleep(2)
    driver.get("https://twitter.com/"+kullanici)
    time.sleep(3)
    driver.find_element(by="xpath", value="//body/div[@id='react-root']/div[1]/div[1]/div[2]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/article[1]/div[1]/div[1]/div[2]/div[2]/div[4]/div[1]/div[3]/div[1]").click()
    time.sleep(3)   
    
def tweetiretweetet(kullaniciadi,sifre,kullanici, tweet):
    driver = webdriver.Chrome()
    driver.get("https://twitter.com/login")
    time.sleep(3)
# Kullanıcı adı ve şifrenizi girin
    username = driver.find_element(by="xpath", value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
    username.send_keys(kullaniciadi)

    next_button = driver.find_element(by="xpath", value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]')
    next_button.click()
    time.sleep(2)

    password = driver.find_element(by="xpath", value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
    password.send_keys(sifre)

    login_button = driver.find_element(by="xpath", value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div')
    login_button.click()
    time.sleep(2)
    driver = webdriver.Chrome()
    driver.get("https://twitter.com/"+kullanici + "/status/" + tweet)
    time.sleep(3)
    driver.find_element(by="xpath", value="//body/div[@id='react-root']/div[1]/div[1]/div[2]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/article[1]/div[1]/div[1]/div[3]/div[7]/div[1]/div[2]/div[1]").click()
    time.sleep(3)  
    driver.find_element(by="xpath", value="//body/div[@id='react-root']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]").click()
    time.sleep(3)
    
