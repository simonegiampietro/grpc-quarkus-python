import grpc
import grpc._server

from grpc_resources.another_hello_world_pb2 import AnotherResponse
from grpc_resources.another_hello_world_pb2_grpc import AnotherHelloWorldServiceServicer, \
    add_AnotherHelloWorldServiceServicer_to_server
from routes.abstract_route import AbstractRoute


class AnotherRoute(AnotherHelloWorldServiceServicer, AbstractRoute):
    def add_to_server(self, server: grpc._server._Server):
        add_AnotherHelloWorldServiceServicer_to_server(self, server)

    def AnotherMessage(self, request, context):
        context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
        context.set_details('Passed invalid argument')
        return AnotherResponse()