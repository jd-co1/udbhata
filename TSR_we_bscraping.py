from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import os, glob
import string
def historical_share_csv_web_scraping(option):
    if not os.path.exists(f"C:\\Users\\sheik jaheer\\OneDrive\\Desktop\\TYNYBAY\\udbhata\\udbhata-poc-main\\share_price_data\\{option.lower()}.csv"):
        chrome_options = Options()
        chrome_options.add_argument("--headless=new")
        driver = webdriver.Chrome(options=chrome_options)

        # download_directory = "C:/Users/sheik jaheer\Downloads"
        # prefs={'download.default_directory':download_directory}
        # chrome_options.add_experimental_option("prefs", prefs)

        # driver = webdriver.Chrome()
        url = "https://www.bseindia.com/"

        driver.get(url)
        driver.maximize_window()

        def wait_for_element(selector,delay=10):
            return WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, selector)))


        # option = "DRreddy"

        # Search for the company
        search = wait_for_element("/html/body/div[1]/div[5]/div/div/div[3]/div/section/form/div[1]/input")
        search.send_keys(option)
        time.sleep(2)
        search.send_keys(Keys.ENTER)
        # Scroll down the page
        driver.execute_script('document.getElementsByTagName("html")[0].style.scrollBehavior = "auto"')

        search=wait_for_element("/html/body/div[1]/div[2]/nav/div/div/ul/li[12]/a")
        search.click()

        equity=wait_for_element("/html/body/div[1]/div[4]/div/div/div/div/div/div[2]/div[2]/div[1]/div[1]/h4/a")
        equity.click()
        time.sleep(5)
        historical_share=wait_for_element("/html/body/div[1]/div[4]/div/div/div/div/div/div[2]/div[2]/div[1]/div[2]/div/ul/li[7]/a")
        historical_share.click()
        time.sleep(5)
        equity_input=wait_for_element("/html/body/div[5]/div/div/table/tbody/tr[2]/td/div/div[2]/div/div/div[2]/div/form/div/input")
        equity_input.send_keys(option)
        time.sleep(2)
        equity_input.send_keys(Keys.ENTER)
        time.sleep(2)
        radio_button=wait_for_element("/html/body/div[5]/div/div/table/tbody/tr[5]/td/table/tbody/tr/td/div/table/tbody/tr[1]/td[1]/input")
        radio_button.click()
        time.sleep(2)
        from_date="31/03/2022"
        to_date="31/03/2023"

        from_date_input=wait_for_element("/html/body/div[5]/div/div/table/tbody/tr[5]/td/table/tbody/tr/td/div/table/tbody/tr[1]/td[2]/input")
        # from_date_input.send_keys(from_date)
        driver.execute_script(f"arguments[0].value = '{from_date}';", from_date_input)


        to_date_input=wait_for_element("/html/body/div[5]/div/div/table/tbody/tr[5]/td/table/tbody/tr/td/div/table/tbody/tr[1]/td[3]/input")
        driver.execute_script(f"arguments[0].value = '{to_date}';", to_date_input)
        driver.execute_script('document.getElementsByTagName("html")[0].style.scrollBehavior = "auto"')
        submit=wait_for_element("/html/body/div[5]/div/div/table/tbody/tr[5]/td/table/tbody/tr/td/div/table/tbody/tr[4]/td/input")
        submit.click()
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

        time.sleep(2)
        download_csv=driver.find_element(By.ID,value='lnkDownload')
        download_csv.click()

        time.sleep(2)


        # Get the default download directory of the browser
        download_directory = driver.execute_script("return window.navigator.downloads ? window.navigator.downloads.directory || '' : '';")

        # Specify the new file name based on the option
        new_file_name = f"{option.lower()}.csv"  # Assuming option is in lowercase, adjust as needed

        # Find the latest downloaded file in the download directory
        list_of_files = glob.glob(os.path.join("C:\\Users\\sheik jaheer\\Downloads\\", '*'))
        latest_file = max(list_of_files, key=os.path.getctime)

        # Build the full paths for the latest and new files
        latest_file_path = os.path.join("C:\\Users\\sheik jaheer\\Downloads\\", latest_file)
        new_file_path = os.path.join("C:\\Users\\sheik jaheer\\OneDrive\\Desktop\\TYNYBAY\\udbhata\\udbhata-poc-main\\share_price_data\\", new_file_name)

        # Rename the file
        os.rename(latest_file_path, new_file_path)

        # time.sleep(5)

    else:
        print("file alredy exist")







