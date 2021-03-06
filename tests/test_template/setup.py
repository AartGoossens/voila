import os
from setuptools import setup


data_files = []
for (dirpath, dirnames, filenames) in os.walk('share/jupyter/voila/templates/'):
    if filenames:
        data_files.append((dirpath, [os.path.join(dirpath, filename) for filename in filenames]))


setup(
    name='test_template',
    version="0.0.1",
    description="Test template for voila",
    data_files=data_files,
    include_package_data=True,
    author='QuantStack',
    author_email='martin.renou@quantstack.net'
)
