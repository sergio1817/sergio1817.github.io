---
layout: single
permalink: /projects/
title: "Technical Projects"
author_profile: true
toc: true
toc_label: "Projects"
---

## 1. Aerial Physical Interaction (The "Tactile Drone")
<!-- ![Tactile Drone project preview](/assets/images/project-1.svg) -->
**Role:** Lead Researcher | **Stack:** C++, Embedded Linux, Sliding Mode Control

*   **Objective:** Enable a quadrotor to maintain stable contact with a ceiling for **non-destructive testing (ultrasound inspection)**.
*   **Innovation:** Developed a **Virtual Force-Position Controller** utilizing the Orthogonalization Principle. This allows the drone to move along a ceiling (rolling contact) while exerting a precise force of 5N.
*   **Technical Detail:** 
    *   Modeled the "Non-holonomic Pffafian constraint" for rolling contact.
    *   Implemented a model-free chatterless sliding mode controller for asymptotic stability.
    *   Validated on a custom quadrotor with a spherical end-effector.
<!-- *   **Links:** [IEEE Paper](https://ieeexplore.ieee.org/document/10332838) | [Project Notes](https://github.com/sergio1817) -->

## 2. Energy-Efficient Flight via Reinforcement Learning
<!-- ![Energy-efficient flight preview](/assets/images/project-2.svg) -->
**Role:** Algorithm Engineer | **Stack:** MATLAB/Simulink, C++

*   **Objective:** Extend operational flight time for autonomous missions.
*   **Solution:** Replaced standard PID loops with an **Actor-Critic Reinforcement Learning** agent trained to minimize energy expenditure.
*   **Outcome:** Measurable reduction in battery consumption during station-keeping tasks; deployed on embedded hardware using multi-threading.
<!-- *   **Links:** [Code Repository](https://github.com/sergio1817) -->

## 3. Cooperative Heterogeneous Fleets (PhD Thesis)
<!-- ![Heterogeneous fleets preview](/assets/images/project-3.svg) -->
**Role:** Systems Architect | **Stack:** Sliding mode control, ROS, Distributed Systems

*   **Objective:** Coordinate ground robots (UGVs) and aerial robots (UAVs) for complex tasks.
*   **Solution:** Developing a **Constrained Model Framework** using Sliding Mode control. This allows diverse agents to subscribe to shared tasks without collision or deadlock.
<!-- *   **Links:** [Thesis Outline](https://github.com/sergio1817) -->
