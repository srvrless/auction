from . import faust_app

topic = faust_app.topic("lots")


@faust_app.agent(topic)
async def agent_lots(stream):
    async for lot in stream:
        yield lot
