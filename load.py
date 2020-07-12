"""
Experimental example plugin that updates the main UI every time we get a journal event
"""
import tkinter
import plug
from EDMCPlugin.ui import EDMCUIPluginBase, EDMCUIDisplayTable


class ExampleDashboardPlugin(EDMCUIPluginBase, EDMCUIDisplayTable):
    """
    A plugin that displays some dasboard status values
    """

    lights = None
    scoop = None
    gear = None

    def plugin_name(self):
        return "Example Dash Plugin"

    def plugin_version(self):
        return "0.0.1"

    def create_rows(self, parent):
        rows = []
        self.scoop = tkinter.Label(parent, text="", justify=tkinter.CENTER)
        rows.append([tkinter.Label(parent, text="Cargo Scoop:", justify=tkinter.LEFT), self.scoop])

        self.lights = tkinter.Label(parent, text="", justify=tkinter.CENTER)
        rows.append([tkinter.Label(parent, text="Lights:", justify=tkinter.LEFT), self.lights])

        self.gear = tkinter.Label(parent, text="", justify=tkinter.CENTER)
        rows.append([tkinter.Label(parent, text="Gear:", justify=tkinter.LEFT), self.gear])

        return rows

    def plugin_start(self):
        print("started {}".format(self.plugin_name()))

    def dashboard_event(self, cmdr, entry):
        flags = entry["entry"]["Flags"]
        if plug.FlagsLandingGearDown & flags:
            self.gear.after(1, self.gear.config, {"text": "down"})
        else:
            self.gear.after(1, self.gear.config, {"text": ""})

        if plug.FlagsCargoScoopDeployed & flags:
            self.scoop.after(1, self.scoop.config, {"text": "open"})
        else:
            self.scoop.after(1, self.scoop.config, {"text": ""})

        if plug.FlagsLightsOn & flags:
            self.lights.after(1, self.lights.config, {"text": "on"})
        else:
            self.lights.after(1, self.lights.config, {"text": ""})


__plugin__ = ExampleDashboardPlugin()
