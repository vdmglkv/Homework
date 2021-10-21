import setuptools

with open("README.md") as file:
    read_me_description = file.read()

setuptools.setup(
    name="RP",
    version="2.0",
    author="Vadim Gulakov",
    author_email="gulakovvadim2@gmail.com",
    description="RSS-newses parser CLI utility.",
    long_description=read_me_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vdmglkv/Homework",
    packages=['RP'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)
