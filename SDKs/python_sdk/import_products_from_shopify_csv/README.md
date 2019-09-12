# Import products from Shopify CSV file

This example demonstrates how to import a bulk of product from a CSV file.
It uses:
- The **[builton-sdk](https://pypi.org/project/builton-sdk/)**
- A **Service Account** Key (SA Key), you can find or create one through [BuiltOn](http://dashboard.builton.dev/) dashboard section **Settings**, sub-section **Service Account Keys**.
- A **BuiltOn API** Key, you can find or create one through [BuiltOn](http://dashboard.builton.dev/) dashboard section *Settings*, sub- section **API Keys**.

# Install Locally

In order to run this example locally, you need to:

1. In order to keep workspace, you can use a Virtual Environment

    1.1. Create a Virtual Environment: `python3 -m venv venv`
    
    Info: The name must start by *venv*

    1.2. Then active the virtual environment: `source ./venv_name/bin/activate`

2. Clone this repository, and run `pip install -r requirements.txt`

3. There are two ways to run the script: `import_products.py`

    3.1. Run the script and add the BuiltOn API Key and the SA Key  when it asks

    Run: `python import_products.py`

    3.2. Add and define the BuiltOn API Key and SA Key to a `settings.py` file. You can use the `setting_example.py` as a template

    Run: `python import_products skip_keys`
