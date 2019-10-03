import os
import setuptools

module_name = 'docxreplace'

here = os.path.abspath(os.path.dirname(__file__))

about = {}
with open(os.path.join(here, module_name, '__version__.py')) as handle:
    exec(handle.read(), about)

setuptools.setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__description__'],
    author=about['__author__'],
    packages=setuptools.find_packages(),
    install_requires=[
        'docopt>=0.6.2',
        'python-docx>=0.8.10'
    ],
    entry_points={
        'console_scripts': [
            '{0} = {0}.cli:cli'.format(module_name)
        ],
    },
    python_requires='>=3.5'
)
