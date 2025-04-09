import json
from flask import session


def select_exchange(user_selection, data):
    user_selection = user_selection.strip().lower()
    
    for exchange in data:
        if (user_selection in exchange["stockExchange"].lower()):
            return exchange
    return None


def get_stock_echanges(data):
    stock_exchanges = []
    for exchange in data:
        stock_exchanges.append(exchange["stockExchange"])
    return stock_exchanges


def get_stock_options(data, selected_exchange):
    stock_options = []
    for exchange in data:
        if exchange["stockExchange"].lower() == selected_exchange.lower():
            for stock in exchange["topStocks"]:
                stock_options.append(stock["stockName"])
            break
    return stock_options



def get_stock_price(user_selection, data):
    user_selection = user_selection.strip().lower()
    
    for exchange in data:
        for stock in exchange["topStocks"]:
            if (user_selection in stock["stockName"].lower()):
                return stock["price"]
    return None


def calculate_response(user_selection, session):
    try:
        with open('Chatbot - stock data.json') as f:
            data = json.load(f)

    # add exception for missing file
    except FileNotFoundError:
        return {
            "message": "Data file not found. Please check the file path again.",
            "options": ["Main Menu"]
        }
    
    except json.JSONDecodeError:
        return {
            "message": "Error reading stock data. Please check the file format.",
            "options": ["Main Menu"]
        }
    # Initialize first step
    if "step" not in session:
        session["step"] = "select_stock_exchange"
    
    # Check if user selection is empty
    if user_selection == "":
        return {
            "message": "Invalid option. Please select an option:",
            "options": ["Main menu"]
        }

        
    #Step 0 -> Initialize chat
    if user_selection.lower() == "main menu" or "hello" in user_selection.lower():
        session.clear()
        session["step"] = "select_stock_exchange"
        stock_exchanges = get_stock_echanges(data)
        return {
            "message": "Please select a Stock Exchange:",
            "options": stock_exchanges
        }

    
    #Step 1 -> Select stock exchange
    if session["step"] == "select_stock_exchange":
        # Check if user selected a correct stock exchange 
        if select_exchange(user_selection, data):
            session['selected_exchange'] = user_selection
            session["step"] = "select_stock"

            # Load stocks for selected exchange  
            stocks = get_stock_options(data, user_selection)
            return {
                "message": "Please select a stock:",
                "options": stocks
            }
        # If user selection is not in stock exchange list
        else:
            stock_exchanges = get_stock_echanges(data)
            return {
                "message": "Please select a stock exchange from the list:",
                "options": stock_exchanges
            }


    # Step 2 -> Select stock
    elif session["step"] == "select_stock":
        selected_exchange = session.get('selected_exchange')

        # Go back option
        if user_selection.lower() == "go back":
            session["step"] = "select_stock"
            stocks = get_stock_options(data, selected_exchange)
            return {
                "message": "Please select a stock:",
                "options": stocks
            }
        # Calculate stock price
        stock_price = get_stock_price(user_selection, data)
        if stock_price:
            return {
                "message": f"Stock price for {user_selection} is {stock_price}. Please select an option:",
                "options": ["Main Menu", "Go Back"]
            }
        else:
            return {
                "message": f"Stock {user_selection} is not listed on {selected_exchange}. Please select an option:",
                "options": ["Main Menu", "Go Back"]
            }

    
    
    
    