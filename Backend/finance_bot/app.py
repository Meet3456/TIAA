import json
import openai
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import yfinance as yf
from dotenv import load_dotenv
import os
import sys
from streamlit_lottie import st_lottie
# from exception import CustomException
import requests
ALPHA_VANTAGE_API_KEY = "BKY908VD3O4T0DMG"
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

openai.api_key = api_key


def get_stock_price(ticker):
    return str(yf.Ticker(ticker).history(period='1y').iloc[-1].Close)


def calculate_SMA(ticker, window):
    data = yf.Ticker(ticker).history(period='1y').Close
    return str(data.rolling(window=window).mean().iloc[-1])


def calculate_EMA(ticker, window):
    data = yf.Ticker(ticker).history(period='1y').Close
    return str(data.ewm(span=window).mean().iloc[-1])


def calculate_RSI(ticker):
    data = yf.Ticker(ticker).history(period='1y').Close
    delta = data.diff()
    up = delta.clip(lower=0)
    down = -delta.clip(upper=0)
    ema_up = up.ewm(com=14-1, adjust=False).mean()
    ema_down = down.ewm(com=14-1, adjust=False).mean()
    rs = ema_up/ema_down
    return str(100 - (100 / (1+rs)).iloc[-1])


def calculate_MACD(ticker):
    data = yf.Ticker(ticker).history(period='1y').Close
    short_ema = data.ewm(span=12, adjust=False).mean()
    long_ema = data.ewm(span=26, adjust=False).mean()

    MACD = short_ema - long_ema
    signal = MACD.ewm(span=9, adjust=False).mean()
    MACD_histogram = MACD - signal

    return f'{MACD[-1]},{signal[-1],{MACD_histogram[-1]}}'


def plot_stock_price(ticker):
    data = yf.Ticker(ticker).history(period='1y')
    plt.figure(figsize=(10, 5))
    plt.plot(data.index, data.Close)
    plt.title(f'{ticker} Stock prize over Last Year')
    plt.xlabel('Date')
    plt.ylabel('Stock Price ($)')
    plt.grid()
    plt.savefig('stock.png')
    plt.close()


def plot_risk_return(ticker):
    # Download historical stock data
    data = yf.Ticker(ticker).history(period='1y')

    # Calculate daily returns
    data['Daily_Return'] = data['Close'].pct_change()

    # Calculate volatility (standard deviation of daily returns)
    volatility = data['Daily_Return'].std()

    # Calculate annualized return
    # Assuming 252 trading days in a year
    annualized_return = (1 + data['Daily_Return'].mean()) ** 252 - 1

    # Plotting risk vs. return
    plt.figure(figsize=(8, 6))
    plt.scatter(volatility, annualized_return, marker='o', color='blue')
    plt.title(f'{ticker} Risk vs. Return')
    plt.xlabel('Volatility (Risk)')
    plt.ylabel('Annualized Return')
    plt.grid(True)

    # Save the plot
    plt.savefig('risk_return_plot.png')

    # Close the plot to free up resources
    plt.close()


