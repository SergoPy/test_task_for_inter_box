from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def scrape_ebay_images(url):
    driver = webdriver.Chrome()

    driver.get(url)

    wait = WebDriverWait(driver, 10)

    image_elements = wait.until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "div.ux-image-carousel-item img[data-zoom-src]"))
    )

    image_urls = set()
    for image_element in image_elements:
        zoom_src = image_element.get_attribute("data-zoom-src")
        src = image_element.get_attribute("src")

        image_url = zoom_src if zoom_src else src

        if image_url:
            image_urls.add(image_url)

    driver.quit()

    return list(image_urls)
