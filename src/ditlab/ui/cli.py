"""Basic command-line interface for DIT Lab.

This CLI allows a user to step through the simulation, view the true
environment state and the perceived environment, and rewind or branch
timelines. It is deliberately simple and synchronous; more advanced
interfaces will be added in later versions.
"""

from typing import Any

from ditlab.config.schemas import LabConfig
from ditlab.llm.client_base import LLMClientBase
from ditlab.lab.experiments import Experiment


def run_cli() -> None:
    """Run the command-line simulation loop."""
    # Load default configuration
    config = LabConfig()
    experiment = Experiment(config=config)
    controller = experiment.create_controller()

    print("Starting DIT Lab CLI simulation. Use commands: n (next), r (rewind), q (quit).\n")

    while True:
        cmd = input("Command [n/r/q]: ").strip().lower()
        if cmd == "q":
            print("Exiting simulation.")
            break
        elif cmd == "r":
            try:
                snapshot = controller.snapshots.rewind()
                controller.env.state = snapshot.env_state
                controller.brain = snapshot.brain_state
                controller.time_step = snapshot.time_step
                print(f"Rewound to time step {snapshot.time_step}.")
            except IndexError:
                print("No previous snapshots to rewind to.")
            continue
        else:
            # On any other command, including 'n' or empty, step once
            env_state, perceived = controller.step_once()
            print(f"\nTime step {controller.time_step}")
            print("True environment:", env_state.to_dict())
            print("Perceived environment:", perceived)
            print()


if __name__ == "__main__":  # pragma: no cover
    run_cli()