functions = [
    {
        'name': 'get_stock_price',
        'description': 'gets the latest stock price given the ticker symbol of a company',
        'parameters': {
            'type': 'object',
            'properties': {
                'ticker': {
                    'type': 'string',
                    'description': 'The stock ticker symbol for a company ( for example APPL for Apple) '
                }
            },
            'required': ['ticker']
        }
    },
    {
        'name': 'calculate_SMA',
        'description': 'Calculate simple moving average for a given stock ticker and a window',
        'parameters': {
            'type': 'object',
            'properties': {
                'ticker': {
                    'type': 'string',
                    'description': 'The stock ticker symbol for a company ( for example APPL for Apple) '
                },
                'window': {
                    "type": "integer",
                    "description": "The timeframe to consider while calculating SMA",
                }
            },
            'required': ['ticker', 'window']
        }
    },

    {
        'name': 'calculate_EMA',
        'description': 'Calculate exponential moving average for a given stock ticker and a window',
        'parameters': {
            'type': 'object',
            'properties': {
                'ticker': {
                    'type': 'string',
                    'description': 'The stock ticker symbol for a company ( for example APPL for Apple) '
                },
                'window': {
                    "type": "integer",
                    "description": "The timeframe to consider while calculating EMA",
                }
            },
            'required': ['ticker', 'window']
        }
    },

    {
        'name': 'calculate_RSI',
        'description': 'Calculate the RSI for a given stock ticker',
        'parameters': {
            'type': 'object',
            'properties': {
                'ticker': {
                    'type': 'string',
                    'description': 'The stock ticker symbol for a company ( for example APPL for Apple) '
                }
            },
            'required': ['ticker']
        }
    },

    {
        'name': 'calculate_MACD',
        'description': 'Calculate the MACD for a given stock ticker',
        'parameters': {
            'type': 'object',
            'properties': {
                'ticker': {
                    'type': 'string',
                    'description': 'The stock ticker symbol for a company ( for example APPL for Apple) '
                }
            },
            'required': ['ticker']
        }
    },

    {
        'name': 'plot_stock_price',
        'description': 'plot the stock price for the last year given  ticker symbol for a company',
        'parameters': {
            'type': 'object',
            'properties': {
                'ticker': {
                    'type': 'string',
                    'description': 'The stock ticker symbol for a company ( for example APPL for Apple) '
                }
            },
            'required': ['ticker']
        }
    },

    {
        'name': 'plot_risk_return',
        'description': 'plot the risk vs. return relationship for the last year given  ticker symbol for a company',
        'parameters': {
            'type': 'object',
            'properties': {
                'ticker': {
                    'type': 'string',
                    'description': 'The stock ticker symbol for a company ( for example APPL for Apple) '
                }
            },
            'required': ['ticker']
        }
    },
]

available_functions = {
    'get_stock_price': get_stock_price,
    'calculate_SMA': calculate_SMA,
    'calculate_EMA': calculate_EMA,
    'calculate_RSI': calculate_RSI,
    'calculate_MACD': calculate_MACD,
    'plot_stock_price': plot_stock_price,
    'plot_risk_return': plot_risk_return
}


# st.set_page_config(
#     page_title="Robo-Advisor",
#     page_icon=":chart_with_upwards_trend:",
#     layout="wide",
#     initial_sidebar_state="expanded"

# )
st.set_page_config(
    page_title="Robo-Advisor",
    page_icon=":books:",
    layout="wide",
    initial_sidebar_state="expanded"

)

custom_style = """
<style>
    body {
        background-color: #FFFFFF;
    }
    input {
        font-size: 18px;
    }
</style>
"""

st.markdown(custom_style, unsafe_allow_html=True)

def load_data():
    url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    html = pd.read_html(url, header = 0)
    df = html[0]
    return df
