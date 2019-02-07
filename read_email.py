from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import base64
import email

SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'

class ReadEmail:
    def setting_credential(self):
        print('Trying to retrieve list of e-mails....')
        store = file.Storage('token.json')
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
            creds = tools.run_flow(flow, store)
        service = build('gmail', 'v1', http=creds.authorize(Http()))
        return service

    def read_email(self): 
        service = self.setting_credential()   
        # Call the Gmail API to fetch INBOX
        results = service.users().messages().list(userId='me',labelIds = ['INBOX']).execute()
        messages = results.get('messages', [])
        

        if not messages:
            print ("No messages found.")
        else:
            # print ("Message snippets:")
            msg_temps = []
            for message in messages:
                msg = service.users().messages().get(userId='me', id=message['id'], format='raw').execute()
                msg_str = base64.urlsafe_b64decode(msg['raw'].encode('ASCII'))
                mime_msg = email.message_from_bytes(msg_str)
                
                
                msg_temps.append(str(mime_msg))
            
            msg_contents = []
            date = []
            sent_from = []
            subjects = []

            values = []
            
            for i in range(len(msg_temps)):
                msgs_test = msg_temps[i].split('Content-Type: text/plain; charset="UTF-8"')
                msgs_test = msgs_test[1].split('--')
                msgs_test = msgs_test[0]
                msg_contents = msgs_test[1:-2]

                sent_test = msg_temps[i].split('From: ')
                sent_test = sent_test[1].split('Date: ')
                sent_from = sent_test[0][:-1]

                date_test = msg_temps[i].split('Date:')
                date_test = date_test[1].split('Message-ID:')
                date_test = date_test[0].replace('+0800','').splitlines()
                date = date_test[0][:-1].lstrip()

                subj_test = msg_temps[i].split('Message-ID:')
                subj_test = subj_test[1].split('To:')
                subj_test = subj_test[0].split('Subject: ')
                subjects = subj_test[1][:-1]
                
                val = [date, sent_from, subjects, msg_contents]
                # print(val)
                values.append(val)
            print('SUCCESS')
            
            return values

# if __name__ == '__main__':
#     read()