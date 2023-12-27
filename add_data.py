import gspread
from oauth2client.service_account import ServiceAccountCredentials


def write_links_to_sheets(sheet_key, photo_links):
    scope = ["https://spreadsheets.google.com/feeds",
             "https://www.googleapis.com/auth/drive"]
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        "credentials.json", scope)
    client = gspread.authorize(credentials)

    sheet = client.open_by_key(sheet_key).sheet1

    column_values = sheet.col_values(2)[2 - 1:]
    filled_cells = sum(1 for value in column_values if value)

    row_number = filled_cells + 2

    for i, photo_link in enumerate(photo_links):
        sheet.update_cell(row_number, i + 2, photo_link)
