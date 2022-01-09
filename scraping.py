from time import sleep
from selenium import webdriver  # Import from seleniumwire
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import pandas as pd
import os

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# di den trang ho tro chong dich thua thien hue
driver.get('https://tcs.thuathienhue.gov.vn/')
sleep(0.5)

# nhap tai khoan mat khau va dang nhap
driver.find_element_by_name('txtUser').send_keys("eggtgg")
txt_pass = driver.find_element_by_name('txtPass')
#9pabK7cKNf4@dcU
txt_pass.send_keys('9pabK7cKNf4@dcU')
sleep(0.5)

txt_pass.send_keys(Keys.ENTER)
sleep(1)

driver.get('https://tcs.thuathienhue.gov.vn/tcs?id=9')
sleep(0.5)

# loc ra du lieu o thua thien hue
select = Select(driver.find_element_by_name('ctl06$DanhMucCapDoDich_TraCuu$drpTinhThanhPho'))
select.select_by_value('46')
sleep(0.5)

# luu du lieu HTML
page_source = driver.page_source

# dong trinh duyet
driver.close()

# Phan tich HTML
soup = BeautifulSoup(page_source, 'html.parser')
links = soup.find_all('div',attrs={'class':"dong-huyen"})

# Loc du lieu
huyen = []
xa = []
thon = []
cap = []
for link in links:
    ten_huyen = link.find('div', attrs={'class':"cot-tenhuyen"}).text
    cac_xa = link.find_all('div',attrs={'class':'cot1-tenxa'})
    cac_thon_trong_xa = link.find_all('div', attrs={'class':"cot2-thon"})
    for i in range(len(cac_xa)):
        ten_xa = cac_xa[i].text
        cac_thon = cac_thon_trong_xa[i].find_all('div')
        for thon_i in cac_thon:
            ten_thon = thon_i.text
            cap_do = thon_i.get('class')[0]
            
            huyen.append(ten_huyen)
            xa.append(ten_xa)
            thon.append(ten_thon)
            cap.append(int(cap_do[-1]))


# Xuat du lieu ra
os.chdir('data')
data = {'huyen':huyen, 'xa':xa, 'thon':thon, 'cap':cap}
df = pd.DataFrame(data)
export_csv = df.to_csv ('ban_mau_1_9_21.csv', index = None, header=True, encoding='utf-8')