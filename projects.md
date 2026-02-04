---
layout: single
permalink: /projects/
title: "Technical Projects"
author_profile: true
toc: true
toc_label: "Projects"
---

## 1. Aerial Physical Interaction
<!-- ![Tactile Drone project preview](/assets/images/project-1.svg) -->
**Role:** Lead Researcher | **Stack:** C++, Embedded Linux, Sliding Mode Control

*   **Objective:** Enable a quadrotor to maintain stable contact with a ceiling for **non-destructive testing (ultrasound inspection)**.
*   **Innovation:** Developed a **Virtual Force-Position Controller** utilizing the Orthogonalization Principle. This allows the drone to move along a ceiling (rolling contact) while exerting a precise force on the normal direction.
*   **Technical Detail:** 
    *   Modeled the "Non-holonomic Pffafian constraint" for rolling contact.
    *   Implemented a model-free chatterless sliding mode controller for asymptotic stability.
    <!-- *   Validated on a custom quadrotor with a spherical end-effector. -->
*   **Links:** [Paper](https://ieeexplore.ieee.org/document/10332838) 
<!-- | [Project Notes](https://github.com/sergio1817) -->

## 2. Energy-Efficient Flight via Reinforcement Learning
<!-- ![Energy-efficient flight preview](/assets/images/project-2.svg) -->
**Role:** Algorithm Engineer | **Stack:** MATLAB/Simulink, C++

*   **Objective:** Extend operational flight time for autonomous missions.
*   **Solution:** Implemented a self-tuning sliding mode controller with an **Actor-Critic Reinforcement Learning** at real-time.
*   **Outcome:** Measurable reduction in battery consumption during regulation and tracking tasks; deployed on embedded hardware using multi-threading.
*   **Links:** [Paper](https://doi.org/10.1109/cce60043.2023.10332878) 
<!-- *   **Links:** [Code Repository](https://github.com/sergio1817) -->

## 3. Cooperative Heterogeneous Interaction (PhD Thesis)
<!-- ![Heterogeneous fleets preview](/assets/images/project-3.svg) -->
**Role:** Lead Researcher | **Stack:** Sliding mode control, heterogenous robots

*   **Objective:** Coordinate ground robots (UGVs) and aerial robots (UAVs) for complex tasks.
*   **Solution:** Developing a cooperative and constrained model and using Sliding Mode control.
<!-- *   **Links:** [Thesis Outline](https://github.com/sergio1817) -->
