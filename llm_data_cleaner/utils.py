from typing import List

import pandas as pd


def batch_dataframe(df: pd.DataFrame, batch_size: int) -> List[pd.DataFrame]:
    """
    Split a DataFrame into batches.

    Args:
        df: Input DataFrame
        batch_size: Size of each batch

    Returns:
        List of DataFrame batches
    """
    if len(df) <= batch_size:
        return [df]
    
    return [df[i:i + batch_size] for i in range(0, len(df), batch_size)]


def validate_instructions(instructions: dict) -> List[str]:
    """
    Validate the cleaning instructions.

    Args:
        instructions: Dictionary of cleaning instructions

    Returns:
        List of validation errors, empty if valid
    """
    errors = []
    
    for column, instruction in instructions.items():
        if not isinstance(column, str):
            errors.append(f"Column name must be a string, got {type(column)}")
        
        if not isinstance(instruction, dict):
            errors.append(f"Instruction for column '{column}' must be a dictionary")
            continue
        
        if "prompt" not in instruction:
            errors.append(f"Missing 'prompt' in instructions for column '{column}'")
        
        if not isinstance(instruction.get("prompt", ""), str):
            errors.append(f"Prompt for column '{column}' must be a string")
        
        if "schema" in instruction and not isinstance(instruction["schema"], dict):
            errors.append(f"Schema for column '{column}' must be a dictionary")
    
    return errors