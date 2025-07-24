from sparce.types import Config, Render


class Vehicle(object):
    def __init__(self, config: Config, render: Render) -> None:
        self._config: Config = config["vehicle"]

        self.render: Render = render
