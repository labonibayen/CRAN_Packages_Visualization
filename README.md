# About

An interactive visualization of major programming languages and their CRAN packages. This is a Flask app built on a Digital Ocean droplet and utilizes D3 for the network graph. See here for live version: http://167.71.178.218/concentricnetwork

<img width="703" alt="Screenshot 2023-10-10 at 1 39 46 AM" src="https://github.com/labonibayen/CRAN_Packages_Visualization/assets/26695981/29ee7ccb-d691-472d-9336-bcc62a93abeb">


This visualization is responsive to mouse hovers. When mousing over a node, the node doubles in size and all edges connected to that node are highlighted.

On mouseover, there are also tooltips that describe the CRAN package, or provide a brief description of the programming language.

<img width="703" alt="Screenshot 2023-10-10 at 1 39 56 AM" src="https://github.com/labonibayen/CRAN_Packages_Visualization/assets/26695981/c53e43f4-7e5a-4d3c-a8a7-46458f31e6bd">


# Notes

Data from the R for Data Science tidytuesday repo: https://github.com/rfordatascience/tidytuesday/blob/master/data/2019/2019-11-12/loc_cran_packages.csv

Inspired by the R visualistion: https://twitter.com/spren9er/status/1195826547724374018?lang=en

This is a massive data set, so the data for this visualization was proportionally shrunk. First, the data was limited by common programming langauges, then a proportional sample was taken from each bucket of languages (see clean_cran_data.py for details).









