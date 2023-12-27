from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
from io import BytesIO
from PIL import Image
import os
import time


def save_image_from_url(url):
    response = requests.get(url)

    parts = url.split("/")
    desired_part = parts[-2] + parts[-1].split("-")[1]
    save_path = "temporary_files/" + desired_part

    img = Image.open(BytesIO(response.content))
    img.save(save_path)

    return save_path


def delete_image(file_path):
    try:
        os.remove(file_path)
        print(f"File '{file_path}' successfully deleted.")
    except FileNotFoundError:
        print(f"File '{file_path}' not found. Unable to delete.")
    except Exception as e:
        print(f"An error occurred while deleting the file '{file_path}': {e}")


def upload_image_to_imgbb(image_path):
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-extensions')
    options.add_argument('--headless')  
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')

    driver = webdriver.Chrome()
    pause_time = 1.5

    try:
        driver.get("https://imgbb.com/")

        wait = WebDriverWait(driver, 10)
        upload_input = wait.until(
            EC.presence_of_element_located((By.ID, "anywhere-upload-input"))
        )

        upload_input.send_keys(os.path.abspath(image_path))

        upload_btn = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[@data-action='upload']"))
        )

        body = driver.find_element(By.TAG_NAME, "button")
        body.send_keys(Keys.END)

        upload_btn.click()

        time.sleep(pause_time)

        uploaded_image_url = wait.until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "image-link"))
        ).get_attribute("href")

        delete_image(image_path)

        return uploaded_image_url
    finally:
        driver.quit()
