from __future__ import annotations

from   pytemplate.template_class \
                                import TemplateClass
from   pytemplate.cy import CythonClass
import pytest


@pytest.fixture
def template_class():
    yield TemplateClass(3)


def test_get_data(template_class, int_fixture):
    assert template_class.get_data(int_fixture) == [3, 3, 3]


def test_cython(capsys):
    x = 1
    cy = CythonClass(x)
    cy.print()
    captured = capsys.readouterr()
    assert 'print' in captured.out
    assert cy.python_print() == x
