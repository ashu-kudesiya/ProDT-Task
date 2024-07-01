# weather_workflow.py

from temporalio import workflow

@workflow.defn
class WeatherWorkflow:
    @workflow.run
    async def run(self, api_key: str, location: str):
        result = await workflow.execute_activity(
            "fetch_weather_data",
            api_key,
            location,
            start_to_close_timeout=300
        )
        return result
