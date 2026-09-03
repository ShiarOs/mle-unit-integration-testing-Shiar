# @TODO Exercise (file-based):
# Objective: Build and verify a text-file integration pipeline end-to-end.
# Edit files:
# - src/integration_test_example/csv_pipeline.py
# Validate with:
# - ../.venv/bin/python -m pytest -q tests/test_integration_csv_pipeline.py
# Solution:
# - 04-intro-to-integration-testing.ipynb (Solution toggle block)


class DataPipelineCSV:
    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path

    def run(self):
        # Coordinate the full read -> process -> write flow and return the result.
        raise NotImplementedError("Implement run in csv_pipeline.py")

    def read_data(self):
        # Read the source text file into a list of lines.
        raise NotImplementedError("Implement read_data in csv_pipeline.py")

    def process_data(self, data):
        # Transform each line before it is written back out.
        raise NotImplementedError("Implement process_data in csv_pipeline.py")

    def write_data(self, processed_data):
        # Persist the processed lines so the output artifact can be verified.
        raise NotImplementedError("Implement write_data in csv_pipeline.py")
