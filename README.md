# SJTDM TAZ Migration and Data Validation Project

## Purpose

The South Jersey Transportation Planning Organization (SJTPO) is transitioning the South Jersey Travel Demand Model (SJTDM) from its legacy Transportation Analysis Zone (TAZ) structure to a new TAZ system based on 2020 Census geography.

The purpose of this project is to document, inventory, trace, and validate the socioeconomic and transportation planning data used by the SJTDM during that transition.

The project focuses on preservation of model-relevant data rather than geometric similarity between TAZ boundaries.

## Project Objectives

1. Inventory all TAZ-related data sources used by the SJTDM.
2. Document data lineage from source datasets to model inputs.
3. Develop reproducible procedures for TAZ crosswalk development.
4. Validate the preservation and allocation of model inputs during migration to the new TAZ structure.
5. Create documentation sufficient to support future model updates, recalibration efforts, and consultant procurements.
6. Maintain compliance with SJTPO GIS Data Management and Documentation Standards.

## Scope

This effort includes:

* Legacy SJTDM TAZ documentation.
* 2010 Census geography relationships.
* 2020 Census geography relationships.
* TAZ crosswalk development.
* Socioeconomic data aggregation.
* Employment data aggregation.
* Recreational and special-generator data review.
* Model input validation.
* QA/QC reporting.

This effort does not include:

* Model recalibration.
* Model validation against traffic counts.
* Travel forecasting.
* Network coding updates.

## Key Deliverables

### Data Inventory

Comprehensive inventory of:

* Cube Voyager inputs
* GIS layers
* Census datasets
* Employment datasets
* Supporting databases and spreadsheets

### Data Dictionary

Documentation of:

* Tables
* Fields
* Data types
* Source systems
* Model usage

### Crosswalk Documentation

Documentation of:

* 2011 TAZ to Census relationships
* Census geography transitions
* New TAZ assignments
* Split and merge conditions

### QA/QC Reports

Validation of:

* Population
* Households
* Employment
* School enrollment
* Special generators
* Recreational data
* Area type assignments

### Final Technical Memorandum

Documentation of methodology, findings, limitations, and recommendations.

## Repository Structure

/docs

Project documentation, standards, reports, and technical memoranda.

/data/raw

Original source datasets. Read-only.

/data/intermediate

Working datasets and processing outputs.

/data/final

Validated project deliverables.

/scripts

Python scripts and automation tools.

/gis

GIS layers, maps, symbology, and project files.

/metadata

Metadata records and supporting documentation.

/outputs

Reports, tables, maps, and exported products.

## Methodology Principles

The project evaluates transportation planning data content rather than geometric similarity alone.

Geometry-based measures such as area change and centroid movement may be used as supporting diagnostics but are not considered primary validation metrics.

Primary validation metrics include:

* Population preservation
* Household preservation
* Employment preservation
* Special generator preservation
* Area type consistency
* External station consistency
* Recreational trip generator preservation

## Software Environment

Primary software includes:

* Cube Voyager
* ArcGIS Pro
* Microsoft Access
* Microsoft Excel
* Python 3.x
* Visual Studio Code
* Git and GitHub

## Project Lead

Kent Schellinger

Technical Support Specialist

South Jersey Transportation Planning Organization (SJTPO)

## Status

Project initiated June 2026.
Current phase: Data Inventory and System Documentation.
