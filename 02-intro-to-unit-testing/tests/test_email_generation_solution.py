"""Reference tests for the email generation solution module."""

from src.unit_test_examples.email_generation_solution import generate_neuefische_emails


def test_generate_neuefische_emails_solution():
    # Include whitespace and mixed formatting to verify normalization behavior.
    employees = [
        {"first_name": "John", "last_name": "Johnson"},
        {"first_name": " Winnie ", "last_name": "Hopkins"},
        {"first_name": "Basil", "last_name": " Hart "},
    ]

    # Expected output always strips spaces and lowercases both name parts.
    assert generate_neuefische_emails(employees) == [
        "john.johnson@neuefische.de",
        "winnie.hopkins@neuefische.de",
        "basil.hart@neuefische.de",
    ]
