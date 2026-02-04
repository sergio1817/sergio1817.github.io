---
layout: single
permalink: /
title: "About Me"
author_profile: true
excerpt: "Robotics Engineer & PhD Researcher specializing in Aerial Systems."
---

I am a **Robotics Engineer and Junior Researcher** bridging the gap between advanced mathematical control theory and real-world embedded implementation. 

Currently, I am a PhD candidate in a **Cotutelle (Dual-Degree)** program between **Cinvestav (Mexico)** and **Heudiasyc - UTC (France)**. My research focuses on giving aerial systems the "sense of touch" through **Robust Force Control** and optimizing autonomy using **Reinforcement Learning**.

### Core Competencies

| Domain | Skills & Tools |
| :--- | :--- |
| **Robotics Control** | Robust Control, Force-Position Control, Sliding Mode, Lyapunov Stability |
| **Embedded Systems** | C++, Embedded Linux, Multi-threading, Pixhawk, ArduPilot |
| **AI & Learning** | Python (PyTorch), Reinforcement Learning (Actor-Critic) |
| **Mechanical Design** | SolidWorks (CSWP Certified), Rapid Prototyping |

### Current Research
At **Heudiasyc**, I am working on the **cooperative interaction of heterogeneous robots**, developing constrained model frameworks that allow drones and ground vehicles to collaborate in complex environments.

---

## About
I focus on robust control and embedded implementation for aerial robotics, with an emphasis on safe physical interaction and energy-aware autonomy.

## News
- **2026:** Continued work on cooperative aerial-ground interaction systems.
- **2025:** Presented force-control results at international conferences.

## Timeline
- **2024–Present:** PhD in Robotics (Cinvestav & Heudiasyc-UTC)
- **2021–2023:** MSc in Robotics (Cinvestav)
- **2016–2020:** BSc in Mechatronics Engineering (UAA)

## Download CV
[Download PDF CV](/assets/Sergio_U_CV.pdf){: .btn .btn--primary target="_blank"}

## Latest GitHub Activity
{% if site.data.github and site.data.github.size > 0 %}
<ul>
{% for repo in site.data.github %}
  <li>
    <strong><a href="{{ repo.url }}">{{ repo.name }}</a></strong>
    {% if repo.description %} — {{ repo.description }}{% endif %}
    {% if repo.language %} ({{ repo.language }}){% endif %}
  </li>
{% endfor %}
</ul>
{% else %}
<p><em>Run the GitHub activity script to load recent repositories.</em></p>
{% endif %}

## Contact
Email: [sergio.urzua@proton.me](mailto:sergio.urzua@proton.me)
