import undetected_chromedriver as uc
import re
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

def get_link_from_website(package_id):
    options = uc.ChromeOptions()
    options.headless = True
    driver = uc.Chrome(executable_path='./chromedriver', options=options)

    url = f"https://apkcombo.com/ru/downloader/{package_id}"
    driver.get(url)

    result_link = None

    try:
        link_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "variant.octs"))
        )
        result_link = link_element.get_attribute('href')

    except NoSuchElementException:
        print("Element not found. Please check the locators (XPATH, ID, class, etc.)")
    except TimeoutException:
        print("Timeout reached. The element could not be located.")
    finally:
        driver.quit()
        return result_link
