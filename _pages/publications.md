---
layout: single
permalink: /publications/
title: "Publications"
author_profile: true
---

My research outputs are indexed on(https://scholar.google.com/citations?user=qwpVD6cAAAAJ), [IEEE Xplore](https://ieeexplore.ieee.org/author/883716826371599), and(https://orcid.org/0009-0009-4185-9405).

### Selected Highlights

*   **S. E. Urzúa**, et al. "3D Force Control of a Quadrotor subject to 2D Non-holonomic Contact with an Spherical Tip." *IEEE International Conference on Cyborg and Bionic Systems (CBS)*, 2023. [View on IEEE](https://ieeexplore.ieee.org/document/10332838)
*   **S. E. Urzúa**, et al. "Reinforcement Learning Based Control for Energy Efficiency in Aerial Vehicles." (Under Review).

### Full List (Auto-Synced from ORCID)

{% if site.data.orcid_pubs %}
  <ul>
  {% for pub in site.data.orcid_pubs %}
    <li>
      <strong>{{ pub.title }}</strong><br>
      <em>{{ pub.journal }}</em> ({{ pub.year }})<br>
      <a href="{{ pub.url }}">View Paper</a>
    </li>
  {% endfor %}
  </ul>
{% else %}
  <p><em>Connecting to ORCID... (Data will appear after the first automated workflow run).</em></p>
{% endif %}

