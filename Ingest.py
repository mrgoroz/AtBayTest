from flask import Flask
import uuid
import asyncio

app = Flask(__name__)


def send_req_to_queue(scanId):
    print('Sent to MQ')
    return True


@app.route('/')
def handle_req():
    scanId = str(uuid.uuid4())
    return scanId
    res = send_req_to_queue(scanId)
    if res:
        return scanId
    else:
        return 'Problem with sending the request'


if __name__ == '__main__':
    app.run()
