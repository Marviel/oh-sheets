#!/usr/bin/python
#Title: gdata_spreadsheet_test.py
#Author:               Luke Bechtel
#Description: 
#     Outputs a value from a given google sheets Worksheet via OAuth2 and the Google Sheets API.
#     
 
from oauth2client.client import OOB_CALLBACK_URN        #'urn:ietf:wg:oauth:2.0:oob'
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import OAuth2WebServerFlow
from subprocess import Popen
import gdata.spreadsheets.client
import os
import xml.dom.minidom
import xml.etree.ElementTree as ET
import re
import sys


USAGESTR = "USAGE: python google_spreadsheet_test.py [sheet_id]"

#Get sheet arg.
if len(sys.argv) != 2:
  print USAGESTR
  exit(0)

SHEET_ID = sys.argv[1]


def get_cell_obj(client,sheet,page,r, c):
  return client.get_cell(spreadsheet_key,1,1,1)

def get_cell_content(client,sheet,page,r,c):
  cell_obj = get_cell_obj(client,sheet,page,r,c)
  root = ET.fromstring(str(cell_obj))

  for child in root:
    mtch = str(child.tag).split('}') #This splits the tag from the prefix.
    actual_tag = mtch[1] if len(mtch) > 1 else mtch[0] #This gives us the actual tag despite prefixes

    #We want content
    if actual_tag == "content":
      full_match_tag = child.tag
      break

    # print str(child.tag) + " ----> " + str(child.attrib)
    # print "tag found: " + actual_tag

  cell = root.find(full_match_tag)
  return cell.text

client_id=os.environ['GD_CLIENTID']
client_secret=os.environ['GD_CLIENTSECRET']
scope="https://spreadsheets.google.com/feeds https://docs.google.com/feeds";
redirect_uri=OOB_CALLBACK_URN

if client_id is None or client_secret is None:
  print 'missing client_id or client secret!'
  exit(1)

flow = OAuth2WebServerFlow(client_id, client_secret, scope, redirect_uri)

#Do the flow step 1
auth_uri = flow.step1_get_authorize_url()

Popen(['open', auth_uri])

# # XXX parse url and retrieve from header
code = raw_input('copy code from browser and enter: ')

#Do the flow step 2
cred = flow.step2_exchange(code)

print 'we have creds'
print 'access token: %s'  % cred.access_token
print 'refresh token: %s' % cred.refresh_token

gd_client = gdata.spreadsheets.client.SpreadsheetsClient()
#gd_client = gdata.docs.service.DocsService()
auth2token = gdata.gauth.OAuth2TokenFromCredentials(cred)
gd_client = auth2token.authorize(gd_client)


#Printing bare xml content in cell object
spreadsheet_key=SHEET_ID
cell = gd_client.get_cell(spreadsheet_key, 1, 1, 1) 
print cell

#Pretty printing xml content in cell object
xml = xml.dom.minidom.parseString(str(cell)) # or xml.dom.minidom.parseString(xml_string)
pretty_xml_as_string = xml.toprettyxml()
print pretty_xml_as_string

cell_content = get_cell_content(gd_client,spreadsheet_key,1,1,1)
print "got content: " + cell_content

exit(0)