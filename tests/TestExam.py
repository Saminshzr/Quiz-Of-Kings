import types
import unittest
from distutils.version import LooseVersion
from unittest import TestCase

import run
from src.exam import *


class TestExamPackage(TestCase):
    @unittest.skipIf(LooseVersion(run.__version__) < LooseVersion("0.0.1"), "demonstrating skipping")
    def test_attributes(self):
        exam = Exam()
        exam_arbitrary_attributes = [
            'exam_id',
            'questions',
            'answers',
            'keys',
            'name',
        ]

        for attribute in exam_arbitrary_attributes:
            self.assertIn(attribute, dir(exam), f'`{attribute}` was not found in Exam class attributes.')

    @unittest.skipIf(LooseVersion(run.__version__) < LooseVersion("0.0.1"), "demonstrating skipping")
    def test_methods(self):
        exam = Exam()
        exam_arbitrary_methods = [
            '__init__',
            'get_new_exam',
            'load',
            'export',
        ]

        exam_arbitrary_static_methods = [
            'get_new_exam'
        ]

        for attribute in exam_arbitrary_methods:
            self.assertIn(attribute, dir(exam), f'`{attribute}` was not found in Exam class methods.')
            if not callable(getattr(exam, attribute)):
                raise AttributeError(f'`{attribute}` attribute isn\'t callable.')

        for method in exam_arbitrary_static_methods:
            if not isinstance(getattr(exam, method), types.FunctionType):
                raise AttributeError(f'`{method}` method isn\'t static.')
