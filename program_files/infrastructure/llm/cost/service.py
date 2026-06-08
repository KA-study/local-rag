

from program_files.shared.schemas import PRICE_TABLE


def calc_cost(input_tokens: int, output_tokens: int, model_name: str) -> float:
    
    if model_name in PRICE_TABLE.keys():
        cost = (
            input_tokens*PRICE_TABLE[model_name].input_fee+
            output_tokens*PRICE_TABLE[model_name].output_fee
        )

    else: 
        raise ValueError(f"Unregistared model name: {model_name}.")

    return cost
 
