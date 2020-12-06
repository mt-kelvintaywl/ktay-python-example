# ktay python example

Test / sample Python package setup.

## Examples of Different Setups & Installs from Github

```

# Installing the main (master) branch...

pip install -e git+git://github.com/mt-kelvintaywl/ktay_python_example.git#egg=ktay_python_example

# Installing from a specific branch...
# In this example, we have additional code added in the feat branch.

pip install -e git+git://github.com/mt-kelvintaywl/ktay_python_example.git@feat#egg=ktay_python_example

# What if the python installable (package) is in a subfolder in our GitHub repo?
# In this case, we've moved the setup.py file and codes to a `./subfolder` folder in subfolder branch.

pip install -e "git+git://github.com/mt-kelvintaywl/ktay_python_example.git@subfolder#egg=ktay_python_example&subdirectory=subfolder"

# What if this python package is a private Github repo?
pip install -e "git+https://$GITHUB_ACCESS_TOKEN:x-oauth-basic@github.com/mt-kelvintaywl/ktay-python-example.git@subfolder#egg=ktay_python_example&subdirectory=subfolder"
```
