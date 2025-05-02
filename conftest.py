import pytest
import json

@pytest.fixture(scope="session")
def env():
    """
    Retrieves the contents of the secrets file for use in tests

    Returns:
        dict: secrets json object
    """

    with open("secrets.json", "r") as f:
        return json.load(f)

@pytest.fixture(scope="session")
def data():
    """
    Retrieves the contents of the test data file for use in tests

    Returns:
        dict: test data object
    """

    with open("data.json", "r") as f:
        return json.load(f)