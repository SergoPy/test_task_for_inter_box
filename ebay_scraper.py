from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from upload_to_ingbb import upload_image_to_imgbb, save_image_from_url


def scrape_ebay_images(url):
    try:
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

        imgbb_urls = set()
        for image_url in image_urls:
            try:
                imgbb_url = upload_image_to_imgbb(
                    save_image_from_url(image_url))
                if imgbb_url:
                    imgbb_urls.add(imgbb_url)
            except Exception as upload_error:
                print(f"Error uploading image to ImgBB: {upload_error}")

        return list(imgbb_urls)

    except Exception as e:
        print(f"Error scraping eBay images: {e}")
        return None
