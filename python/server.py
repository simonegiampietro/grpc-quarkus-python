from concurrent import futures
from typing import List

import grpc

from routes.abstract_route import AbstractRoute


class Server:
    def __init__(self, routes: List[AbstractRoute]):
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        self.server.add_insecure_port('[::]:50051')
        for route in routes:
            route.add_to_server(self.server)

    def serve(self):
        self.before_serve()
        self.server.start()
        print('service started')
        self.server.wait_for_termination()

    def before_serve(self):
        pass
