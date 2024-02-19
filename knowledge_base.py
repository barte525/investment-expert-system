import sys

deposits = 'deposits'
bonds = 'bonds'
dividend_companies = 'dividend companies'
stock_index = 'stock index'
energy_companies = 'energy companies'
REITs = 'REITs'
real_estate = 'real estate'
gold = 'gold'
silver = 'silver'
cryptocurrencies = 'cryptocurrencies'
stable_currencies = 'stable currencies'
trust_funds = 'trust funds'


RISK = {
    'small': {
        deposits: 1,
        bonds: 0.95,
        gold: 0.8,
        stable_currencies: 0.6,
        real_estate: 0.4
    },
    'medium': {
        deposits: 0.3,
        bonds: 0.35,
        gold: 0.4,
        stable_currencies: 0.5,
        real_estate: 0.7,
        dividend_companies: 1,
        trust_funds: 0.9,
        REITs: 0.8,
        silver: 0.7
    },
    'big': {
        deposits: 0.01,
        bonds: 0.02,
        gold: 0.1,
        stable_currencies: 0.15,
        real_estate: 0.2,
        dividend_companies: 0.4,
        trust_funds: 0.5,
        REITs: 0.6,
        silver: 0.65,
        cryptocurrencies: 1,
        energy_companies: 1,
        stock_index: 0.9
    },
}

# in polish zloty
MEANS = {
    1000: {
        deposits: 0.9,
        cryptocurrencies: 1,
        stable_currencies: 1,
        bonds: 0.5
    },
    10000: {
        deposits: 0.5,
        cryptocurrencies: 0.5,
        stable_currencies: 0.25,
        bonds: 1,
        stock_index: 1,
        silver: 1
    },
    100000: {
        deposits: 0.1,
        cryptocurrencies: 0.3,
        bonds: 0.5,
        stock_index: 0.8,
        silver: 0.3,
        energy_companies: 1,
        REITs: 1,
        trust_funds: 1,
        gold: 1,
        dividend_companies: 1,
    },
    sys.maxsize: {
        cryptocurrencies: 0.1,
        bonds: 0.2,
        stock_index: 0.6,
        silver: 0.05,
        energy_companies: 0.3,
        REITs: 0.6,
        trust_funds: 0.7,
        gold: 0.5,
        dividend_companies: 0.6,
        real_estate: 1,
    }
}

# number of months
INVESTMENT_TIME = {
    12: {
        deposits: 1,
        bonds: 0.9,
        cryptocurrencies: 0.5,
        stable_currencies: 0.8
    },
    60: {
        bonds: 1,
        dividend_companies: 0.9,
        energy_companies: 0.7,
        REITs: 1,
        silver: 0.9,
        cryptocurrencies: 1,
        stable_currencies: 0.1,
        trust_funds: 0.8,
        deposits: 0.5
    },
    sys.maxsize: {
        dividend_companies: 1,
        stock_index: 1,
        real_estate: 1,
        gold: 1,
        trust_funds: 0.5,
        silver: 0.5,
        bonds: 0.1
    }
}


TIME_TO_SPEND_ON_INVESTMENT = {
    'small': {
        deposits: 1,
        bonds: 0.9,
        gold: 0.8,
        silver: 0.7,
        cryptocurrencies: 0.9,
        stable_currencies: 1
    },
    'medium': {
        deposits: 0.3,
        bonds: 0.4,
        gold: 0.5,
        silver: 0.8,
        cryptocurrencies: 0.5,
        stable_currencies: 0.3,
        trust_funds: 1,
        REITs: 1,
        dividend_companies: 1,
        stock_index: 1
    },
    'big': {
        deposits: 0.1,
        bonds: 0.2,
        gold: 0.4,
        silver: 0.6,
        cryptocurrencies: 0.2,
        stable_currencies: 0.1,
        trust_funds: 0.5,
        REITs: 0.5,
        dividend_companies: 0.5,
        stock_index: 0.5,
        energy_companies: 0.8,
        real_estate: 1
    }
}

