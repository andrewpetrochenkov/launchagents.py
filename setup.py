import setuptools

setuptools.setup(
    name='launchagents',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
