from flask import Flask, render_template, request
import undetected_chromedriver as uc
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

def get_link_from_website(input_string):
    # Set up the WebDriver (change 'PATH' to the location of your WebDriver)
    options = uc.ChromeOptions()
    options.headless = True  # You can set this to True if you want to run Chrome in headless mode
    driver = uc.Chrome(executable_path='/usr/local/bin/chromedriver', options=options)

    # Navigate to the website
    url = "https://apps.evozi.com/apk-downloader/"  # Replace with the target website's URL
    driver.get(url)

    result_link = None  # Initialize the result_link variable before the try-except block

    try:
        # Locate the text box and button elements using their xpath, id, class, or other attributes
        text_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//input[@type="text"]')))  # Adjust as needed
        submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//button[@class="btn btn-lg btn-block btn-info mt-4 mb-4"]')))  # Adjust as needed

        # Enter the input_string into the text box and click the submit button
        text_box.send_keys(input_string)
        submit_button.click()

        # Wait for the new button to appear, then locate it and get its link attribute
        new_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[@class="btn btn-success btn-block mt-4 mb-4"]')))  # Adjust as needed
        result_link = new_button.get_attribute("href")

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

@app.route('/get-link', methods=['POST'])
def get_link():
    user_input = request.form['input_string']
    result = get_link_from_website(user_input)
    return {'result_link': result}

if __name__ == '__main__':
    app.run(debug=True)
