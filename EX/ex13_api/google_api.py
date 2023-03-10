"""Ok."""
from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1WrCzu4p5lFwPljqZ6tMQEJb2vSJQSGjyMsqcYt-yS4M'
SAMPLE_RANGE_NAME = 'A2:E'


def get_links_from_spreadsheet(id: str, token_file_name: str) -> list:
    """
    Show basic usage of the Sheets API.

    Print values from a sample spreadsheet.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(token_file_name):
        creds = Credentials.from_authorized_user_file(token_file_name, SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(token_file_name, 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=id,
                                    range="A1:E4").execute()
        values = result.get('values')

        if not values:
            print('No data found.')
        rows = []
        for row in values:
            rows.append(row)
        flat_list = [item for sublist in rows for item in sublist]
        return flat_list

    except HttpError as err:
        print(err)


if __name__ == '__main__':
    print(get_links_from_spreadsheet("1WrCzu4p5lFwPljqZ6tMQEJb2vSJQSGjyMsqcYt-yS4M", "A2:E"))
