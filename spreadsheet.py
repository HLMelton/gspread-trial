import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
# Json file can be renamed, though it needs to be edited here as well.
# The current name is the dafault given to it by GoogleAPIs


client = gspread.authorize(creds)

sheet = client.open('Legislators 2017').sheet1

legislators = sheet.get_all_records()
print(legislators)