"""
_mypy_ needs to look for package root.
Normally this is /app, but we're running it outside of /src/app.
Therefore it needs to traverse through /src as well and we need to place this __init__.py file here.
Otherwise the lookup will throw an error like: Can't find package 'src.app'
"""
