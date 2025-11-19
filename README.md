# DIT Lab (Working Title)

**DIT Lab** is an open‑source Python framework for simulating artificial “brains” with superposition‑like internal states interacting with abstract environments over time. It combines a qubit‑style internal model, a controllable environment, and a 4D lab controller (step, pause, rewind, branch) to study how perception, cognition, and overload evolve under changing conditions.

This repo is intended as a **research playground** for:

- DIT‑style *cognitive timelines* (past / present / future zones)  
- Superposition‑like internal “brain” states (qubit‑inspired)  
- Perception vs reality (what the agent thinks the world is vs what it actually is)  
- Temporal control over cognition (time as an experimental variable)  

---

## ✨ Core Ideas

At a high level, DIT Lab is built around four main components:

1. **Environment (`env/`)**  
   A small, controllable abstract world (not necessarily visual/3D at first).  
   Example: a 1D or 2D space with an agent, a threat, noise, light level, etc.

2. **Brain (`brain/`)**  
   An internal state that behaves like a set of “qubits”:
   - represented as vectors / amplitudes  
   - evolves via deterministic + stochastic rules  
   - can be “measured” to yield a perceived environment and self state  
   
   This is where superposition, entropy and DIT‑inspired dynamics live.

3. **LLM Node (`llm/`)**  
   A large language model (external node) that:
   - receives the **true environment** + **brain summary**  
   - returns:
     - suggested updates to internal brain state  
     - a description of **what the brain thinks the environment is**  
   
   The LLM acts as a meta‑controller or “narrator” for cognitive evolution.

4. **4D Lab (`lab/`)**  
   A control layer that:
   - steps the simulation forward  
   - pauses or runs continuously  
   - creates **snapshots** of full state  
   - rewinds to earlier snapshots  
   - branches new timelines from any snapshot  
   
   This turns the simulation into a **time‑playable lab** for cognition.

---

## 🧱 Project Structure

This repository is still in early scaffolding. The following layout shows the intended structure:

```
dit‑lab/
├─ pyproject.toml         # or requirements.txt (to be finalised)
├─ README.md
├─ LICENSE
├─ CONTRIBUTING.md        # (planned)
├─ docs/
│   ├─ index.md
│   └─ design‑overview.md
├─ examples/
│   ├─ minimal_cli_demo.py
│   └─ experiment_chaos_vs_stability.py
├─ src/
│   └─ ditlab/
│       ├─ __init__.py
│       ├─ config/
│       │   ├─ __init__.py
│       │   └─ schemas.py          # pydantic models for configs
│       ├─ env/
│       │   ├─ __init__.py
│       │   ├─ base.py             # EnvState, BaseEnvironment
│       │   └─ simple_1d.py        # first toy environment
│       ├─ brain/
│       │   ├─ __init__.py
│       │   ├─ qubits.py           # QubitBrainState and measurement
│       │   ├─ dynamics.py         # update rules (diffusion, noise)
│       │   ├─ perception.py       # turning internal state into perception
│       │   └─ metrics.py          # entropy, Φ‑like proxies, divergence
│       ├─ graphmodel/
│       │   ├─ __init__.py
│       │   └─ task_graph.py       # DIT/task graph representation
│       ├─ llm/
│       │   ├─ __init__.py
│       │   ├─ client_base.py      # abstract LLM client interface
│       │   ├─ openai_client.py    # or other provider‑specific impls
│       │   └─ prompts.py          # prompt templates & parsing helpers
│       ├─ lab/
│       │   ├─ __init__.py
│       │   ├─ state.py            # FullState, serialisable snapshot
│       │   ├─ timeline.py         # SnapshotManager, branching timelines
│       │   ├─ controller.py       # main simulation step/run logic
│       │   └─ experiments.py      # helpers for defining experiments
│       ├─ ui/
│       │   ├─ __init__.py
│       │   ├─ cli.py              # basic CLI
│       │   └─ textual_app.py      # TUI dashboard (planned)
│       ├─ io/
│       │   ├─ __init__.py
│       │   ├─ logging.py          # JSONL / structured logging
│       │   └─ storage.py          # save/load runs, configs, snapshots
│       └─ util/
│           ├─ __init__.py
│           └─ random_seed.py
└─ tests/
    ├─ test_env.py
    ├─ test_brain.py
    ├─ test_lab.py
    └─ test_llm.py
```

---

## 🛠️ Installation (Dev Mode)

> **Note:** This project is in early scaffolding. Expect changes.

```
git clone https://github.com/your‑username/dit‑lab.git
cd dit‑lab

python -m venv .venv
# Windows:
.\.venv\Scripts\activate
# Mac / Linux:
source .venv/bin/activate

# Temporary: until pyproject.toml is finalised
pip install -r requirements.txt
```

Planned core dependencies:

- `numpy` – vector math, qubit amplitudes  
- `networkx` – DIT‑style task / cognitive graphs  
- `pydantic` – clean data models for states/configs  
- `textual` – TUI‑based “lab dashboard” (later)  
- `matplotlib` or `plotly` – plots for entropy / Φ / metrics  

---

## 🚀 Quick Start (Target)

Once the scaffolding is in place, the goal is to support something like:

```
# Run a minimal CLI simulation
python -m ditlab.ui.cli
```

and see:

- true environment state  
- brain’s perceived environment  
- qubit measurements / probabilities  
- step counter, plus options to:
  - `(n)` next step  
  - `(r)` rewind  
  - `(b)` branch  
  - `(q)` quit  

Later, a TUI dashboard (`textual_app.py`) will provide a richer interface with panels and keybindings.

---

## 📚 Background & Inspiration

This project is inspired by the idea of **DIT (Dit Notation)** and **cognitive timelines**:  
modelling cognition as evolving structures across deep past, recent past, present, near future, and speculative future, with integration and overload dynamics.

The goal of DIT Lab is to turn those ideas into an **executable, inspectable simulation**:  
a place where we can stress‑test cognitive architectures, perception models, and temporal control in a small, controlled “universe”.