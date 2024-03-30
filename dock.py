class Dock:
    def __init__(self, config):
        self.printer = config.get_printer()
        self.name = config.get_name().split(' ')[-1]
        self.location = config.get('location')
        self.safe_y = float(config.get('safe_y'))
        self.safe_zd = float(config.get('safe_zd'))
        self.load_yd = float(config.get('load_yd'))
        self.load_xd = float(config.get('load_xd'))
        self.loading_speed = float(config.get('loading_speed')) * 60
        self.loading_pause = config.get('loading_pause')
        self.printer.add_object('dock ' + self.name, self)


def load_config_prefix(config):
    return Dock(config)
