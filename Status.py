from StatusCode import StatusCode
from flask import Flask, request
import asyncio

app = Flask(__name__)


def get_status_from_redis(scanId):
    print('Got status from Redis')
    return True


def get_status_from_db(scanId):
    print('Got status from DB')
    return True


@app.route('/')
def handle_req():
    scanId = request.args['scanId']
    status = get_status_from_redis(scanId)
    if not status:
        return get_status_from_db(scanId)
    return scanId


if __name__ == '__main__':
    app.run()
