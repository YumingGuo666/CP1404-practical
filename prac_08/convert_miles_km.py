from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    """MilesConverterApp is a Kivy App for converting miles to kilometres."""

    output_text = StringProperty("0.0")

    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):
        """Convert miles to kilometres and update the label text."""
        miles = self.get_validated_miles()
        km = miles * MILES_TO_KM
        self.output_text = f"{km:.2f}"

    def handle_increment(self, change):
        """Increase or decrease the miles input by 1, then update the output."""
        miles = self.get_validated_miles()
        miles += change
        self.root.ids.input_miles.text = str(miles)
        self.handle_calculate()

    def get_validated_miles(self):
        """Get and validate the input from TextInput. Return 0 if invalid."""
        try:
            return float(self.root.ids.input_miles.text)
        except ValueError:
            return 0.0


MilesConverterApp().run()

