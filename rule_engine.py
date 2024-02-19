from knowledge_base import RISK, MEANS, INVESTMENT_TIME, TIME_TO_SPEND_ON_INVESTMENT
from typing import Optional


def get_fitting_investments_with_weights(
        risk: str,
        means: int,
        investment_time: int,
        commitment_time: str
) -> dict | str:
    exception_msg = check_exceptions(means, investment_time)
    if exception_msg:
        return exception_msg
    weighted_dicts = get_weighted_dicts(risk, means, investment_time, commitment_time)
    fitting_investments = get_fitting_investments(weighted_dicts)
    weight_of_fitting_investments = get_weight_of_fitting_investments(fitting_investments, weighted_dicts)
    return sort_dict_by_value(weight_of_fitting_investments)


def check_exceptions(
        means: int,
        investment_time: int
) -> Optional[str]:
    if means < 100:
        return 'The minimum recommended investment funds are: 100zl.'
    if investment_time < 3:
        return 'The minimum recommended investment time is 3 months.'
    return None


def get_weighted_dicts(
        risk: str,
        means: int,
        investment_time: int,
        commitment_time: str
) -> list[dict]:
    means_value = get_lowest_key_possible(MEANS.keys(), means)
    investment_time_value = get_lowest_key_possible(INVESTMENT_TIME.keys(), investment_time)
    risk_fit = RISK[risk]
    means_fit = MEANS[means_value]
    investment_time_fit = INVESTMENT_TIME[investment_time_value]
    commitment_time_fit = TIME_TO_SPEND_ON_INVESTMENT[commitment_time]
    return [risk_fit, means_fit, investment_time_fit, commitment_time_fit]


def get_lowest_key_possible(
        keys: list[int],
        value: int
) -> int:
    for key in keys:
        if value <= key:
            return key


def get_fitting_investments(
        weighted_dicts: list[dict]
) -> list[str]:
    result = set(weighted_dicts[0])
    for weighted_dicts_idx in range(1, len(weighted_dicts)):
        result = result.intersection(weighted_dicts[weighted_dicts_idx])
    return result


def get_weight_of_fitting_investments(
        fitting_investments: list[str],
        weighted_dicts: list[dict]
) -> dict[str, int]:
    result = {}
    for investment in fitting_investments:
        for weighted_dict in weighted_dicts:
            if investment not in result:
                result[investment] = 0
            result[investment] = result[investment] + weighted_dict[investment]
    for investment in result:
        result[investment] = round(round(result[investment]/len(weighted_dicts), 3) * 100, 1)
    return result


def sort_dict_by_value(
        weight_of_fitting_investments: dict[str, int]
) -> dict[str, int]:
    return dict(sorted(weight_of_fitting_investments.items(), key=lambda item: item[1], reverse=True))
