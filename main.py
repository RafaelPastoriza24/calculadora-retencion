
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.clipboard import Clipboard

class RetencionCalculator(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=15, **kwargs)

        self.add_widget(Label(text='Calculadora de Retención (75% del IVA)', font_size=20))

        self.input_field = TextInput(hint_text='Monto total de la factura', multiline=False,
                                     input_filter='float', font_size=20, size_hint_y=None, height=50)
        self.add_widget(self.input_field)

        self.result_label = Label(text='', font_size=20)
        self.add_widget(self.result_label)

        button_layout = BoxLayout(size_hint_y=None, height=50, spacing=10)
        calc_button = Button(text='Calcular', on_press=self.calculate_retention)
        copy_button = Button(text='Copiar', on_press=self.copy_to_clipboard)
        button_layout.add_widget(calc_button)
        button_layout.add_widget(copy_button)
        self.add_widget(button_layout)

    def calculate_retention(self, instance):
        try:
            total = float(self.input_field.text)
            base_imponible = total / 1.16
            iva = base_imponible * 0.16
            retencion = iva * 0.75
            self.result_label.text = f'Monto a Retener: Bs. {retencion:.2f}'
        except ValueError:
            self.result_label.text = 'Ingrese un monto válido.'

    def copy_to_clipboard(self, instance):
        Clipboard.copy(self.result_label.text)

class FacturaRetencionApp(App):
    def build(self):
        return RetencionCalculator()

if __name__ == '__main__':
    FacturaRetencionApp().run()
