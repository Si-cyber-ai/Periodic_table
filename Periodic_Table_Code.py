from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter.font as tkfont

class Element:
    def __init__(self, full_name, symbol, atomic_number, atomic_weight):
        self.FullName = full_name
        self.Symbol = symbol
        self.AtomicNumb = atomic_number
        self.AtomicW = atomic_weight

# Periodic Table Data
ELEMENTS = [
    Element("Hydrogen", "H", 1, 1.008),
    Element("Helium", "He", 2, 4.0026),
    Element("Lithium", "Li", 3, 6.94),
    Element("Beryllium", "Be", 4, 9.0122),
    Element("Boron", "B", 5, 10.81),
    Element("Carbon", "C", 6, 12.011),
    Element("Nitrogen", "N", 7, 14.007),
    Element("Oxygen", "O", 8, 15.999),
    Element("Fluorine", "F", 9, 18.998),
    Element("Neon", "Ne", 10, 20.180),
    Element("Sodium", "Na", 11, 22.990),
    Element("Magnesium", "Mg", 12, 24.305),
    Element("Aluminum", "Al", 13, 26.982),
    Element("Silicon", "Si", 14, 28.085),
    Element("Phosphorus", "P", 15, 30.974),
    Element("Sulfur", "S", 16, 32.06),
    Element("Chlorine", "Cl", 17, 35.45),
    Element("Argon", "Ar", 18, 39.948),
    Element("Potassium", "K", 19, 39.098),
    Element("Calcium", "Ca", 20, 40.078),
    Element("Scandium", "Sc", 21, 44.956),
    Element("Titanium", "Ti", 22, 47.867),
    Element("Vanadium", "V", 23, 50.942),
    Element("Chromium", "Cr", 24, 51.996),
    Element("Manganese", "Mn", 25, 54.938),
    Element("Iron", "Fe", 26, 55.845),
    Element("Cobalt", "Co", 27, 58.933),
    Element("Nickel", "Ni", 28, 58.693),
    Element("Copper", "Cu", 29, 63.546),
    Element("Zinc", "Zn", 30, 65.38),
    Element("Gallium", "Ga", 31, 69.723),
    Element("Germanium", "Ge", 32, 72.63),
    Element("Arsenic", "As", 33, 74.922),
    Element("Selenium", "Se", 34, 78.971),
    Element("Bromine", "Br", 35, 79.904),
    Element("Krypton", "Kr", 36, 83.798),
    Element("Rubidium", "Rb", 37, 85.468),
    Element("Strontium", "Sr", 38, 87.62),
    Element("Yttrium", "Y", 39, 88.906),
    Element("Zirconium", "Zr", 40, 91.224),
    Element("Niobium", "Nb", 41, 92.906),
    Element("Molybdenum", "Mo", 42, 95.95),
    Element("Technetium", "Tc", 43, 98),
    Element("Ruthenium", "Ru", 44, 101.07),
    Element("Rhodium", "Rh", 45, 102.91),
    Element("Palladium", "Pd", 46, 106.42),
    Element("Silver", "Ag", 47, 107.87),
    Element("Cadmium", "Cd", 48, 112.41),
    Element("Indium", "In", 49, 114.82),
    Element("Tin", "Sn", 50, 118.71),
    Element("Antimony", "Sb", 51, 121.76),
    Element("Tellurium", "Te", 52, 127.60),
    Element("Iodine", "I", 53, 126.90),
    Element("Xenon", "Xe", 54, 131.29),
    Element("Cesium", "Cs", 55, 132.91),
    Element("Barium", "Ba", 56, 137.33),
    Element("Lanthanum", "La", 57, 138.91),
    Element("Cerium", "Ce", 58, 140.12),
    Element("Praseodymium", "Pr", 59, 140.91),
    Element("Neodymium", "Nd", 60, 144.24),
    Element("Promethium", "Pm", 61, 145),
    Element("Samarium", "Sm", 62, 150.36),
    Element("Europium", "Eu", 63, 151.96),
    Element("Gadolinium", "Gd", 64, 157.25),
    Element("Terbium", "Tb", 65, 158.93),
    Element("Dysprosium", "Dy", 66, 162.50),
    Element("Holmium", "Ho", 67, 164.93),
    Element("Erbium", "Er", 68, 167.26),
    Element("Thulium", "Tm", 69, 168.93),
    Element("Ytterbium", "Yb", 70, 173.05),
    Element("Lutetium", "Lu", 71, 174.97),
    Element("Hafnium", "Hf", 72, 178.49),
    Element("Tantalum", "Ta", 73, 180.95),
    Element("Tungsten", "W", 74, 183.84),
    Element("Rhenium", "Re", 75, 186.21),
    Element("Osmium", "Os", 76, 190.23),
    Element("Iridium", "Ir", 77, 192.22),
    Element("Platinum", "Pt", 78, 195.08),
    Element("Gold", "Au", 79, 196.97),
    Element("Mercury", "Hg", 80, 200.59),
    Element("Thallium", "Tl", 81, 204.38),
    Element("Lead", "Pb", 82, 207.2),
    Element("Bismuth", "Bi", 83, 208.98),
    Element("Polonium", "Po", 84, 209),
    Element("Astatine", "At", 85, 210),
        Element("Radon", "Rn", 86, 222),
    Element("Francium", "Fr", 87, 223),
    Element("Radium", "Ra", 88, 226),
    Element("Actinium", "Ac", 89, 227),
    Element("Thorium", "Th", 90, 232.04),
    Element("Protactinium", "Pa", 91, 231.04),
    Element("Uranium", "U", 92, 238.03),
    Element("Neptunium", "Np", 93, 237),
    Element("Plutonium", "Pu", 94, 244),
    Element("Americium", "Am", 95, 243),
    Element("Curium", "Cm", 96, 247),
    Element("Berkelium", "Bk", 97, 247),
    Element("Californium", "Cf", 98, 251),
    Element("Einsteinium", "Es", 99, 252),
    Element("Fermium", "Fm", 100, 257),
    Element("Mendelevium", "Md", 101, 258),
    Element("Nobelium", "No", 102, 259),
    Element("Lawrencium", "Lr", 103, 266),
    Element("Rutherfordium", "Rf", 104, 267),
    Element("Dubnium", "Db", 105, 270),
    Element("Seaborgium", "Sg", 106, 271),
    Element("Bohrium", "Bh", 107, 270),
    Element("Hassium", "Hs", 108, 277),
    Element("Meitnerium", "Mt", 109, 278),
    Element("Darmstadtium", "Ds", 110, 281),
    Element("Roentgenium", "Rg", 111, 282),
    Element("Copernicium", "Cn", 112, 285),
    Element("Nihonium", "Nh", 113, 286),
    Element("Flerovium", "Fl", 114, 289),
    Element("Moscovium", "Mc", 115, 290),
    Element("Livermorium", "Lv", 116, 293),
    Element("Tennessine", "Ts", 117, 294),
    Element("Oganesson", "Og", 118, 294)
]


