import gspread
from oauth2client.service_account import ServiceAccountCredentials


def parse_sheets_links(sheet_key, credentials_file):
    scope = ["https://spreadsheets.google.com/feeds",
             "https://www.googleapis.com/auth/drive"]

    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        credentials_file, scope)
    client = gspread.authorize(credentials)

    sheet = client.open_by_key(sheet_key).sheet1

    links = sheet.col_values(1)[2:]

    return list(links)
