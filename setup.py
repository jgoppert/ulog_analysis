from distutils.core import setup

import versioneer

setup(
    name='ulog_analysis',
    version=versioneer.get_version(),
    packages=['ulog_analysis'],
    requires=['pyulog', 'pandas'],
    url='github.com/jgoppert/ulog_analysis',
    license='BSD v3',
    author='James Goppert',
    author_email='james.goppert@gmail.com',
    description='Analysis for px4 autopilot flight log data in ulog format.',
    cmdclass=versioneer.get_cmdclass()
)
