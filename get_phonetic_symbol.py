from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pyperclip


options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--single-process')
options.add_argument('--disable-application-cache')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--blink-settings=imagesEnabled=false')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

try:
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(options=options, service=service)
    while True:
        tango = input("発音記号をコピーしたい英単語を入力してください。'q'を入力すると終了します。：")
        if tango == 'q':
            break
        driver.get('https://eow.alc.co.jp/search?q=' + tango)
        kigo = driver.find_element(By.CLASS_NAME, "pron")
        pyperclip.copy(kigo.text[:-1])
        print(tango + "の発音記号をコピーしました\n")
    driver.quit()
except:
    driver.quit()