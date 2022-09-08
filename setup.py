from setuptools import setup

setup(name='redlooper_app_app',
      version='0.1',
      description='Raspberry Pi Looper Pedal',
      author='Basil',
      author_email='basil.huber@gmail.com',
      packages=['redlooper_app', 'redlooper_app.gui'],
      install_requires=['pygame', 'cython', 'pyliblo', 'JACK-Client', 'RPi.GPIO'],
      entry_points={'console_scripts': ['redlooper_app=redlooper_app.main:main']},
      zip_safe=False)
