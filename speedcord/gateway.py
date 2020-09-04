"""
Created by Epic at 9/2/20
"""
from logging import getLogger


class DefaultGatewayHandler:
    def __init__(self, client):
        self.client = client
        self.logger = getLogger("speedcord.gateway")

    async def on_receive(self, data: dict):
        self.logger.debug("Data received: " + str(data))
        self.client.opcode_dispatcher.dispatch(data["op"], data)
