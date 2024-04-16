import os

class CarraigeChanger:
    def __init__(self, config):
        self.printer = config.get_printer()

        # Load carriage movement
        pconfig = self.printer.lookup_object('configfile')
        dirname = os.path.dirname(os.path.realpath(__file__))
        filename = os.path.join(dirname, 'carriage_movement.cfg')
        try:
            cariage_movement = pconfig.read_config(filename)
        except Exception:
            raise config.error("Cannot load config '%s'" % (filename,))
        for section in cariage_movement.get_prefix_sections(''):
            self.printer.load_object(cariage_movement, section.get_name())

def load_config_prefix(config):
    return CarraigeChanger(config)