# Sidebar
with st.sidebar:


    df = load_data()
    sector = df.groupby('GICS Sector')

    # Sidebar - Sector selection
    sorted_sector_unique = sorted( df['GICS Sector'].unique() )
    st.markdown("<div class='sidebar-header'>Select Sectors to display the Corresponding Companies:</div>", unsafe_allow_html=True)
    selected_sector = st.sidebar.multiselect('Sectors', sorted_sector_unique, sorted_sector_unique)

    # Filtering data
    df_selected_sector = df[ (df['GICS Sector'].isin(selected_sector)) ]

    st.markdown("<div class='sidebar-content'>", unsafe_allow_html=True)

    st.markdown("<div class='sidebar-header'>Chatbot Information:</div>", unsafe_allow_html=True)
    st.markdown("This chatbot can help you with various tasks, such as:")
    st.markdown("- Answering questions")
    st.markdown("- Providing information")
    st.markdown("- Assisting with tasks")

    st.markdown("<div class='sidebar-header'>Trending Stocks:</div>", unsafe_allow_html=True)

    # Get trending stocks
    trending_stocks = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA']

    for stock_symbol in trending_stocks:
        try:
            # Use Alpha Vantage API for stock information
            alpha_vantage_url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={stock_symbol}&apikey={ALPHA_VANTAGE_API_KEY}"
            response = requests.get(alpha_vantage_url)
            data = response.json()

            if 'Global Quote' in data:
                current_price = float(data['Global Quote']['05. price'])
                previous_close = float(data['Global Quote']['08. previous close'])

                st.markdown("<div class='stock-info'>", unsafe_allow_html=True)
                st.write(f"**{stock_symbol}**")
                st.write(f"Current Price: {current_price}")
                st.write(f"Previous Close: {previous_close}")

                # Mini graph
                # st.line_chart([previous_close, current_price], height=50, use_container_width=True)

                # Price change button
                price_change_color = "green" if current_price > previous_close else "red"
                st.markdown(
                    f"<div class='price-change-button' style='background-color: {price_change_color};'>"
                    f"Price Change: {current_price - previous_close} ({((current_price - previous_close) / previous_close) * 100:.2f}%)"
                    "</div>",
                    unsafe_allow_html=True,
                )

                st.markdown("</div>", unsafe_allow_html=True)
            else:
                st.warning(f"Unable to fetch data for {stock_symbol}")

        except Exception as e:
            st.error(f"Error fetching data for {stock_symbol}: {str(e)}")

    st.markdown("</div>", unsafe_allow_html=True)


left_column, right_column = st.columns([3, 1])
with left_column:
    st.title('Display Companies in Selected Sector')
    st.write('Data Dimension: ' + str(df_selected_sector.shape[0]) + ' rows and ' + str(df_selected_sector.shape[1]) + ' columns.')
    st.dataframe(df_selected_sector)

    st.title("Stock-Bot : Ask me any Stock Related Queries/Information")

    if 'messages' not in st.session_state:
        st.session_state['messages'] = []

    sample_questions = [
        "What is the current price of Google stock?",
        "What are steps to be taken for Retirement Planning",
        "Plot the stock price for Microsoft.",
        "What all things I can do during me retirement"
    ]

    # Display sample questions as buttons
    selected_question = st.selectbox(":blue[Select a sample question:]", sample_questions)

    user_input = st.text_input(":blue[Your Input Questions]", key="user_input")

    if st.button("Submit", key="submit_button"):
        try:
            input_text = user_input if user_input else selected_question
            st.session_state['messages'].append({'role': 'user', 'content': input_text})

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo-0613",
                messages=st.session_state['messages'],
                functions=functions,
                function_call="auto",
            )

            # Extracting the useful info from the response_message:
            response_message = response['choices'][0]['message']

            # AS WE KNOW OUR RESPONSE_MESSAGE MAPS ITSELF TO A FUNCTION TO MATCH THE INPUT ARGUMENT OF THE USER:
            if response_message.get('function_call'):
                function_name = response_message['function_call']['name']

                function_args = json.loads(
                    response_message['function_call']['arguments'])

                if function_name in ['get_stock_price', 'calculate_RSI', 'calculate_MACD', 'plot_stock_price', 'plot_risk_return']:
                    args_dict = {'ticker': function_args.get('ticker')}
                elif function_name in ['calculate_SMA', 'calculate_EMA']:
                    args_dict = {'ticker': function_args.get(
                        'ticker'), 'window': function_args.get('window')}

                functiono_to_call = available_functions[function_name]

                function_response = functiono_to_call(**args_dict)

                if function_name == 'plot_stock_price':
                    st.image('stock.png')

                elif function_name == 'plot_risk_return':
                    st.image('risk_return_plot.png')

                else:
                    st.session_state['messages'].append(response_message)
                    st.session_state['messages'].append(
                        {
                            'role': 'function',
                            'name': function_name,
                            'content': str(function_response),
                        }
                    )

                    second_response = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo-0613",
                        max_tokens = 1024,
                        messages=st.session_state['messages']
                    )

                    st.text(second_response['choices']
                            [0]['message']['content'])
                    st.session_state['messages'].append(
                        {'role': 'assistant', 'content': second_response['choices'][0]['message']['content']})

            else:
                st.text(response_message['content'])
                st.session_state['messages'].append(
                    {'role': 'assistant', 'content': response_message['content']})

            with st.expander("Chat History", expanded=True):
                for message in st.session_state['messages']:
                    if message['role'] == 'user':
                        st.text_input(
                            "User:", message['content'], key=message['content'], disabled=True)
                    elif message['role'] == 'function':
                        st.text_input(
                            f"Function {message['name']}:", message['content'], key=message['content'], disabled=True)

        except Exception as e:
            st.error(f"An error occurred: {e}")

