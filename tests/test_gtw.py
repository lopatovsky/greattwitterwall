import pytest
import greattwitterwall as gtw
import flexmock


@pytest.fixture
def gen_b():
    return 8

@pytest.mark.parametrize('a', range(1,20,2) )
def test_suma(a, gen_b ):
    """Test suma"""
    #flexmock(gtw, suma=9 )
    s = gtw.suma(a,gen_b)
    assert (s == a+gen_b)
