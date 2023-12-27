from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from upload_to_ingbb import upload_image_to_imgbb, save_image_from_url


def scrape_ebay_images(url):
    with webdriver.Chrome() as driver:
        driver.get(url)

        wait = WebDriverWait(driver, 10)

        image_elements = wait.until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "div.ux-image-carousel-item img[data-zoom-src]"))
        )

        image_urls = {
            image_element.get_attribute(
                "data-zoom-src") or image_element.get_attribute("src")
            for image_element in image_elements
        }

    imgbb_urls = [
        upload_image_to_imgbb(save_image_from_url(image_url))
        for image_url in image_urls if image_url
    ]

    return [url for url in imgbb_urls if url]
