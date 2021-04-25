from setuptools import find_packages, setup

print("hello from setup.py")

setup(
    name="gb_chat",
    description="GB chat",
    version="0.0.1",
    install_requires=["click>=7.0,<8.0", "PyQt5>=5.0,<6.0", "SQLAlchemy>=1.2,<2.0"],
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "start_client=chat.start_client:start",
            "start_server=chat.start_server:start",
        ]
    },
)