def SearchTable(name=None, symbol=None, atomic_number=None, atomic_weight=None):
    results = []
    
    for element in ELEMENTS:
        if name and name.lower() in element.FullName.lower():
            results.append(element)
        elif symbol and symbol.lower() == element.Symbol.lower():
            results.append(element)
        elif atomic_number and str(element.AtomicNumb) == atomic_number:
            results.append(element)
        elif atomic_weight:
            # Allow for some margin of error in atomic weight (±0.1)
            if abs(element.AtomicW - atomic_weight) <= 0.1:
                results.append(element)
    
    return results

# Modern Color Scheme
COLORS = {
    'primary': "#1E88E5",       # Main blue
    'primary_dark': "#1565C0",  # Darker blue for hover
    'secondary': "#FFC107",     # Accent color (amber)
    'background': "#F5F5F5",    # Light gray background
    'surface': "#FFFFFF",       # White surface
    'text_primary': "#212121",  # Dark text
    'text_secondary': "#757575", # Secondary text
    'error': "#F44336",         # Error red
    'success': "#4CAF50"        # Success green
}

# Modern Font Configuration
FONTS = {
    'title': ("Segoe UI", 32, "bold"),
    'heading': ("Segoe UI", 24, "bold"),
    'subheading': ("Segoe UI", 18),
    'body': ("Segoe UI", 12),
    'button': ("Segoe UI", 12, "bold"),
    'caption': ("Segoe UI", 10)
}

