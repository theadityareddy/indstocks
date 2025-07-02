from setuptools import setup, find_packages

# Package Metadata
PACKAGE_NAME = "indstocks"
VERSION = "1.0.0"
DESCRIPTION = "Comprehensive access to Indian stock market insights via Python."
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
        'indstocks': ['scrapers/links.json'],  # Make sure this path is correct
    },
    install_requires=[
        "beautifulsoup4",
        "bs4",
        "requests",
        "selenium"
    ],
    python_requires='>=3.7',
    keywords=["python", "finance", "stock market", "india", "data scraper"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Financial and Insurance Industry",
        "Topic :: Software Development :: Libraries",
        "Topic :: Office/Business :: Financial :: Investment",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    license="MIT",
)
