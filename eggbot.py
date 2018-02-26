from sanic import Sanic
from sanic import response
#from apscheduler.schedulers.asyncio import AsyncIOScheduler
import aiofiles as asio
from time import sleep
import uuid
import asyncio

async def async_task():
        while True:
            sleep(5)
            async with asio.open(str(uuid.uuid4()), 'w') as out:
                await out.write('sup')
                await out.flush()
                print('done writing file')

app = Sanic()
app.add_task(async_task)



@app.route('/')
async def home(request):
    return await response.file('index.html')


@app.route('/bundle.js')
async def static(request):
    return await response.file('bundle.js')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
