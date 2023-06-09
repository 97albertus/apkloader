from flask import Flask, render_template, request
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
        # Wait for the new button to appear, then locate it and get its link attribute
        link_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "variant.octs"))
        )
        result_link = link_element.get_attribute('href')

    except NoSuchElementException:
        print("Element not found. Please check the locators (XPATH, ID, class, etc.)")
    except TimeoutException:
        print("Timeout reached. The element could not be located.")
    finally:
        # Close the browser window and return the result link
        driver.quit()
        return result_link

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-link', methods=['GET'])
def get_link():
    user_input = request.args.get('input_string')
    package_id = re.search('id=(.+)', user_input)
    if package_id:
        package_id = package_id.group(1)
        result = get_link_from_website(f"#package={package_id}")
    else:
        result = None
    return {'result_link': result}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
