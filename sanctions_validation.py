import requests 
import pandas
import tkinter as tk
import logging

from tkinter import filedialog, ttk
from lxml import etree
from constants import SANCTIONS_URLS

class XMLValidatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Sanctions Validator App')

        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s',
                            filename='sanctions.log',
                            filemode='w')
        
        self.logger = logging.getLogger()

        # Create a custom style for the widgets
        self.style = ttk.Style()
        self.style.configure('Custom.TButton', background='#4CAF50', foreground='white')
        self.style.configure('Custom.TEntry', background='#F1F1F0')

        self.create_widgets()
        self.resize_window()

        self.execute()

    def create_widgets(self):
        self.label = ttk.Label(self, text='Excel file path:')
        self.label.pack()

        self.entry = ttk.Entry(self, style='Custom.TEntry')
        self.entry.pack()

        self.browse_button = ttk.Button(self, text='Browse', style='Custom.TButton', command=self.browse_file)
        self.browse_button.pack()

        self.button = ttk.Button(self, text='Validate', style='Custom.TButton', command=self.execute)
        self.button.pack()

    def resize_window(self):
        window_width = 400
        window_height = 100
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))
        self.geometry(f'{window_width}x{window_height}+{x_cordinate}+{y_cordinate}')


    def fetch_sanctions(self):
        xml_data = []
        for url in SANCTIONS_URLS.values():
            response = requests.get(url)
            if response.status_code == 200:
                xml_data.append(response.content)
            else:
                error_msg = f'There was an error accessing: {url} - Status code: {response.status_code}'
                self.logger.error(error_msg)
                print(error_msg)
        return xml_data

    def read_excel(self):
        df = pandas.read_excel(self.entry.get())
        line_values = df.values.tolist()
        return line_values

    def browse_file(self):
        filetypes = (('Excel Files', '*.xlsx'), ('All Files', '*.*'))
        filename = filedialog.askopenfilename(filetypes=filetypes)
        self.entry.delete(0, tk.END)
        self.entry.insert(0, filename)

    def execute(self):
        excel_filepath = self.entry.get()
        if not excel_filepath:
            print("No Excel file selected.")
            return

        excel_data = self.read_excel()
        xml_data = self.fetch_sanctions()

        for line in excel_data:
            nome, emitente = line[0], line[1]
            if self.check_match(xml_data, nome, emitente):
                log_msg = f'Match found for Nome: {nome} or Emitente: {emitente}'
                self.logger.warning(log_msg)
                print(log_msg)
            else:
                log_msg = f'No match found for Nome: {nome} or Emitente: {emitente}'
                self.logger.info(log_msg)
                print(log_msg)

    def check_match(self, xml_data, nome, emitente):
        for xml_content in xml_data:
            root = etree.fromstring(xml_content)
            for element in root.iter():
                if element.text == nome or element.text == emitente:
                    return True
                else:
                    return False

if __name__ == '__main__':
    app = XMLValidatorApp()
    app.mainloop()