def load_lottiefile(filepath: str):
    with open(filepath, "r") as file:
        return json.load(file)


with right_column:
    st.title("Welcome to Stock-Bot!")

    subheader_text = '<span style="color: blue; font-size:18px">Your personal stock advisor powered by AI!</span>'
    st.markdown(subheader_text, unsafe_allow_html=True)
    lottie = load_lottiefile('hello.json')
    st_lottie(lottie, key="hello")

# ----------------------------------------------------------------------------------------------------------------------------------

def get_stock_data(symbol):
    stock = yf.Ticker(symbol)
    current_price = stock.history(period='1d')['Close'].iloc[-1]
    return current_price


# Streamlit app
st.title('Stock Risk Analyzer')

# Radio buttons for risk level selection
risk_level = st.radio('Select Risk Level:', [
                      'High Risk', 'Moderate Risk', 'Low Risk'])

# Define top 5 companies for each risk level
top_companies = {
    'High Risk': ['AAPL', 'GOOGL', 'PYPL', 'AMZN', 'NVDA'],
    'Moderate Risk': ['JPM', 'INTC', 'IBM', 'JD', 'KO'],
    'Low Risk': ['WBA', 'MS', 'BAC', 'EA', 'ORCL']
}

# Get selected risk level companies
selected_companies = top_companies.get(risk_level, [])

subheader_text = f'<span style="color: blue; font-size:18px">Top 5 {risk_level} Companies To Invest:</span>'
st.markdown(subheader_text, unsafe_allow_html=True)
if selected_companies:
    data = {'Company': selected_companies, 'Current Stock Price': []}
    for company in selected_companies:
        current_price = get_stock_data(company)
        data['Current Stock Price'].append(f'${current_price:.2f}')

    df = pd.DataFrame(data)
    st.table(df.style.set_properties(**{'text-align': 'center'}).set_table_styles(
        [dict(selector='th', props=[('text-align', 'center')])]))
else:
    st.write('No companies found for the selected risk level.')



#-------------------------------------------------------------------------------------------------------------------------------------


lottie1 = load_lottiefile('hello1.json')
st_lottie(lottie1, key="hello1")


#-------------------------------------------------------------------------------------------------------------------------------------
st.header(":mailbox: Get In Touch With Me!")


contact_form = """
<form action="https://formsubmit.co/meetvasa09@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your Feedback!"></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

# Use Local CSS File


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style.css")


#-------------------------------------------------------------------------------------------------------------------------------------


footer = """
<style>
    .footer {
        width: 100%;
        background-color: #f4f4f4;
        padding: 10px;
        text-align: center;
        color: black;
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
    }
</style>
<div class="footer">
    <p>© 2023 Stock-Bot. All rights reserved.</p>
</div>
"""

st.markdown(footer, unsafe_allow_html=True)


#-------------------------------------------------------------------------------------------------------------------------------------


st.markdown(
    """
    <style>

        .sidebar-header {
            color: #007bff;
            font-size: 20px;
            font-weight: bold;
            margin-bottom: 15px;
        }
        .stock-info {
            margin-bottom: 20px;
        }

        .price-change-button {
            padding: 5px 10px;
            border-radius: 5px;
            color: white;
            font-weight: bold;
            margin-top: 10px;
            cursor: pointer;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

