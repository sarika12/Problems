import pytest

def reversed_text(text):
    if not isinstance(text,str):
        raise ValueError("Expected string")
    return text[::-1]