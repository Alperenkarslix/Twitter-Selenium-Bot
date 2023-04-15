# Gerekli kütüphaneleri yükle
from selenium import webdriver
import time
from tkinter import *
from mttkinter import mtTkinter as tk
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
    
if __name__ == "__main__":

    def tweetatma():
        tweetat(kullaniciaditut.get(), sifretut.get(), tweettut.get())
    def takipatma():
        takipat(kullaniciaditut.get(), sifretut.get(), takipicinkullaniciaditut.get())
    def sikayetetme():
        sikayetet(kullaniciaditut.get(), sifretut.get(), sikayeticinkullaniciaditut.get())
    def ilktweetelikeatma():
        ilktweetelikeat(kullaniciaditut.get(), sifretut.get(), likeicinkullaniciaditut.get())
    def tweetelikeatma():
        tweetelikeat(kullaniciaditut.get(), sifretut.get(), tweetlikeicinkullaniciaditut.get(), tweetlikeicinidtut.get() )
    def tweetiretweetetma():
        tweetiretweetet(kullaniciaditut.get(), sifretut.get(), tweetrticinkullaniciaditut.get(), tweetrticinidtut.get() )
    window = Tk()
    window.title("Alperen Twitter BOT")
    lbl = Label(window, text="Kullanıcı Adı:")
    lbl2 = Label(window, text="Şifre:")
    lbl.grid(column=0, row=0)
    lbl2.grid(column=2, row=0)
    kullaniciaditut = tk.StringVar(window)
    kullaniciadigir = Entry(window,textvariable = kullaniciaditut, width=10)
    kullaniciadigir.grid(column=1, row=0)
    sifretut = tk.StringVar(window)
    sifregir = Entry(window,textvariable = sifretut, width=10, show="*")
    sifregir.grid(column=3, row=0)
    lbl3 = Label(window, text="İşlem Seçiniz:")
    lbl3.grid(column=0, row=1)
    lbl4 = Label(window, text="Tweet:")
    lbl4.grid(column=0, row=2)
    tweettut =tk.StringVar(window)
    txt3 = Entry(window,textvariable = tweettut, width=10)
    txt3.grid(column=1, row=2)
    btn2 = Button(window, text="Tweet At", command=tweetatma)
    btn2.grid(column=2, row=2)

    lbl5 = Label(window, text="Kullanıcı Adı:")
    lbl5.grid(column=0, row=3)
    takipicinkullaniciaditut =tk.StringVar(window)
    txt3 = Entry(window,textvariable=takipicinkullaniciaditut, width=10)
    txt3.grid(column=1, row=3)
    btn3 = Button(window, text="Takip Et", command=takipatma)
    btn3.grid(column=2, row=3)

    lbl6 = Label(window, text="Kullanıcı Adı:")
    lbl6.grid(column=0, row=4)
    sikayeticinkullaniciaditut =tk.StringVar(window)
    txt4 = Entry(window,textvariable=sikayeticinkullaniciaditut, width=10)
    txt4.grid(column=1, row=4)
    btn4 = Button(window, text="Şikayet Et", command=sikayetetme)
    btn4.grid(column=2, row=4)

    lbl7 = Label(window, text="Kullanıcı Adı:")
    lbl7.grid(column=0, row=5)
    likeicinkullaniciaditut =tk.StringVar(window)
    txt5 = Entry(window,textvariable=likeicinkullaniciaditut, width=10)
    txt5.grid(column=1, row=5)
    btn5 = Button(window, text="İlk Tweete Like At", command=ilktweetelikeatma)
    btn5.grid(column=2, row=5)

    lbl8 = Label(window, text="Kullanıcı Adı:")
    lbl8.grid(column=0, row=6)
    tweetlikeicinkullaniciaditut =tk.StringVar(window)
    txt6 = Entry(window,textvariable=tweetlikeicinkullaniciaditut, width=10)
    txt6.grid(column=1, row=6)
    lbl9 = Label(window, text="Tweet ID:")
    lbl9.grid(column=2, row=6)
    tweetlikeicinidtut =tk.StringVar(window)
    txt7 = Entry(window,textvariable=tweetlikeicinidtut, width=10)
    txt7.grid(column=3, row=6)
    btn6 = Button(window, text="Tweete Like At", command=tweetelikeatma)
    btn6.grid(column=4, row=6)

    lbl9 = Label(window, text="Kullanıcı Adı:")
    lbl9.grid(column=0, row=7)
    tweetrticinkullaniciaditut =tk.StringVar(window)
    txt7 = Entry(window,textvariable=tweetrticinkullaniciaditut, width=10)
    txt7.grid(column=1, row=7)
    lbl10 = Label(window, text="Tweet ID:")
    lbl10.grid(column=2, row=7)
    tweetrticinidtut =tk.StringVar(window)
    txt8 = Entry(window,textvariable=tweetrticinidtut, width=10)
    txt8.grid(column=3, row=7)
    btn7 = Button(window, text="Tweeti Retweet Et", command=tweetiretweetetma)
    btn7.grid(column=4, row=7)
    window.geometry('700x300')
    window.mainloop()