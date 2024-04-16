import os

class CarriageChanger:
    def __init__(self, config):
        self.printer = config.get_printer()

        # # Load carriage movement
        # pconfig = self.printer.lookup_object('configfile')
        # dirname = os.path.dirname(os.path.realpath(__file__))
        # filename = os.path.join(dirname, 'carriage_movement.cfg')
        # try:
        #     carriage_movement = pconfig.read_config(filename)
        # except Exception:
        #     raise config.error("Cannot load config '%s'" % (filename,))
        # for section in carriage_movement.get_prefix_sections(''):
        #     self.printer.load_object(carriage_movement, section.get_name())

def load_config_prefix(config):
    return CarriageChanger(config)
