import requests 
import pandas
import tkinter as tk
import logging
import json

from tkinter import filedialog, ttk
from lxml import etree

class XMLValidatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Sanctions Validator App')

        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s',
                            filename='sanctions.log',
                            filemode='w')
        
        self.logger = logging.getLogger()

        self.style = ttk.Style()
        self.style.configure('Custom.TButton', background='black', foreground='black')
        self.style.configure('Custom.TEntry', background='green')

        self.create_widgets()
        self.resize_window()

    def create_widgets(self):
        self.label = ttk.Label(self, text='Excel file path:')
        self.label.pack()

        self.entry = ttk.Entry(self, style='Custom.TEntry')
        self.entry.pack()

        self.browse_button = ttk.Button(self, text='Browse', style='Custom.TButton', command=self.browse_file)
        self.browse_button.pack()

        self.button = ttk.Button(self, text='Validate', style='Custom.TButton', width=20, command=self.execute)
        self.button.pack()

        self.log_text = tk.Text(self, height=20, width=80)
        self.log_text.pack()

    def resize_window(self):
        window_width = 500
        window_height = 200
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))
        self.geometry(f'{window_width}x{window_height}+{x_cordinate}+{y_cordinate}')


    def fetch_sanctions(self):
        xml_data = {}

        info_msg = "Starting Sanction lists reading..."
        self.logger.error(info_msg)
        self.log_text.insert(tk.END, info_msg + '\n')

        with open('config.json') as config_file:
            xml_data = json.load(config_file)

        fetched_data = {}

        for source, url in xml_data.items():
            response = requests.get(url)
            if response.status_code == 200:
                xml_content = response.content.decode('utf-8')
                fetched_data[xml_content] = source

                # Extract the name of the XML file from the URL
                xml_filename = url.split('/')[-1]
                log_msg = f'Fetched XML: {source} - {xml_filename}'
                self.logger.info(log_msg)
                self.log_text.insert(tk.END, log_msg + '\n')
                print(log_msg)
            else:
                error_msg = f'There was an error accessing: {url} - Status code: {response.status_code}'
                self.logger.error(error_msg)
                self.log_text.insert(tk.END, error_msg + '\n')
                print(error_msg)
        return fetched_data

    def read_excel(self):
        info_msg = "Starting Excel reading..."
        self.logger.error(info_msg)
        self.log_text.insert(tk.END, info_msg + '\n')

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
            error_msg = "No Excel file selected!"
            self.logger.error(error_msg)
            self.log_text.insert(tk.END, error_msg + '\n')
            return

        excel_data = self.read_excel()
        xml_data = self.fetch_sanctions()


        info_msg = "Validating matches entries..."
        self.logger.error(info_msg)
        self.log_text.insert(tk.END, info_msg + '\n')

        for line in excel_data:
            nome, emitente = line[0], line[1]
            matched, source = self.check_match(xml_data, nome, emitente)
            if matched:
                log_msg = f'Match found for Nome: {nome} or Emitente: {emitente} in {source} XML'
                self.logger.warning(log_msg)
                self.log_text.insert(tk.END, log_msg + '\n')
                print(log_msg)
            else:
                log_msg = f'No match found for Nome: {nome} or Emitente: {emitente}'
                self.logger.info(log_msg)
                print(log_msg)

    def check_match(self, xml_data, nome, emitente):
    
        for xml_content, source in xml_data.items():
            root = etree.fromstring(xml_content)
            for element in root.iter():
             if element.text:
                element_text = str(element.text)
                if element_text.lower() == nome.lower() or element_text.lower() == emitente.lower():
                    return True, source
        return False, None

if __name__ == '__main__':
    app = XMLValidatorApp()
    app.mainloop()
