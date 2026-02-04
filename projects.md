---
layout: single
permalink: /projects/
title: "Technical Projects"
author_profile: true
toc: true
toc_label: "Projects"
---

## 1. Aerial Physical Interaction ("The Tactile Drone")
**Role:** Lead Researcher | **Stack:** C++, Embedded Linux, Lyapunov Control

*   **Objective:** Enable a quadrotor to maintain stable contact with a ceiling for **non-destructive testing (ultrasound inspection)**.
*   **Innovation:** Developed a **Virtual Force-Position Controller** utilizing the Orthogonalization Principle. This allows the drone to move along a ceiling (rolling contact) while exerting a precise force of 5N.
*   **Tech Details:** 
    *   Modeled the "Non-holonomic Pffafian constraint" for rolling contact.[1]
    *   Implemented a model-free chatterless sliding mode controller for asymptotic stability.
    *   Validated on a custom quadrotor with a spherical end-effector.

## 2. Energy-Efficient Flight via RL
**Role:** Algorithm Engineer | **Stack:** Python, PyTorch, C++

*   **Objective:** Extend operational flight time for autonomous missions.
*   **Solution:** Replaced standard PID loops with an **Actor-Critic Reinforcement Learning** agent trained to minimize energy expenditure.
*   **Outcome:** Measurable reduction in battery consumption during station-keeping tasks; deployed on embedded hardware using multi-threading.

## 3. Cooperative Heterogeneous Fleets
**Role:** Systems Architect (PhD Thesis) | **Stack:** Sliding mode control, ROS, Distributed Systems

*   **Objective:** Coordinate ground robots (UGVs) and aerial robots (UAVs) for search-and-rescue.
*   **Solution:** Developing a **Constrained Model Framework** using sliding mode control. This allows diverse agents to subscribe to shared tasks without collision or deadlock.
