from setuptools import setup

setup(
    name='dynamo-mypy',
    version='0.0.1',
    description='remove annotations',
    author='Alexander Ivanov',
    author_email='alehander42@gmail.com',
    url='https://github.com/alehander42/dynamo',
    download_url='https://github.com/alehander42/dynamo/archive/v0.0.1.tar.gz',
    keywords=['mypy', 'annotation'],
    packages=['dynamo'],
    license='MIT',
    install_requires=[
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        'console_scripts': [
            'dynamo=dynamo.main:main',
        ],
    },
)
