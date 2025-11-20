# Johnny's Rant–Driven Task List

This document is generated from Johnny's after‐work rant to his wife, where he explained the unrealistic demands placed on him by his boss and outlined what a sensible roadmap would look like. The tasks below turn those complaints into concrete, actionable work items for the project.

> “Today he walks in, Mira… and he drops ANOTHER one of those ‘big visionary tasks’ on me. Like— *‘Johnny, create a live cognitively simulated universe accessed through the web.’* … He wants it beta‑testable, scalable, documented, full dashboard, snapshot timelines, multiverse branching… He talks like ChatGPT is my cousin and physics is optional.” — Johnny

## Phase 1 – Core Simulation Engine

- **Task 1.1** – Implement the *Simple1DEnvironment* stepping logic. Handle actions "left", "right", "stay" and update agent positions and threat positions accordingly.
- **Task 1.2** – Implement the qubit brain update logic. Create functions in `brain/dynamics.py` to apply bias, decoherence, and renormalisation based on textual instructions.
- **Task 1.3** – Implement qubit measurement and perception generation. Use `brain/qubits.py` and `brain/perception.py` to summarise the state and produce a perceived environment.
- **Task 1.4** – Implement the snapshot manager in `lab/state.py` and `lab/timeline.py` to allow saving, rewinding and branching of the simulation state.
- **Task 1.5** – Build an initial command‑line interface that calls into the simulation controller, steps the simulation, prints the true and perceived environment, and allows resetting and branching.

## Phase 2 – API and Automation Layer

- **Task 2.1** – Wrap the simulation controller in a FastAPI application (see `src/ditlab/api.py`). Define endpoints for `/reset`, `/step` and `/state`.
- **Task 2.2** – Replace the placeholder `FakeLLMClient` with a configurable LLM client (e.g. `OpenAIClient`). Provide fallback behaviour when API keys are missing.
- **Task 2.3** – Add error handling and validation to the API. Return appropriate status codes and messages when requests are invalid or the simulation is not initialised.
- **Task 2.4** – Create an automated task generation script (see below) that analyses Johnny’s rants and produces new tasks when the scope creeps. The script should parse sentences describing unrealistic expectations and automatically break them into smaller tasks.

## Phase 3 – Web Dashboard

- **Task 3.1** – Design a simple web dashboard using FastAPI with Jinja templates. Render the true environment, perceived environment and qubit statistics on a single page.
- **Task 3.2** – Implement user controls for stepping, resetting, rewinding and branching through HTML forms or JavaScript buttons.
- **Task 3.3** – Visualise qubit amplitudes and measurement probabilities with charts (e.g. using a Python plotting library rendered to SVG).
- **Task 3.4** – Display the snapshot timeline and allow users to jump to any previous snapshot.

## Phase 4 – Experiment Designer and Research Tools

- **Task 4.1** – Build a configuration interface that lets users define custom environments (size, threat distribution, noise levels) and brain configurations (number of qubits, initial amplitudes).
- **Task 4.2** – Implement a run‑manager that can execute multiple experiments, record metrics (entropy, Φ proxy, divergence), and compare runs.
- **Task 4.3** – Create a research pipeline that logs errors (e.g. LLM hallucinations, qubit runaway) and tracks research questions. Each log entry should include reproduction steps and potential fixes.
- **Task 4.4** – Document the API, CLI and dashboard for external users. Write a user manual and developer reference.

## Phase 5 – Stretch Goals (Multi‑Agent Universe)

- **Task 5.1** – Extend the environment to support multiple agents with independent brains. Implement inter‑agent communication and entanglement.
- **Task 5.2** – Implement parallel timeline simulations and multiverse branching with different initial seeds.
- **Task 5.3** – Investigate emotional and belief systems layered on top of the qubit brain model.
- **Task 5.4** – Deploy the application to a cloud environment for open beta testing. Ensure security and scalability.

## Automated Task Generator Concept

The automated task generator should listen to a block of text (Johnny’s rant) and extract tasks based on patterns like:

- Sentences containing *“build”*, *“create”*, *“implement”* → break into sub‑features.
- Sentences complaining about unrealistic timelines → infer a need to re‑order tasks into phases.
- Sentences mentioning features (dashboards, snapshots, multiverse) → add tasks in the appropriate phase.

Pseudo‑code:

```python
import re

def generate_tasks_from_rant(rant: str) -> list[str]:
    tasks = []
    for sentence in rant.split('.'):
        sentence = sentence.strip().lower()
        if 'dashboard' in sentence:
            tasks.append('Design and implement the web dashboard UI')
        if 'snapshot' in sentence:
            tasks.append('Implement snapshot save and rewind functionality')
        if 'multiverse' in sentence:
            tasks.append('Add multiverse branching and timeline comparison tools')
        # Add more patterns here...
    return tasks

# Example usage
rant = (
    "He wants everything at once: live interactive timeline, endless features, multiverse branching. "
    "I suggested we break it down." )
print(generate_tasks_from_rant(rant))
```

You can integrate this function into your CI pipeline or a CLI tool. After each meeting, paste Johnny’s notes and automatically generate new GitHub issues or update this tasks document.