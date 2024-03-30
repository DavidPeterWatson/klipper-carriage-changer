class Carriage:
    def __init__(self, config):
        self.printer = config.get_printer()
        self.name = config.get_name().split(' ')[-1]
        self.dock = config.get('dock')
        self.docking_bay_x = config.get('docking_bay_x')
        self.offset_x = config.get('offset_x')
        self.offset_y = config.get('offset_y')
        self.offset_z = config.get('offset_z')
        self.printer.add_object('carriage-' + self.name, self)
        # gcode_macro = self.printer.load_object(config, 'gcode_macro')
        # self.after_load_template = gcode_macro.load_template(config, 'after_load_gcode')
        # self.after_unload_template = gcode_macro.load_template(config, 'after_unload_gcode', '')


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
