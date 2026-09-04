"""Integration test for the text-file pipeline implementation target."""

import os

import pytest
from src.integration_test_example.csv_pipeline import DataPipelineCSV


@pytest.fixture(scope="module")


def input_file(tmp_path_factory):
    # Create a temporary input file so the test uses real file I/O.

    input_path = tmp_path_factory.mktemp("data").joinpath("input.txt")
    # print(f"Temporary input file path: {input_path}")  # Debugging line
    print(f"Temporary input file path: {input_path}")  # Debugging line
    input_path.write_text("hello\nworld\n", encoding="utf-8")
    print(f"Temporary input file content: {input_path.read_text(encoding='utf-8')}")  # Debugging line
    return str(input_path)


@pytest.fixture(scope="module")
def output_file(tmp_path_factory):
    # Use a separate temporary output path for the persisted pipeline result.
    output_path = tmp_path_factory.mktemp("data").joinpath("output.txt")
    print(f"Temporary output file path: {output_path}")  # Debugging line
    return str(output_path)


def test_pipeline(input_file, output_file):

    pipeline = DataPipelineCSV(input_file, output_file)
    processed_data = pipeline.run()
    print(f"Pipeline run completed. Processed data: {processed_data}")  # Debugging line

    # Check both the returned value and the written artifact.
    assert os.path.exists(output_file)
    with open(output_file, "r", encoding="utf-8") as file:
        output_data = file.read().strip().split("\n")
    print(f"Output data read from file: {output_data}")  # Debugging line

    assert processed_data == output_data
    assert output_data == ["HELLO", "WORLD"]
