import os.path
import unittest
from distutils.version import LooseVersion
from unittest import TestCase

import run


class TestPackageFilesExistence(TestCase):
    list_of_exam_packages_files = [
        "src/exam.py",
        "src/user.py"
    ]

    @unittest.skipIf(LooseVersion(run.__version__) < LooseVersion("0.0.1"), "demonstrating skipping")
    def test_main_files(self):
        for file_name in self.list_of_exam_packages_files:
            if not os.path.exists(file_name):
                raise FileNotFoundError(f'File {file_name} wan\'t found!')
