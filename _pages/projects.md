---
permalink: /projects/
title: "Technical Projects"
author_profile: true
---

## 1. Aerial Physical Interaction (The "Tactile Drone")
**Objective:** Enable a quadrotor to maintain stable contact with a ceiling for non-destructive testing (ultrasound inspection).

*   **The Challenge:** Standard drones crash upon contact. The system needed to exert precisely 5N of force while moving.
*   **The Solution:** Developed a **Virtual Force-Position Controller** utilizing the Orthogonalization Principle to decouple force and motion dynamics.
*   **Implementation:** 
    *   **Algorithm:** Model-free chatterless sliding mode control.
    *   **Hardware:** Custom quadrotor with a spherical end-effector.
    *   **Stack:** C++ implementation on Embedded Linux.
*   **Outcome:** Validated stable "rolling contact" capabilities in real-world experiments.
*   *Reference: IEEE Conference Publication 2023*

## 2. Energy-Efficient Flight via Reinforcement Learning
**Objective:** Extend the operational flight time of autonomous drones.

*   **The Solution:** Replaced standard PID loops with an **Actor-Critic Reinforcement Learning** agent trained to minimize energy expenditure.
*   **Implementation:**
    *   **Training:** Python (PyTorch) simulation environment.
    *   **Deployment:** Optimized C++ inference engine running on onboard hardware.
    *   **Tech:** Multi-thread programming for real-time performance.
*   **Outcome:** Measurable reduction in battery consumption during station-keeping tasks.

## 3. Cooperative Heterogeneous Fleets
**Objective:** Coordinate ground robots (UGVs) and aerial robots (UAVs) for search-and-rescue.

*   **The Solution:** Designed a constrained model framework allowing diverse agents to share tasks without collision.
*   **Implementation:** Nonlinear Model Predictive Control (NMPC) and distributed consensus algorithms.

