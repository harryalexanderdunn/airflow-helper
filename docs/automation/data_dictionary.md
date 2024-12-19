# Automating Data Dictionary creation and maintenance

Nobody wants to spend all their time writing documentation, so lets make some code to do it for you. I have written a script which takes tables from any bigquery dataset (that you have access to) and generates a data dictionary for each table in the dataset within a single md file. If you display this in a centralised site such as Mkdocs you can then split your data dictionaries by dataset and they are all easily searchable through the search bar on Mkdocs. This makes looking at data very powerful as its easy to search for certain key words over many different projects.

Please see my previous [article](../Documentation%20Series/central_docs_methodology.md) for more information on setting up a centralised documentation site.

## How it works

This is specifically for extracting data information out of bigquery and displaying it as a data dictionary within a central documentation site.

1. **You need to ensure your columns descriptions are labelled appropriately**. See here for information on how to do this within dataform: [Centralising & Automating Dataform Column Descriptions](https://medium.com/@harryalexdunn/centralising-automating-gcp-dataform-column-descriptions-3fec5d4734d0).
2. You need to have access to the appropriate tables and access to the metadata tables: "INFORMATION_SCHEMA.COLUMN_FIELD_PATHS"
3. If your table schemas or descriptions change you will need to rerun this code and push to the repo.
4. Have pandas & google-cloud-bigquery installed to use the libraries

## The Code

::: automation.data_dictionary
