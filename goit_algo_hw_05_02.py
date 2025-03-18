import re
from typing import Callable

def generator_numbers(text: str):
    pattern = r'(?<=\s)(\d+\.\d+|\d+)(?=\s)' 
    for match in re.findall(pattern, f" {text} "):  # if it text also can be used floats with integers. 
    #for match in re.findall(r'\d+', text) - if text contain only integers 
        yield float(match) 

def sum_profit(text: str, func: Callable):
    return sum(func(text))

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")

