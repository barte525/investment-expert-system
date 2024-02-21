from rule_engine import get_fitting_investments_with_weights

INPUT_TO_RISK_MAPPING = {
    '1': 'small',
    '2': 'medium',
    '3': 'big',
}

INPUT_TO_INVOLVEMENT_MAPPING = {
    '1': 'small',
    '2': 'medium',
    '3': 'big',
}


def numeric_input(msg: str) -> int:
    while True:
        result = input(msg)
        if result.isdigit():
            return int(result)


def switch_case_input(msg: str, switch_case_dict: dict) -> str:
    while True:
        result = input(msg)
        if result in switch_case_dict:
            return switch_case_dict[result]


def run_app() -> None:
    risk = switch_case_input(
        '\nEnter an acceptable risk level:\n1: small\n2: medium\n3: big\n',
        INPUT_TO_RISK_MAPPING
    )
    commitment = switch_case_input(
        '\nSpecify an acceptable level of involvement:\n1: small\n2: medium\n3: big\n',
        INPUT_TO_INVOLVEMENT_MAPPING
    )
    means = numeric_input("\nEnter funds for investment (in polish zloty):\n")
    investment_time = numeric_input("\nEnter the investment time (in months):\n")
    result = get_fitting_investments_with_weights(risk, means, investment_time, commitment)
    if type(result) == str:
        print(f'\n{result}')
    else:
        print(f'\nRecommended investments based on the given assumptions:')
        for investment, weight in result.items():
            print(f'{investment} with {weight}% matching')
