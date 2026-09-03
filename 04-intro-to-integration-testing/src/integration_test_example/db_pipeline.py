# @TODO Exercise (file-based):
# Objective: Build and verify an SQLite-to-CSV integration pipeline end-to-end.
# Edit files:
# - src/integration_test_example/db_pipeline.py
# Validate with:
# - ../.venv/bin/python -m pytest -q tests/test_integration_db_pipeline.py
# Solution:
# - 04-intro-to-integration-testing.ipynb (Solution toggle block)


class DataPipelineDB:
    def __init__(self, input_path, output_path, table_name):
        self.input_path = input_path
        self.output_path = output_path
        self.table_name = table_name

    def run(self):
        # Coordinate the full database -> transform -> CSV pipeline.
        raise NotImplementedError("Implement run in db_pipeline.py")

    def read_data(self):
        # Read the SQLite table into a DataFrame for downstream processing.
        raise NotImplementedError("Implement read_data in db_pipeline.py")

    def process_data(self, data):
        # Transform the in-memory DataFrame before it is written to CSV.
        raise NotImplementedError("Implement process_data in db_pipeline.py")

    def write_data(self, processed_data):
        # Persist the processed DataFrame so the written artifact can be checked.
        raise NotImplementedError("Implement write_data in db_pipeline.py")
