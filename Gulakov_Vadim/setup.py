import setuptools
requirements = [
    'jinja2',
    'bs4',
]
# with open("requirements.txt") as f:
#     requirements = f.read()

with open("README.md") as file:
    read_me_description = file.read()

setuptools.setup(
    name="rss-news",
    version="4.0",
    author="Vadim Gulakov",
    author_email="gulakovvadim2@gmail.com",
    description="RSS-newses parser CLI utility.",
    long_description=read_me_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vdmglkv/Homework",
    install_requires=requirements,
    include_package_data=True,
    packages=setuptools.find_packages(),
    scripts=['RP/converter.py',
             'RP/console_args.py',
             'RP/db.py',
             'RP/templates/base.html',
             'RP/templates/DejaVuSans.ttf'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': ['rss_parser=RP.rss_parser:main'],
    },
    python_requires='>=3.9',
)
