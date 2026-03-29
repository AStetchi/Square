from pathlib import Path

import bcoding
import pytest

from main import main

allfiles = Path("tests/torrents")
torrentsfiles = [file for file in allfiles.iterdir() if not file.name.startswith(".")]


@pytest.mark.parametrize("filename", torrentsfiles)
def test_main(filename):

    with open(filename, "rb") as file:
        assert main(file) == bcoding.bdecode(file)
