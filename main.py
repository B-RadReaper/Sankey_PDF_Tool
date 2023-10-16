###Starting Code###
# main.py - Entry point for the PDF app

import tkinter as tk
from pdf_viewer import PDFViewer
from menu_bar import MenuBar
from toolbars import Toolbars
from pdf_operations import PDFOperations
from search_functions import SearchFunctions

class PDFApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF App")
        
        # Initialize UI components
        self.pdf_viewer = PDFViewer(self.root)
        self.menu_bar = MenuBar(self.root)
        self.toolbars = Toolbars(self.root)
        
        # Initialize core functionality
        self.pdf_operations = PDFOperations()
        self.search_functions = SearchFunctions()
        
        # Connect UI components to core functionality
        self.menu_bar.set_pdf_operations(self.pdf_operations)
        self.toolbars.set_pdf_operations(self.pdf_operations)
        self.toolbars.set_search_functions(self.search_functions)
        self.pdf_viewer.set_pdf_operations(self.pdf_operations)
        
        # Pack UI components
        self.menu_bar.pack()
        self.toolbars.pack()
        self.pdf_viewer.pack(fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFApp(root)
    root.mainloop()
