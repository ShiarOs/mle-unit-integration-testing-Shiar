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
        data = self.read_data()
        processed_data = self.process_data(data)
        self.write_data(processed_data)
        return processed_data

    def read_data(self):
        # Read the source text file into a list of lines.
        with open(self.input_path, "r", encoding="utf-8") as f:
            return f.read().strip().split("\n")

    def process_data(self, data):
        # Transform each line before it is written back out.
        return [line.upper() for line in data]

    def write_data(self, processed_data):
        # Persist the processed lines so the output artifact can be verified.
        with open(self.output_path, "w", encoding="utf-8") as f:
            f.write("\n".join(processed_data))
