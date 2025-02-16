from setuptools import setup, find_packages

setup(
    name='MultiTaskProcessor',
    version='1.0.1',
    author='Hui Liu',
    license='MIT',
    author_email='23122842@qq.com',
    description='when you have a lot of tasks to process, you can use this package to process them in parallel.',
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',  #if not note number, can not be installed
    ],
)