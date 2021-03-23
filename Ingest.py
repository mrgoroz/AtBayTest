from flask import Flask
import uuid
import asyncio
from StatusCode import StatusCode

app = Flask(__name__)


def send_req_to_queue(scanId):
    print('Sent to MQ')
    return True


def write_status_to_dbs(scanId, status):
    print('scanId sent to dbs with status')
    return True


@app.route('/')
def handle_req():
    scanId = str(uuid.uuid4())
    return scanId
    res = send_req_to_queue(scanId)
    if res:
        write_status_to_dbs(scanId, StatusCode.Accepted)
        return scanId
    else:
        write_status_to_dbs(scanId, StatusCode.Error)
        return 'Problem with sending the request'


if __name__ == '__main__':
    app.run()
