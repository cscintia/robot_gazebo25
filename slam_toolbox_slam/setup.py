from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'slam_toolbox_slam'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*launch.[pxy][yma]*')),
        (os.path.join('share', package_name, 'config'), glob('config/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Farraj007',
    maintainer_email='BarhamFarraj@icloud.com',
    description='TODO: Package description',
    license='GNU General Public License v3.0',
)
