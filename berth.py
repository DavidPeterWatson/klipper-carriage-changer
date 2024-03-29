class Berth:
    def __init__(self, config):
        self.printer = config.get_printer()
        self.name = config.get_name().split(' ')[-1]
        self.dock_name = config.get('dock')
        self.dock_x = config.get('dock_x')
        self.printer.add_object(self.name, self)


def load_config_prefix(config):
    return Berth(config)
