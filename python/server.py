from concurrent import futures

import grpc

from grpc_resources.another_hello_world_pb2 import AnotherResponse
from grpc_resources.another_hello_world_pb2_grpc import AnotherHelloWorldService, \
    add_AnotherHelloWorldServiceServicer_to_server, AnotherHelloWorldServiceServicer
from grpc_resources.hello_world_pb2 import HelloWorldResponse
from grpc_resources.hello_world_pb2_grpc import HelloWorldServiceServicer, add_HelloWorldServiceServicer_to_server


class HelloWorldRoute(HelloWorldServiceServicer):
    def Hello(self, request, context):
        print(f'values = {request.values}')
        return HelloWorldResponse(returnedValue="Hello Guys")


class AnotherRoute(AnotherHelloWorldServiceServicer):
    def AnotherMessage(self, request, context):
        context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
        context.set_details('Passed invalid argument')
        return AnotherResponse()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_AnotherHelloWorldServiceServicer_to_server(AnotherRoute(), server)
    add_HelloWorldServiceServicer_to_server(HelloWorldRoute(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print('service started')
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
