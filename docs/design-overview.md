# Design Overview

This document is a high‑level overview of the planned architecture for the DIT Lab project. It will be expanded with diagrams, component descriptions, and rationale as development progresses.

## Components

- **Environment (`env`)**: defines the world in which the agent operates. Initially this will be a simple 1D or 2D space with a few attributes (e.g., position of agent and threats, light and noise levels).
- **Brain (`brain`)**: represents the internal cognitive state of the agent. Inspired by qubits, the state uses complex amplitudes or probability vectors to represent superposition of cognitive elements. It includes functions to evolve this state and measure it to produce perceptions.
- **LLM Node (`llm`)**: acts as a reasoning layer that interprets the true environment and the brain’s current state to suggest state updates and produce the agent’s perceived environment.
- **Lab (`lab`)**: orchestrates the simulation, handles the stepping of time, snapshotting and branching of timelines, and coordinates interactions between the environment, brain, and LLM node.
- **Graph Model (`graphmodel`)**: uses networkx to represent DIT‑style task graphs and compute metrics like entropy and integration.

Further details will be elaborated as the modules are implemented.