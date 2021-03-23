import asyncio
from StatusCode import StatusCode


async def get_task_id_from_queue():
    print('Got taskID from queue')
    await write_status_to_dbs('taskId', StatusCode.Accepted)
    return 'taskID'


async def init_task(taskID):
    print('Init task taskID')
    result = await write_status_to_dbs('taskId', StatusCode.Running)
    if result:
        await write_status_to_dbs('taskId', StatusCode.Complete)
    else:
        await write_status_to_dbs('taskId', StatusCode.Error)
    return True


async def write_status_to_dbs(scanId, status):
    await print('Sent taskid: status to redis for 20 mins')
    await print('Sent taskid: status to DB')
    return True


async def main():
    while(True):
        taskId = await loop.create_task(get_task_id_from_queue())
        if not taskId:
            await write_status_to_dbs('taskId', StatusCode.NotFound)
        else:
            taskStatus = await loop.create_task(init_task(taskId))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
