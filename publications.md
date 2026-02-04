---
layout: single
permalink: /publications/
title: "Publications"
author_profile: true
---

My research outputs are indexed on [Google Scholar](https://scholar.google.com/citations?user=qwpVD6cAAAAJ), [IEEE Xplore](https://ieeexplore.ieee.org/author/883716826371599), and [HAL](https://cv.hal.science/sergiourzua).

### Selected Highlights
*   **S. E. Urzúa**, et al. "3D Force Control of a Quadrotor subject to 2D Non-holonomic Contact with an Spherical Tip." *IEEE International Conference on Cyborg and Bionic Systems (CBS)*, 2023. [View on IEEE](https://ieeexplore.ieee.org/document/10332838)
*   **S. E. Urzúa**, et al. "Reinforcement Learning Based Control for Energy Efficiency in Aerial Vehicles." (Under Review).

<hr>

### Full List (Auto-Synced from ORCID)
*This list is automatically updated via GitHub Actions.*

{% if site.data.publications %}
  <ul>
  {% for pub in site.data.publications %}
    <li>
      <strong>{{ pub.title }}</strong> ({{ pub.year }})<br>
      <em>{{ pub.journal }}</em><br>
      {% if pub.url!= "" %}<a href="{{ pub.url }}">View Paper</a>{% endif %}
    </li>
  {% endfor %}
  </ul>
{% else %}
  <p><em>Connecting to ORCID... (Data will appear after the first automated workflow run).</em></p>
{% endif %}
