Currency Converter

A simple currency converter web application built with Python, Django, HTML, CSS, and the ExchangeRate-API.

1. Features

   - Convert between multiple currencies
   - Real-time exchange rates using ExchangeRate-API
   - User-friendly interface

2. Technologies Used

   - Python: Backend programming language
   - Django: Web framework for building the application
   - HTML: Markup language for structuring the web pages
   - CSS: Styling language for enhancing the appearance of the application
   - ExchangeRate-API: API for fetching real-time exchange rates

3. Installation

   1. Clone the repository:
      git clone https://github.com/SumedhTardalkar142/currency-convertor.git
   2. Navigate to the project directory:
      cd currency-convertor
   3. Install the required packages:
      pip install -r requirements.txt
   4. Set up your environment variables, including your ExchangeRate-API key.
   5. Run the migrations:
      python manage.py migrate
   6. Start the development server:
      python manage.py runserver
   7. Open your browser and go to http://127.0.0.1:8000 to use the application.

4. Usage

   1. Select the currency you want to convert from.
   2. Enter the amount you wish to convert.
   3. Select the target currency.
   4. Click on the "Convert" button to see the result.


5. Acknowledgments

   - Django - For the powerful web framework
   - ExchangeRate-API - For providing exchange rate data
