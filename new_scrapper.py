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

new_planets_data=[]

def scrape_more_data(hyperlink):
    """"""

planet_df_1 = pd.read_csv("scaraped_data.csv")

for index, row in planet_df_1.iterrows():
    print(row['hyperlink'])
    scrape_more_data(row['hyperlink'])