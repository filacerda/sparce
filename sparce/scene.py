from sparce.types import Config, Render


class Scene(object):
    def __init__(self, config: Config, render: Render) -> None:
        self._config: Config = config["scene"]

        self.render: Render = render
