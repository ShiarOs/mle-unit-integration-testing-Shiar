"""Reference solution for the email generation exercise."""


def generate_neuefische_emails(employees):
    """Generate emails as <first_name>.<last_name>@neuefische.de.

    We normalize each name component with strip() and lower() so
    extra spaces and casing differences do not affect the output.
    """

    return [
        # Build one normalized email address per employee record.
        f"{employee['first_name'].strip().lower()}.{employee['last_name'].strip().lower()}@neuefische.de"
        for employee in employees
    ]