# Custom Styles
def setup_styles():
    style = ttk.Style()
    style.theme_use('clam')  # Use 'clam' theme as base
    
    # Configure main window
    style.configure('Main.TFrame', background=COLORS['background'])
    
    # Configure modern buttons
    style.configure('Modern.TButton',
        font=FONTS['button'],
        padding=10,
        background=COLORS['primary'],
        foreground=COLORS['surface']
    )
    
    # Configure search entry
    style.configure('Search.TEntry',
        font=FONTS['body'],
        padding=10,
        fieldbackground=COLORS['surface']
    )
    
    # Configure result cards
    style.configure('Card.TFrame',
        background=COLORS['surface'],
        relief='raised',
        borderwidth=1
    )

    return style

class ModernWindow(Tk):
    def __init__(self):
        super().__init__()
        
        # Window setup
        self.title('Periodic Table Explorer Pro')
        self.geometry('1024x768')
        self.configure(bg=COLORS['background'])
        
        # Center window
        self.center_window(1024, 768)
        
        # Setup styles
        self.style = setup_styles()
        
        # Create main container
        self.container = ttk.Frame(self, style='Main.TFrame')
        self.container.pack(side="top", fill="both", expand=True, padx=20, pady=20)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        
        # Initialize frames
        self.frames = {}
        for F in (ModernStartPage, SearchByNumber, SearchByWeight, SearchByName, SearchBySymbol):
            frame = F(self.container, self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame("ModernStartPage")
    
    def center_window(self, width, height):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.geometry(f'{width}x{height}+{x}+{y}')
    
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
        frame.event_generate("<<PageShown>>")

class ModernStartPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        # Main container with padding
        main_container = ttk.Frame(self, style='Main.TFrame')
        main_container.pack(fill="both", expand=True, padx=40, pady=40)
        
        # Header
        header_frame = ttk.Frame(main_container, style='Main.TFrame')
        header_frame.pack(fill="x", pady=(0, 40))
        
        title = ttk.Label(header_frame,
            text="Periodic Table Explorer",
            font=FONTS['title'],
            foreground=COLORS['primary']
        )
        title.pack()
        
        subtitle = ttk.Label(header_frame,
            text="Your Professional Element Search Tool",
            font=FONTS['subheading'],
            foreground=COLORS['text_secondary']
        )
        subtitle.pack(pady=(10, 0))
        
        # Search options container
        options_frame = ttk.Frame(main_container, style='Main.TFrame')
        options_frame.pack(fill="both", expand=True)
        
        # Grid layout for search options
        options = [
            ("Search by Atomic Number", "SearchByNumber", "⚛"),
            ("Search by Atomic Weight", "SearchByWeight", "⚖"),
            ("Search by Element Name", "SearchByName", "📝"),
            ("Search by Element Symbol", "SearchBySymbol", "🔍")
        ]
        
        for idx, (text, page, icon) in enumerate(options):
            option_frame = self.create_option_card(options_frame, text, icon, lambda p=page: controller.show_frame(p))
            row, col = divmod(idx, 2)
            option_frame.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
        
        options_frame.grid_columnconfigure(0, weight=1)
        options_frame.grid_columnconfigure(1, weight=1)
    
    def create_option_card(self, parent, text, icon, command):
        card = ttk.Frame(parent, style='Card.TFrame')
        card.bind('<Enter>', lambda e: self.on_hover(card, True))
        card.bind('<Leave>', lambda e: self.on_hover(card, False))
        card.bind('<Button-1>', lambda e: command())
        
        icon_label = ttk.Label(card,
            text=icon,
            font=("Segoe UI", 48),
            foreground=COLORS['primary']
        )
        icon_label.pack(pady=(20, 10))
        
        text_label = ttk.Label(card,
            text=text,
            font=FONTS['button'],
            foreground=COLORS['text_primary']
        )
        text_label.pack(pady=(0, 20))
        
        return card
    
    def on_hover(self, card, entering):
        if entering:
            card.configure(cursor="hand2")
            # Add hover effect here (e.g., change background color)
        else:
            card.configure(cursor="")
            # Remove hover effect here

class ModernSearchPage(ttk.Frame):
    """Base class for all search pages"""
    def __init__(self, parent, controller, title, search_label):
        super().__init__(parent)
        self.controller = controller
        
        # Main container
        main_container = ttk.Frame(self, style='Main.TFrame')
        main_container.pack(fill="both", expand=True, padx=40, pady=40)
        
        # Header
        header = ttk.Label(main_container,
            text=title,
            font=FONTS['heading'],
            foreground=COLORS['primary']
        )
        header.pack(pady=(0, 30))
        
        # Search container
        search_container = ttk.Frame(main_container, style='Card.TFrame')
        search_container.pack(fill="x", padx=100, pady=20)
        
        # Search label
        search_label = ttk.Label(search_container,
            text=search_label,
            font=FONTS['subheading'],
            foreground=COLORS['text_primary']
        )
        search_label.pack(pady=(20, 10))
        
        # Search entry
        self.search_entry = ttk.Entry(search_container,
            style='Search.TEntry',
            font=FONTS['body']
        )
        self.search_entry.pack(fill="x", padx=20, pady=(0, 10))
        
        # Search button
        search_btn = ttk.Button(search_container,
            text="Search",
            style='Modern.TButton',
            command=self.search
        )
        search_btn.pack(pady=(0, 20))
        
        # Results container
        self.results_container = ttk.Frame(main_container, style='Main.TFrame')
        self.results_container.pack(fill="both", expand=True, pady=20)
        
        # Back button
        back_btn = ttk.Button(main_container,
            text="Back to Main Menu",
            style='Modern.TButton',
            command=lambda: controller.show_frame("ModernStartPage")
        )
        back_btn.pack(side="bottom", pady=20)
    
    def search(self):
        # Clear previous results
        for widget in self.results_container.winfo_children():
            widget.destroy()
        
        # Get search value and perform search
        value = self.search_entry.get().strip()
        if not value:
            self.show_error("Please enter a search value")
            return
        
        try:
            results = self.perform_search(value)
            self.display_results(results)
        except ValueError as e:
            self.show_error(str(e))
    
    def perform_search(self, value):
        # Override in subclasses
        raise NotImplementedError
    
    def display_results(self, results):
        if not results:
            self.show_error("No results found")
            return
        
        # Results header
        result_header = ttk.Label(self.results_container,
            text=f"Found {len(results)} result(s)",
            font=FONTS['subheading'],
            foreground=COLORS['success']
        )
        result_header.pack(pady=(0, 20))
        
        # Display each result in a card
        for element in results:
            self.create_result_card(element)
    
    def create_result_card(self, element):
        card = ttk.Frame(self.results_container, style='Card.TFrame')
        card.pack(fill="x", padx=100, pady=5)
        
        # Element info
        info_text = f"""
        Full Name: {element.FullName}
        Symbol: {element.Symbol}
        Atomic Number: {element.AtomicNumb}
        Atomic Weight: {element.AtomicW}
        """
        
        info_label = ttk.Label(card,
            text=info_text,
            font=FONTS['body'],
            foreground=COLORS['text_primary'],
            justify="left"
        )
        info_label.pack(padx=20, pady=15)
    
    def show_error(self, message):
        error_label = ttk.Label(self.results_container,
            text=message,
            font=FONTS['body'],
            foreground=COLORS['error']
        )
        error_label.pack(pady=20)

# Create specific search page classes
class SearchByNumber(ModernSearchPage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, "Search by Atomic Number", "Enter Atomic Number:")
    
    def perform_search(self, value):
        try:
            number = int(value)
            return SearchTable(None, None, str(number), None)
        except ValueError:
            raise ValueError("Please enter a valid atomic number")

class SearchByWeight(ModernSearchPage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, "Search by Atomic Weight", "Enter Atomic Weight:")
    
    def perform_search(self, value):
        try:
            weight = float(value)
            return SearchTable(None, None, None, weight)
        except ValueError:
            raise ValueError("Please enter a valid atomic weight")

class SearchByName(ModernSearchPage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, "Search by Element Name", "Enter Element Name:")
    
    def perform_search(self, value):
        return SearchTable(value, None, None, None)

class SearchBySymbol(ModernSearchPage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, "Search by Element Symbol", "Enter Element Symbol:")
    
    def perform_search(self, value):
        return SearchTable(None, value, None, None)

if __name__ == "__main__":
    app = ModernWindow()
    app.mainloop()
