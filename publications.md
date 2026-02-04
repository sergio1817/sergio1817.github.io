---
layout: single
permalink: /publications/
title: "Publications"
author_profile: true
---

<!-- My research outputs are indexed on [Google Scholar](https://scholar.google.com/citations?user=qwpVD6cAAAAJ), [IEEE Xplore](https://ieeexplore.ieee.org/author/883716826371599), and [HAL](https://cv.hal.science/sergiourzua). -->

### Selected Highlights
*   **S. E. Urzúa**, et al. "3D Force Control of a Quadrotor subject to 2D Non-holonomic Contact with an Spherical Tip." *20th International Conference on Electrical Engineering, Computing Science and Automatic Control, CCE*, 2023. [View on IEEE](https://ieeexplore.ieee.org/document/10332838)
<!-- *   **S. E. Urzúa**, et al. "Reinforcement Learning Based Control for Energy Efficiency in Aerial Vehicles." (Under Review). -->

<hr>

### Full List (Auto-Synced from ORCID)
<!-- *This list updates automatically via GitHub Actions.* -->

{% if site.data.publications %}
{% assign sorted_pubs = site.data.publications | sort: "year" | reverse %}
{% assign pubs_by_year = sorted_pubs | group_by: "year" %}
{% for group in pubs_by_year %}
<h4>{{ group.name }}</h4>
<ul>
{% for pub in group.items %}
  <li>
    <strong>{{ pub.title }}</strong><br>
    <em>{{ pub.journal }}</em><br>
    {% if pub.url != "" %}<a href="{{ pub.url }}">View Paper</a>{% endif %}
  </li>
{% endfor %}
</ul>
{% endfor %}
{% else %}
<p><em>Loading publications from ORCID... (Wait for the 'Update Publications' workflow to run).</em></p>
{% endif %}
