import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="amazoncaptcha_api",
    version="0.0.2",
    author="Fedor Melekhin",
    author_email="fedormelexin@gmail.com",
    description="Simple anti-captcha compatable API (createTask/getTaskResult) to solve the Amazon's text captcha for free",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/melehin/amazoncaptcha-api",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'flask',
        'amazoncaptcha',
        'requests',
        'gunicorn',
    ],
    include_package_data=True,
    zip_safe=False
)