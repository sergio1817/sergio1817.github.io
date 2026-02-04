---
layout: single
permalink: /projects/
title: "Technical Projects"
author_profile: true
toc: true
toc_label: "Project List"
---

## 1. Aerial Physical Interaction (The "Tactile Drone")
**Role:** Lead Researcher & Developer | **Stack:** C++, Embedded Linux, Lyapunov Control

*   **The Problem:** Standard drones are visual observers that crash upon contact. Infrastructure inspection (NDT) requires drones to exert stable force against surfaces.
*   **The Innovation:** Developed a **Virtual Force-Position Controller** based on the Orthogonalization Principle. This allows the drone to move along a ceiling (rolling contact) while exerting a precise force of 5N.
*   **Technical Detail:** 
    *    Modeled the "Non-holonomic Pffafian constraint" for the rolling contact.
    *   Implemented a model-free chatterless sliding mode controller to ensure asymptotic stability.
    *   Validated on a custom quadrotor with a spherical end-effector.[1]

## 2. Energy-Efficient Flight via Reinforcement Learning
**Role:** Algorithm Engineer | **Stack:** Python, PyTorch, C++

*   **The Problem:** Traditional PID controllers are robust but energy-inefficient, limiting mission time.
*   **The Solution:** Replaced standard PID loops with an **Actor-Critic Reinforcement Learning (RL)** agent.
*   **Outcome:** The RL agent optimized the attitude control policy to minimize battery consumption while maintaining tracking accuracy, validated in simulation and hardware-in-the-loop tests.

## 3. Cooperative Heterogeneous Fleets
**Role:** Systems Architect (PhD Thesis) | **Stack:** NMPC, ROS, Distributed Systems

*   **The Problem:** Coordinating ground robots (UGVs) and aerial robots (UAVs) that have different dynamics and constraints.
*   **The Solution:** Developing a **Constrained Model Framework** using Nonlinear Model Predictive Control (NMPC). This allows diverse agents to subscribe to shared tasks without collision or deadlock in complex environments.
