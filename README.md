# oh-sheets
A python wrapper for the google sheets api.


## Setup

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
