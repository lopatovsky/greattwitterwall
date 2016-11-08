import pytest
import greattwitterwall as gtw
# moze sa to importovat znovu od nova from .greattwitterwall import *,  potom v __init__.py nemusi byt *, ale len verejne rozhranie.
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


"""
import betamax

with betamax.Betamax.configure() as config:
    config.cassette_library_dir = 'tests/fixtures/cassettes'

def test_get(betamax_session):
    betamax_session.get('https://httpbin.org/get')


class Client:
    def __init__(self, session=None):
        self.session = session or requests.Session()


def test_search(betamax_session):
    client = Client(betamax_session)
    assert client.foo() == 42
"""
