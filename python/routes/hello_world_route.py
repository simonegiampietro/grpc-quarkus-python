import grpc._server

from grpc_resources.hello_world_pb2 import HelloWorldResponse
from grpc_resources.hello_world_pb2_grpc import HelloWorldServiceServicer, add_HelloWorldServiceServicer_to_server
from routes.abstract_route import AbstractRoute


class HelloWorldRoute(HelloWorldServiceServicer, AbstractRoute):
    def add_to_server(self, server: grpc._server._Server):
        add_HelloWorldServiceServicer_to_server(self, server)

    def Hello(self, request, context):
        print(f'values = {request.values}')
        return HelloWorldResponse(returnedValue="Hello Guys")