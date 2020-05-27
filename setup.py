from setuptools import setup

setup(name="Sigalog",
      version="0.4",
      description="Easy URL signing",
      url="https://github.com/MichaelJFlynn/Sigalog",
      author="Michael J. Flynn",
      packages=['Sigalog'],
      zip_safe=True,
      install_requires=["oscrypto>=1.2.0"]
  ) 
