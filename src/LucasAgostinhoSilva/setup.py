from setuptools import find_packages, setup

package_name = 'LucasAgostinhoSilva'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/primeiro_launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='root',
    maintainer_email='root@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'primeiro_binario = LucasAgostinhoSilva.primeiro_no:main',
            'segundo_binario = LucasAgostinhoSilva.segundo_no:main',
            'binario_no_classe = LucasAgostinhoSilva.no_com_classe:main',
        ],
    },
)
