# main.py

import asyncio
from temporalio.client import Client
from temporalio.worker import Worker
from weather_workflow import WeatherWorkflow
from activities import fetch_weather_data_activity

async def main():
    client = await Client.connect("localhost:7233")
    worker = Worker(
        client,
        task_queue="weather-task-queue",
        workflows=[WeatherWorkflow],
        activities=[fetch_weather_data_activity],
    )
    await worker.run()

if __name__ == "__main__":
    asyncio.run(main())
