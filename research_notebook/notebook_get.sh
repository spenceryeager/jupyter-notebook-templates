#!/bin/bash

# Downloading the notebook

curl -O https://raw.githubusercontent.com/spenceryeager/jupyter-notebook-templates/master/research_notebook/MonthYear_Yeager_ResearchNotebook.ipynb

# Setting file name to the month and year for consistency

mv MonthYear_Yeager_ResearchNotebook.ipynb  $(date +%m%b%Y)"_Yeager_ResearchNotebook.ipynb"
