from setuptools import find_packages, setup

package_name = 'interacao_humano_robo'

setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/meu_primeiro_launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Lucas Agostinho Silva',
    maintainer_email='lucasagostinhosilv@gmail.com',
    description='Pacote para aula interação humano robo',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'meu_primeiro_binario = interacao_humano_robo.meu_primeiro_no:main',
            'talker = interacao_humano_robo.primeiro_publisher:main',
            'listener = interacao_humano_robo.primeiro_subscriber:main',
            'r2s2 = interacao_humano_robo.r2d2:main',
        ],
    },
)
