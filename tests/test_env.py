"""Basic tests for the environment module."""

from ditlab.env.base import BaseEnvironment, EnvironmentState
from ditlab.env.simple_1d import Simple1DEnvironment


def test_environment_initialisation() -> None:
    env = Simple1DEnvironment(size=5)
    assert isinstance(env.state, EnvironmentState)
    assert env.state.size == 5