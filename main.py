from sheets_parser import parse_sheets_links
from ebay_scraper import scrape_ebay_images
from add_data import write_links_to_sheets


def main():
    sheet_key = "16ttuOesg_JfIUGcRYo01L--VBDemQolcp1FruSv3t44"
    credentials_file = "credentials.json"

    ebay_links = parse_sheets_links(sheet_key, credentials_file)
    for ebay_link in ebay_links:
        image_urls = scrape_ebay_images(ebay_link)
        write_links_to_sheets(sheet_key, image_urls)


if __name__ == "__main__":
    main()
