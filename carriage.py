class Carriage:
    def __init__(self, config):
        self.printer = config.get_printer()
        self.name = config.get_name().split(' ')[-1]
        Carriage.validate_name(self.name)
        self.berth = config.get('berth')
        self.offset_x = float(config.get('offset_x') or 0)
        self.offset_y = float(config.get('offset_y') or 0)
        self.offset_z = float(config.get('offset_z') or 0)
        self.printer.add_object('carriage ' + self.name, self)
        gcode_macro = self.printer.load_object(config, 'gcode_macro') 
        self.after_load_template = gcode_macro.load_template(config, 'after_load_gcode', '') 
        self.after_unload_template = gcode_macro.load_template(config, 'after_unload_gcode', '')

    def validate_name(name):
        if name == 'none':
            raise Exception("Carriage name cannot be 'none'")
        if name == '':
            raise Exception("Carriage name cannot be ''")
        if not name:
            raise Exception("Carriage name cannot be '{name}'")

    # def cmd_QUERY_BUTTON(self, gcmd):
    #     gcmd.respond_info(self.name + ": " + self.get_status()['state'])

    # def button_callback(self, eventtime, state):
    #     self.last_state = state
    #     template = self.press_template
    #     if not state:
    #         template = self.release_template
    #     try:
    #         self.gcode.run_script(template.render())
    #     except:
    #         logging.exception("Script running error")

    # def get_status(self, eventtime=None):
    #     if self.last_state:
    #         return {'state': "PRESSED"}
    #     return {'state': "RELEASED"}

def load_config_prefix(config):
    return Carriage(config)
