from setuptools import setup

import {{ cookiecutter.package_name }}

setup(
    name="{{ cookiecutter.project_name }}",
    version="{{ cookiecutter.version }}",
    description="{{ cookiecutter.project_short_description }}",
    long_description="{{ cookiecutter.project_long_description }}",
    keywords="django",
    author="{{ cookiecutter.author_special }}",
    author_email="{{ cookiecutter.email }}",
    url="https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}",
    license="{{ cookiecutter.open_source_license }}",
    packages=["{{ cookiecutter.package_name }}"],
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Environment :: Web Environment",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Framework :: Django",
        "Framework :: Django :: 1.8",
    ],
)
