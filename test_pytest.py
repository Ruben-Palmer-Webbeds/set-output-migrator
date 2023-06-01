import argparse
from contextlib import nullcontext as does_not_raise
from unittest import mock
import sys
import os

sys.path.append(os.getcwd() + "/..")

import pytest

from setOutputDeprecation import file_path, replace_output_line, main

good_file_path: str = "C:/Users/RubénPalmerPérez/Documents/platform/set-output-deprecation/tests/test.yaml"


@pytest.mark.parametrize(
    "path, expected",
    [
        (good_file_path, does_not_raise()),
        ("/path/to/invalid/file.txt", pytest.raises(argparse.ArgumentTypeError)),
    ],
)
def test_file_path(path, expected):
    with expected:
        file_path(path)


@pytest.mark.parametrize(
    "line, expected",
    [
        ("echo 'Hello, world!'", "echo 'Hello, world!'"),
        ('echo "::set-output name=foo::bar"', 'echo "foo=bar" >> $GITHUB_OUTPUT'),
    ],
)
def test_replace_output_line(line, expected):
    result = replace_output_line(line)
    assert result == expected
