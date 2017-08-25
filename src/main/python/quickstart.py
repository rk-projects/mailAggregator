from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/gmail-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Gmail API Python Quickstart'


def get_credentials( credentailFile ):
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   credentailFile)

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def headers(service):
    """
    Fetch "from" and "subject"
    """
    print ("Calling Headers")

def bodySnippet(service):
    "fetch body snippet"
    print ( "calling body snippet")
    results = service.users().messages().list(userId='me').execute()

    # labels = service.users().messages().get(userId="me", id="15e19a83eaed02de").execute()

    # print('Message snippet: %s' % message['snippet'])


    # for label in results:
    #     print(results[label])
    # for arrayVal in results
    # message []

    # Get functions for
    #       From, Subject, Body

    # Modify credential path to be able to take multiple credentials.
    i = 0

    for dictValues in results.get('messages'):
        i += 1
        messageText = service.users().messages().get(userId="me", id=dictValues.get('id')).execute()
        # print(messageText['snippet'])
        print(messageText['payload']['headers'])
        print("---------------------------------------")
        if i > 5:
            break


def main():
    """Shows basic usage of the Gmail API.

    Creates a Gmail API service object and outputs a list of label names
    of the user's Gmail account.
    """

    """ Create a credential file which will have username binded to it dynamically 
    """
    mainCredentialFile =  "gmail-python-quickstart-vineet.json"
    credentials = get_credentials( mainCredentialFile )
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('gmail', 'v1', http=http)

    # Fetch "From" and "Subject"
    headers(service)
    # Fetch Body Snippet
    bodySnippet(service)


if __name__ == '__main__':
    main()
