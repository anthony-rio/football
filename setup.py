from setuptools import setup, find_packages

setup(
    name="football",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "supervision",
        "opencv-python",
        "numpy"
    ],
    author="anthony-rio",
    description="Football field analysis and visualization tools",
    python_requires=">=3.7",
    include_package_data=True,
    zip_safe=False
)
