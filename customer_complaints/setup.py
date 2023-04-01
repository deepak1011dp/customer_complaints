from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in customer_complaints/__init__.py
from customer_complaints import __version__ as version

setup(
	name="customer_complaints",
	version=version,
	description="Customer Complaints of Items",
	author="Deepak Kumar",
	author_email="deepakkumar.it20@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
