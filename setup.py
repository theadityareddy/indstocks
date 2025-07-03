from setuptools import setup, find_packages

# Package Metadata
PACKAGE_NAME = "indstocks"
VERSION = "1.1.1"
DESCRIPTION = "Access to Indian Stock Market insights via Python package."
AUTHOR = "Aditya Reddy & Kshitij Mahale"
AUTHOR_EMAIL = "adityareddy.biz@gmail.com, kshitijmahale02@gmail.com"
GITHUB_URL = "https://github.com/theadityareddy/indstocks"

# Long description from README.md with fallback
try:
    with open("README.md", "r", encoding="utf-8") as fh:
        LONG_DESCRIPTION = fh.read()
except FileNotFoundError:
    LONG_DESCRIPTION = (
        "INDStocks is a Python package designed to fetch, parse, and present "
        "key data from the Indian stock markets. Built for researchers, developers, "
        "and hobbyist investors, it simplifies the retrieval of market data using "
        "modern scraping tools. Note: This package is intended solely for educational "
        "and non-commercial use."
    )

# Setup function
setup(
    name=PACKAGE_NAME, 
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url=GITHUB_URL,
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'indstocks.scrapers': ['links.json'],
    },
    install_requires=[
        "beautifulsoup4",
        "bs4",
        "requests",
        "selenium"
    ],
    extras_require={
        "dev" : ["pytest>7.0", "twine>4.0.2"]
    },
    python_requires='>=3.10',
    keywords=["python", "india", "nse", "bse", "stock market", "indian", "data scraper"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Financial and Insurance Industry",
        "License :: OSI Approved :: MIT License",
        "Topic :: Office/Business :: Financial",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    license="MIT",
)
