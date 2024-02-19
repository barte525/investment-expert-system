from unittest import TestCase
from knowledge_base import INVESTMENT_TIME, TIME_TO_SPEND_ON_INVESTMENT, RISK, MEANS


class TestKnowledgeBase(TestCase):
    def test_if_knowledge_base_is_full(self):
        for investment_time in INVESTMENT_TIME:
            for time_to_spend_on_investment in TIME_TO_SPEND_ON_INVESTMENT:
                for risk in RISK:
                    for means in MEANS:
                        common_elements = list(set(
                            INVESTMENT_TIME[investment_time]).intersection(
                            TIME_TO_SPEND_ON_INVESTMENT[time_to_spend_on_investment]).intersection(
                            RISK[risk]).intersection(
                            MEANS[means])
                        )
                        if not common_elements:
                            print(f"\nError for:\n"
                                  f"investment_time: {investment_time}\n"
                                  f"time_to_spend_on_investment: {time_to_spend_on_investment}\n"
                                  f"risk: {risk}\n"
                                  f"means {means}")
                        self.assertNotEqual(common_elements, [])
