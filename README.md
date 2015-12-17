# oh-sheets
A python wrapper for the google sheets api.


## Setup Google API
1. Go here:  https://console.developers.google.com/home/
2. In the mid-top-right of the header, find the down arrow, click it, then create a project.
3. Fill out project details.
4. Go back to the dashboard and click `Enable and Manage APIs`, or something similar
5. Find the google drive API in the listing, and click it
6. Click 'Enable API'
7. Click 'Go To Credentials'
8. Create new credentials with Oauth2, download the .json file
9. Copy the Client ID and the Client Secret, and use them to setup your environment, as below:


## Setup Local Environment

You'll need two environment variables setup:
- GD_CLIENTID : your GoogleData client ID
- GD_CLIENTSECRET : your GoogleData client secret.

I put these in my own .env file in the folder this repository is in:

[this_repo]/.env
```
export GD_CLIENTID=[redacted]
export GD_CLIENTSECRET=[redacted]
```

## Usage

```
USAGE: python google_spreadsheet_test.py [sheet_id]
```
where "sheet_id" is the long random string you get in the url when you visit your google sheet in the web.
