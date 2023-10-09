# About

An interactive visualization of major programming languages and their CRAN packages. This is a Flask app built on a Digital Ocean droplet and utilizes D3 for the network graph. See here for live version: http://167.71.178.218/concentricnetwork

<img width="972" alt="Screenshot 2023-10-09 at 4 48 30 PM" src="https://github.com/labonibayen/flask_network_graph/assets/26695981/6e64dcdc-c69a-4833-9257-d64e8be67ae6">

This visualization is responsive to mouse hovers. When mousing over a node, the node doubles in size and all edges connected to that node are highlighted.

On mouseover, there are also tooltips that describe the CRAN package, or provide a brief description of the programming language.

<img width="972" alt="Screenshot 2023-10-09 at 5 03 47 PM" src="https://github.com/labonibayen/flask_network_graph/assets/26695981/b82f0ec8-b97c-42c1-9c78-92f20f052511">
<img width="972" alt="Screenshot 2023-10-09 at 5 03 19 PM" src="https://github.com/labonibayen/flask_network_graph/assets/26695981/02662019-b316-4cf9-ade4-b639d486b13a">

# Notes

Data from the R for Data Science tidytuesday repo: https://github.com/rfordatascience/tidytuesday/blob/master/data/2019/2019-11-12/loc_cran_packages.csv

Inspired by the R visualistion: https://twitter.com/spren9er/status/1195826547724374018?lang=en

This is a massive data set, so the data for this visualization was proportionally shrunk. First, the data was limited by common programming langauges, then a proportional sample was taken from each bucket of languages (see cran.py for details).









