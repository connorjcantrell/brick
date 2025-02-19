"""
Generates tests automatically
"""
import pytest
import ontoenv
import brickschema
import glob
import sys

sys.path.append("..")
from bricksrc.namespaces import QUDT, RDF, RDFS, BRICK  # noqa: E402


def pytest_generate_tests(metafunc):
    """
    Generates Brick tests for a variety of contexts
    """

    # validates that example files pass validation
    if "filename" in metafunc.fixturenames:
        # example_files_1 = glob.glob("examples/*.ttl")
        example_files = glob.glob("examples/*/*.ttl")
        # example_files = set(example_files_1 + example_files_2)
        metafunc.parametrize("filename", example_files)


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "slow: mark tests as slow (deselect w/ '-m \"not slow\"')"
    )


@pytest.fixture()
def brick_with_imports():
    env = ontoenv.OntoEnv()
    g = brickschema.graph.Graph()
    g.load_file("Brick.ttl")
    g.bind("qudt", QUDT)
    g.bind("rdf", RDF)
    g.bind("rdfs", RDFS)
    g.bind("brick", BRICK)
    env.import_dependencies(g)
    return g
