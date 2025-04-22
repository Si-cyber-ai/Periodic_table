# Periodic Table Explorer Pro

A modern, user-friendly desktop application for exploring and searching the periodic table of elements. Built with Python and Tkinter, this application provides an intuitive interface for chemistry students, educators, and professionals.

## Features

- **Multiple Search Options:**
  - Search by Atomic Number
  - Search by Atomic Weight
  - Search by Element Name
  - Search by Element Symbol

- **Modern UI Design:**
  - Clean and intuitive interface
  - Responsive layout
  - Professional color scheme
  - Card-based design

- **Search Capabilities:**
  - Exact matching for atomic numbers and symbols
  - Partial matching for element names
  - Atomic weight search with ±0.1 margin of error
  - Clear result display

## Installation

1. Ensure you have Python 3.x installed on your system
2. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/periodic-table-explorer.git
   ```
3. Navigate to the project directory:
   ```bash
   cd periodic-table-explorer
   ```
4. Install required dependencies:
   ```bash
   pip install tkinter
   ```

## Usage

1. Run the application:
   ```bash
   python Periodic_Table_Code.py
   ```

2. Select your preferred search method from the main menu:
   - ⚛ Search by Atomic Number
   - ⚖ Search by Atomic Weight
   - 📝 Search by Element Name
   - 🔍 Search by Element Symbol

3. Enter your search criteria in the search field

4. View detailed results including:
   - Full Element Name
   - Chemical Symbol
   - Atomic Number
   - Atomic Weight

## Technical Details

- **Programming Language:** Python 3.x
- **GUI Framework:** Tkinter
- **Design Pattern:** Object-Oriented Programming
- **Data Structure:** Custom Element class for storing element information

## Project Structure

```
periodic-table-explorer/
│
├── Periodic_Table_Code.py    # Main application file
├── README.md                 # Project documentation
└── requirements.txt          # Project dependencies
```

## Features in Detail

### Search Methods

- **Atomic Number Search:**
  - Enter any atomic number (1-118)
  - Returns exact matches

- **Atomic Weight Search:**
  - Enter atomic weight
  - Includes ±0.1 margin of error for practical purposes

- **Element Name Search:**
  - Case-insensitive search
  - Supports partial name matching

- **Symbol Search:**
  - Case-insensitive search
  - Requires exact symbol match

### User Interface

- Modern color scheme with professional aesthetics
- Responsive design that adapts to window size
- Clear navigation with intuitive icons
- Error handling with user-friendly messages
- Card-based result display for better readability

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Acknowledgments

- Periodic Table data sourced from official chemical databases
- UI design inspired by modern Material Design principles
- Special thanks to the Python and Tkinter communities


## Future Enhancements

- Add element properties like electron configuration
- Include visual representation of atomic structure
- Add export functionality for search results
- Implement advanced filtering options
- Add interactive periodic table view
