from setuptools import setup

setup(
    name='httpie-tokli',
    description='Tokli OAuth 2 plugin for HTTPie.',
    version='0.1',
    license='MIT',
    url='https://github.com/gnicod/httpie-tokli',
    py_modules=['httpie_tokli'],
    zip_safe=False,
    entry_points={
        'httpie.plugins.auth.v1': [
            'httpie_tokli = httpie_tokli:TokliPlugin'
        ]
    },
    install_requires=[
        'httpie>=0.7.0',
        'tokli'
    ]
)
