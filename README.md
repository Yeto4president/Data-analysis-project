# Data-analysis-project

Use of PCA to analyze Ethiopia's animal protein production, GHG emissions, emission intensity, and supply from 2010-2020, revealing increased production and efficiency by 2020 and lower emissions in 2016.

## Project Overview

This project performs a Principal Component Analysis (PCA) on a dataset from Ethiopia (2010-2020) to explore relationships between animal protein production, GHG emissions, emission intensity, and supply. The analysis reveals increased production and efficiency by 2020, with 2016 as an outlier for lower emissions.

## Dataset

The dataset includes:


Total ASP Produced: Animal protein production (Mt/year)


GHG Emissions: Greenhouse gas emissions (Mt CO2e/year)


Emission Intensity: Emissions per kg of protein (kg CO2e/kg)


Total ASP Supply: Protein supply (kg/person/year)


Years: 2010, 2012, 2014, 2016, 2018, 2020

## Analysis

The analysis is conducted in a Jupyter Notebook (PCA_Analysis_Ethiopia.ipynb) with the following steps:


Data preparation and transposition


Basic statistical analysis (min, max, mean, std)


Data standardization (centered and reduced)


Correlation matrix calculation


PCA to reduce dimensionality (97.9% variance explained by first two axes)


Visualization (correlation circle, principal components plot)


Quality of representation (cos²) and year selection



## Results


Axe 1 (92.74%): Highlights increased animal protein production and supply from 2010-2012 to 2020, with reduced emission intensity, suggesting improved efficiency.


Axe 2 (5.24%): Identifies 2016 as an outlier with lower GHG emissions.


The analysis indicates potential sustainability efforts in Ethiopia's livestock industry despite increased resource pressure.



