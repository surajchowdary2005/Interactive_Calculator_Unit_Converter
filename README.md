# Interactive Calculator & Unit Converter

A beginner-friendly web application built using Python, Flask, HTML, and CSS. It provides basic arithmetic operations, unit conversions, and currency conversion through a clean and responsive interface.

## Features

- **Basic Calculator:** Addition, subtraction, multiplication, and division.
- **Unit Converter:** Convert kilometers to miles and Celsius to Fahrenheit.
- **Currency Converter:** Convert INR to USD and USD to INR using a sample exchange rate.
- **Input Validation:** Handles invalid inputs and division by zero.
- **Responsive Design:** Simple interface that works on desktop and mobile screens.

## Technologies Used

- Python
- Flask
- HTML5
- CSS3

## Project Structure

```text
Interactive_Calculator_Unit_Converter/
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/surajchowdary2005/Interactive_Calculator_Unit_Converter.git
```

### 2. Open the project folder

```bash
cd Interactive_Calculator_Unit_Converter
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

For Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install Flask

```bash
pip install flask
```

### 6. Run the application

```bash
python app.py
```

Open your browser and visit:

http://127.0.0.1:5000

## Example Conversions

| Feature | Input | Example Output |
|---|---|---|
| Addition | 10 + 5 | 15 |
| Kilometers to Miles | 10 km | 6.21 miles |
| Celsius to Fahrenheit | 25°C | 77°F |
| INR to USD | ₹830 | $10.00 USD |

**Note:** Currency conversion uses a sample rate of ₹83 per USD. It does not provide live exchange rates.

## Learning Objectives

- Understand Python functions and conditional statements.
- Handle user input and validate values.
- Build a web application using Flask.
- Connect HTML forms with Python backend logic.
- Style a responsive interface using CSS.

## Author

Suraj Chowdary

## License

This project is created for educational and learning purposes.
