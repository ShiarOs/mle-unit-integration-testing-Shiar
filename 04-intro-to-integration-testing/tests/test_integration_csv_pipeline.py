"""Integration test for the text-file pipeline implementation target."""

import os

import pytest
from src.integration_test_example.csv_pipeline import DataPipelineCSV


@pytest.fixture(scope="module")
def input_file(tmp_path_factory):
    # Create a temporary input file so the test uses real file I/O.
    input_path = tmp_path_factory.mktemp("data").joinpath("input.txt")
    input_path.write_text("hello\nworld\n", encoding="utf-8")
    return str(input_path)


@pytest.fixture(scope="module")
def output_file(tmp_path_factory):
    # Use a separate temporary output path for the persisted pipeline result.
    return str(tmp_path_factory.mktemp("data").joinpath("output.txt"))


def test_pipeline(input_file, output_file):
    pipeline = DataPipelineCSV(input_file, output_file)
    processed_data = pipeline.run()

    # Check both the returned value and the written artifact.
    assert os.path.exists(output_file)
    with open(output_file, "r", encoding="utf-8") as file:
        output_data = file.read().strip().split("\n")

    assert processed_data == output_data
    assert output_data == ["HELLO", "WORLD"]
