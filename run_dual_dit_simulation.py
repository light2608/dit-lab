"""A quick demonstration of two DIT agents interacting and becoming
entangled through emotional language input.

This script simulates a simple scenario in which a neutral cognitive
agent (Dit A) becomes entangled with another agent (Dit B) that
produces emotionally charged words.  The strength of the entanglement
grows with the emotional intensity of the language, and this is
reflected both in the quantum state and in a simple colour-coded
activity indicator.

The intent of this script is not to produce a physically accurate
quantum model but rather to illustrate how our DIT simulation could
respond to external emotional input and visualise internal state
changes.  It should run without any external API dependencies.

Usage:
    PYTHONPATH=src python run_dual_dit_simulation.py
"""

from __future__ import annotations

import json
import random
from typing import List, Tuple

import numpy as np

from ditlab.brain.qubits import QubitBrainState


def colour_from_activity(activity: float, emotion: float) -> str:
    """Map activity and emotion levels to a simple colour name.

    The activity value represents the maximum probability amplitude in
    the measured qubit state (0-1).  The emotion value is a random
    measure of how emotionally charged the input language is (0-1).

    Returns a colour string representing the qualitative state of the
    agent.  Highly active and highly emotional states are red or
    orange; low activity and low emotion states are blue or purple;
    intermediate combinations map to yellow and green.
    """
    if emotion > 0.7:
        # Very emotional – warm colours
        if activity > 0.6:
            return "red"
        return "orange"
    if emotion > 0.4:
        # Moderately emotional – mid colours
        if activity > 0.6:
            return "yellow"
        return "green"
    # Low emotional charge – cool colours
    if activity > 0.6:
        return "cyan"
    return "blue"


def entangle_brains(brain_neutral: QubitBrainState, brain_speaker: QubitBrainState, emotion: float) -> None:
    """Entangle the neutral brain with the speaker based on emotional intensity.

    We simply adjust the amplitudes of the neutral brain's qubits to
    reflect the strength of the emotional influence.  This is a
    heuristic update for demonstration purposes: amplitudes are scaled
    by (1 + emotion * 0.2) and then renormalised.  In a real model
    you might implement entanglement using tensor products and more
    sophisticated operations.
    """
    amps = brain_neutral.amplitudes.copy()
    amps *= (1.0 + emotion * 0.2)
    # Renormalise each qubit's state
    norms = np.linalg.norm(amps, axis=1, keepdims=True)
    amps = amps / norms
    brain_neutral.amplitudes = amps


def run_simulation(steps: int = 5) -> None:
    """Run a short simulation of two DITs entangling through emotion.

    The function prints the true and perceived internal states of the
    neutral agent at each step, along with the emotional intensity
    (randomly generated), the most active qubit probability and the
    resulting colour designation.  The speaker agent's state is
    currently unused except to illustrate how two brains might
    interact.
    """
    # Initialise two brains with two qubits each
    brain_neutral = QubitBrainState.init_random(num_qubits=2)
    brain_speaker = QubitBrainState.init_random(num_qubits=2)

    # Print header
    print("Simulating dual DIT entanglement with colour-coded activity")
    print("---------------------------------------------------------")
    for step in range(steps):
        # Generate an emotional intensity (0 to 1).  In a real system
        # this would come from a sentiment analysis of the LLM output.
        emotion = random.random()

        # Entangle the neutral brain with the speaker brain
        entangle_brains(brain_neutral, brain_speaker, emotion)

        # Measure the qubits of the neutral brain
        bits, probs = brain_neutral.measure()

        # Determine overall activity as the maximum probability
        activity_level = max(p[1] for p in probs)

        # Choose a colour based on activity and emotion
        colour = colour_from_activity(activity_level, emotion)

        # Build a simple perceived environment message
        perceived_env = {
            "description": "Agent hears emotionally charged words from another agent.",
            "emotion_intensity": round(emotion, 2),
            "activity_level": round(activity_level, 2),
            "colour": colour,
        }

        # Print the results for this step
        print(f"Step {step}:")
        print(f"  Emotion intensity: {emotion:.2f}")
        print(f"  Measured bits: {bits.tolist()}")
        print(f"  Probabilities: {[[round(p[0], 3), round(p[1], 3)] for p in probs]}")
        print(f"  Activity level: {activity_level:.2f}")
        print(f"  Colour: {colour}")
        print(f"  Perceived environment: {json.dumps(perceived_env)}")
        print()


if __name__ == "__main__":
    run_simulation(steps=6)