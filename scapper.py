import time 
import pandas as pd

from selenium import webdriver 
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=service)


START_URL = "https://exoplanets.nasa.gov/exoplanet-catalog/"
driver.get(START_URL)

time.sleep(10)

planets_data=[]

def scrape():
    for i in range(0,10):
        soup=BeautifulSoup(driver.page_source, "html.parser")
        print(f'Scrapping page {i+1} ...' )

        for ul_tag in soup.find_all("ul" ,attrs = {"class", "exoplanet"}):
            li_tags = ul_tag.find_all("li")
            temp_list = []

            for index, li_tag in enumerate(li_tags):
                if index == 0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except: 
                        temp_list.append("")
                
            hyperlink_li_tag = li_tags[0] 
            temp_list.append("https://exoplanets.nasa.gov"+ hyperlink_li_tag.find_all("a", href=True)[0]["href"])      
            planets_data.append(temp_list)
        
        driver.find_element(By.XPATH, value = '//*[@id="primary_column"]/div[1]/div[2]/div[1]/div/nav/span[2]/a').click()

scrape()

headers = ["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date", "hyperlink"]

planet_df_1 = pd.DataFrame(planets_data, columns= headers)

planet_df_1.to_csv('scaraped_data.csv', index = True, index_label="id")


        