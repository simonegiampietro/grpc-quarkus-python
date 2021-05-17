from abc import abstractmethod

import grpc._server


class AbstractRoute:
    @abstractmethod
    def add_to_server(self, server: grpc._server._Server):
        pass
