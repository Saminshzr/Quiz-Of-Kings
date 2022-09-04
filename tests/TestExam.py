import types
import uuid
from distutils.version import LooseVersion

import pytest

import run
from src.exam import *


class TestExamPackage():
    @pytest.mark.skipif(LooseVersion(run.__version__) < LooseVersion("0.0.2"), reason="demonstrating skipping")
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
            assert attribute in dir(exam), f'`{attribute}` was not found in Exam class attributes.'
            assert isinstance(getattr(exam, attribute), exam_arbitrary_attributes.get(attribute)), f'`{attribute}` isn\'t {exam_arbitrary_attributes.get(attribute)}.'

    @pytest.mark.skipif(LooseVersion(run.__version__) < LooseVersion("0.0.2"), reason="demonstrating skipping")
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
            assert attribute in dir(exam), f'`{attribute}` was not found in Exam class methods.'
            assert callable(getattr(exam, attribute)), f'`{attribute}` attribute isn\'t callable.'

        for method in exam_arbitrary_static_methods:
            assert isinstance(getattr(exam, method), types.FunctionType), f'`{method}` method isn\'t static.'

    @pytest.mark.skipif(LooseVersion(run.__version__) < LooseVersion("0.0.3"), reason="demonstrating skipping")
    def test_init_method(self):
        pass

    @pytest.mark.skipif(LooseVersion(run.__version__) < LooseVersion("0.0.3"), reason="demonstrating skipping")
    def test_get_new_exam_method(self):
        new_exam = Exam.get_new_exam('test_exam')

        assert len(new_exam.questions) == 10
        assert len(new_exam.answers) == 10
        assert len(new_exam.keys) == 10

        uuid.UUID(new_exam.exam_id)

    @pytest.mark.skipif(LooseVersion(run.__version__) < LooseVersion("0.0.3"), reason="demonstrating skipping")
    def test_load_method(self):
        pass

    @pytest.mark.skipif(LooseVersion(run.__version__) < LooseVersion("0.0.3"), reason="demonstrating skipping")
    def test_export_method(self):
        pass
