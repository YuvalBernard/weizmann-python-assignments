import pytest
from helper_functions import count_lines, count_words, count_characters

@pytest.mark.parametrize("sample_text, expected",[
    ("The quick\nbrown fox\njumps over\nthe lazy dog", 4),
    ("This text is 31 characters long", 1)
])
def test_count_lines(sample_text, expected):
    assert count_lines(sample_text) == expected
    
@pytest.mark.parametrize("sample_text, expected",[
    ("The quick brown fox jumps over the lazy dog", 9),
    ("This text is 31 characters long", 6)
])
def test_count_words(sample_text, expected):
    assert count_words(sample_text) == expected

@pytest.mark.parametrize("sample_text, expected",[
    ("The quick brown fox jumps over the lazy dog", 26),
    ("This text is 31 characters long", 31)
])
def test_count_characters(sample_text, expected):
    assert count_characters(sample_text) == expected
