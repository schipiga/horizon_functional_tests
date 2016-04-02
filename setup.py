from setuptools import setup


requires = [
    "selenium",
    "pyhamcrest",
    "pytest",
    "testtools",
    "nose"
]


if __name__ == '__main__':
    setup(
        name='horizon-functional-tests',
        version='0.1a',
        author="Sergei Chipiga",
        author_email="chipiga86@gmail.com",
        packages=["horizon"],
        install_requires=requires)
