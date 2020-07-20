import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

requires = [
    'psutil>=5',
    'selenium>=3',
    'urllib3>=1.25',
]

setuptools.setup(
    name="faceit_friends",  # Replace with your own username
    version="1.0.1",
    author="Pavel Borshchevsky",
    author_email="3410914@gmail.com",
    description="Scraps friend's friends from Faceit.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PavelBorsh/faceit_friends",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=requires,
)
