# .travis.yml
config = """
    language: python
    python:
        - '2.7'
        - '2.7.13'
        - '3.6.1'
        - '3.7'
        - 'pypy'
        - 'pypy3'
    
    install:
        pip install -r requirements.txt

    script: pytest

"""
