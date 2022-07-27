import pytest
from guns import print_total_deaths, count_children_teens


YEAR_COLUMN = 0
DEATHS_COLUMN = 1
SUICIDES_COLUMN = 2
INJURIES_COLUMN = 3
CHILDREN_COLUMN = 4
TEENS_COLUMN = 5
MASS_COLUMN = 6
MURDER_COLUMN = 7
DEFENSIVE_COLUMN = 8
UNINTENTIONAL_COLUMN = 9


def test_total_deaths():
   """Verify that the total deaths calculations functions work correctly."""

   assert print_total_deaths() 



def test_count_children_teens():
    """Verify that the data produced correct percentage of deaths related to children and teens."""

    assert count_children_teens(513932) == 5.18

pytest.main(["-v", "--tb=line", "-rN", __file__])