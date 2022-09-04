import types
import unittest
import uuid
from distutils.version import LooseVersion
from unittest import TestCase

import run
from src.exam import *


class TestExamPackage(TestCase):
    @unittest.skipIf(LooseVersion(run.__version__) < LooseVersion("0.0.1"), "demonstrating skipping")
    def test_attributes(self):
        exam = Exam()
        exam_arbitrary_attributes = {
            'exam_id': str,
            'questions': list,
            'answers': list,
            'keys': list,
            'name': str,
        }

        for attribute in exam_arbitrary_attributes:
            self.assertIn(attribute, dir(exam), f'`{attribute}` was not found in Exam class attributes.')
            if not isinstance(getattr(exam, attribute), exam_arbitrary_attributes.get(attribute)):
                raise AttributeError(f'`{attribute}` isn\'t {exam_arbitrary_attributes.get(attribute)}.')

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

    @unittest.skipIf(LooseVersion(run.__version__) < LooseVersion("0.0.2"), "demonstrating skipping")
    def test_init_method(self):
        pass

    @unittest.skipIf(LooseVersion(run.__version__) < LooseVersion("0.0.2"), "demonstrating skipping")
    def test_get_new_exam_method(self):
        new_exam = Exam.get_new_exam('test_exam')
        self.assertEqual(10, len(new_exam.questions))
        self.assertEqual(10, len(new_exam.answers))
        self.assertEqual(10, len(new_exam.keys))
        uuid.UUID(new_exam.exam_id)

    @unittest.skipIf(LooseVersion(run.__version__) < LooseVersion("0.0.2"), "demonstrating skipping")
    def test_load_method(self):
        pass

    @unittest.skipIf(LooseVersion(run.__version__) < LooseVersion("0.0.2"), "demonstrating skipping")
    def test_export_method(self):
        pass
