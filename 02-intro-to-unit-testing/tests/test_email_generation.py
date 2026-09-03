"""Regression tests for the email generation implementation target."""

from src.unit_test_examples.email_generation import generate_neuefische_emails


def test_generate_neuefische_emails():
    # Include whitespace and mixed formatting to verify normalization behavior.
    employees = [
        {"first_name": "John", "last_name": "Johnson"},
        {"first_name": " Winnie ", "last_name": "Hopkins"},
        {"first_name": "Basil", "last_name": " Hart "},
    ]

    # This check covers normalization as much as formatting.
    assert generate_neuefische_emails(employees) == [
        "john.johnson@neuefische.de",
        "winnie.hopkins@neuefische.de",
        "basil.hart@neuefische.de",
    ]
