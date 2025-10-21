from setuptools import find_packages, setup

package_name = 'tugas_ros2_kelompok'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='gayubaruwa',
    maintainer_email='gayubaruwa@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    # --- PERBAIKAN DI SINI ---
    # 'extras_require' diganti menjadi 'tests_require'
    tests_require=['pytest'],
    # -----------------------
    entry_points={
        'console_scripts': [
            'keyboard_pub = tugas_ros2_kelompok.keyboard_publisher:main',
            'processor_sub = tugas_ros2_kelompok.processor_subscriber:main',
        ],
    },
)
