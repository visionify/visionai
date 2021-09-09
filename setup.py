from setuptools import setup,find_packages

setup(name="visionai",
      version='0.0.1',
      description='Python based computer vision inference library that you can use in your production applications (supports NVIDIA Jetson platform & Intel platforms)',
      url="https://github.com/visionify/visionai",
      author='Harsh Murari',
      author_email='hmurari@visionify.ai',
      license='MIT',
      packages= find_packages(),
      install_requires=['opencv-python','scipy','pillow','matplotlib', 'h5py', 'requests'],
      zip_safe=False
      )
