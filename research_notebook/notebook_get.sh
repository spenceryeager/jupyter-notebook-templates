#!/bin/bash

# Downloading the notebook

#curl -O https://raw.githubusercontent.com/spenceryeager/jupyter-notebook-templates/master/research_notebook/MonthYear_Yeager_ReasearchNotebook.ipynb

# Setting file name to the month and year for consistency

printf $(date +%b%Y)
