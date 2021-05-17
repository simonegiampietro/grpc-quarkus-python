from typing import List

from routes.abstract_route import AbstractRoute
from routes.another_hello_world_route import AnotherRoute
from routes.hello_world_route import HelloWorldRoute
from server import Server

ROUTES: List[AbstractRoute] = [
    AnotherRoute(),
    HelloWorldRoute()
]


def launch():
    Server(ROUTES).serve()


if __name__ == '__main__':
    launch()
