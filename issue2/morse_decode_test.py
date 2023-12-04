import pytest
from morse import decode

@pytest.mark.parametrize("morse_input, expected_output", [
    ('... --- ...', 'SOS'),
    ('.... . .-.. .-.. --- --..--   .-- --- .-. .-.. -.. -.-.--', 'HELLO, WORLD!'),
    ('--. .- -... --. . -', 'GABGET'),
    ('- .... .. -. -.-. . -... . -- -.. -.--', 'THINK BETTER MY FRIEND'),
])
def test_decode(morse_input, expected_output):
    result = decode(morse_input)
    assert result == expected_output
