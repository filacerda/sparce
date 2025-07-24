from panda3d.core import loadPrcFile, AntialiasAttrib

from direct.showbase.ShowBase import ShowBase

from sparce.types import Config

from sparce.scene import Scene
from sparce.vehicle import Vehicle


class Simulator(ShowBase):
    def __init__(self, config: Config) -> None:
        # Load Panda3D config file
        loadPrcFile("config/Config.prc")

        super().__init__()

        self.render.setAntialias(AntialiasAttrib.MAuto)

        self._config: Config = config

        self.scene: Scene = Scene(self._config, self.render)
        self.vehicle: Vehicle = Vehicle(self._config, self.render)
