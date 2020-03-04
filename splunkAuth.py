import splunklib.client as client
import sys
from os import path


HOST = 'localhost'
PORT = '8089'
USERNAME = 'digarci13'
PASSWORD = 'blackvenom13'
def splunk_connect():
    service = client.connect(host=HOST, port=PORT, username=USERNAME, password=PASSWORD)
    print(service)

    try:
        i = service.indexes.get('main')
        
    except Exception as e:
        print(str(e))




if __name__ == '__main__':
    splunk_connect()