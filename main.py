import json

from sparce.types import Config

from sparce.simulator import Simulator


def main(config_path: str) -> None:
    with open(config_path, "r") as file:
        config: Config = json.load(file)

    simulator: Simulator = Simulator(config)
    simulator.run()


if __name__ == "__main__":
    main("config/config.json")
