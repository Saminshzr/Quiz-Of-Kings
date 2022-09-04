import os.path
from distutils.version import LooseVersion
from unittest import TestCase

import pytest

import run


class TestPackageFilesExistence(TestCase):
    list_of_exam_packages_files = [
        "src/exam.py",
        "src/user.py"
    ]

    @pytest.mark.skipif(LooseVersion(run.__version__) < LooseVersion("0.0.1"), reason="demonstrating skipping")
    def test_main_files(self):
        for file_name in self.list_of_exam_packages_files:
            assert os.path.exists(file_name), f'File {file_name} wan\'t found!'
