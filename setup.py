from setuptools import setup,find_packages
setup(name="censum-income",
      version="0.01",
      author="Naveen",
      author_email="naveen@test.com",
      packages=find_packages(),
      install_requires=["pandas","numpy","flask"]
      )