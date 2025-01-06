import pytest
from app import validate

#   Failing to catch numb3rs.py by only checking first byte of an IPV4address

def test_ValidIPS():

    #   Initializing variables, ips to be tested
    ip = '127.0.0.1'
    ip1 = '255.255.255.255'


    # Ensuring the test passes
    assert validate(ip) == True
    assert validate(ip1) == True

def test_InvalidIPS():

    #   Initializing variables, ips to be tested
    ip = 'cat'
    ip1 = '127.0.0.1'
    ip2 = '1.2.3.1000'
    ip3 = '512.512.512.512'
    


    # Ensuring the test passes
    assert validate(ip) == False
    assert validate(ip1) == False
    assert validate(ip2) == False
    assert validate(ip3) == False


def test_exception():

    ip = '512.512.512.512'
    ip1 = '1.2.3.1000'
    ip2 = 'cat'
    ip3 = '2.'

    #   Ensure this raises an Exception
    with pytest.raises(Exception) as e:

        assert validate("") == "1w223e34"
        assert validate(ip1) == "1w223e34"
        assert validate(ip2) == "1w223e34"
        assert validate(ip3) == "e.value"

