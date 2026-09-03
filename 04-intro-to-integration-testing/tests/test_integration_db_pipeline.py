"""Integration test for the SQLite-to-CSV pipeline implementation target."""

import os

import pandas as pd
import pytest
from pandas.testing import assert_frame_equal
from sqlalchemy import create_engine
from src.integration_test_example.db_pipeline import DataPipelineDB


@pytest.fixture(scope="module")
def input_path(tmp_path_factory):
    # Seed a temporary SQLite database so the test uses real DB I/O.
    database_path = tmp_path_factory.mktemp("test_data").joinpath("input.db")
    engine = create_engine("sqlite:///" + str(database_path), echo=False)
    sample_data = pd.DataFrame({"names": ["mary", "john"], "age": [25, 30]})
    sample_data.to_sql("table", con=engine, index=False)
    return str(database_path)


@pytest.fixture(scope="module")
def output_path(tmp_path_factory):
    # The pipeline writes its result here, and the test reads it back in.
    return str(tmp_path_factory.mktemp("test_data").joinpath("output.csv"))


def test_data_pipeline(input_path, output_path):
    pipeline = DataPipelineDB(input_path, output_path, "table")
    processed_data = pipeline.run()

    # This checks the full workflow, not just one helper method.
    assert os.path.exists(output_path)
    output_data = pd.read_csv(output_path)

    assert processed_data.equals(output_data)
    assert_frame_equal(
        pd.DataFrame({"names": ["MARY", "JOHN"], "age": [25, 30]}),
        output_data,
    )
