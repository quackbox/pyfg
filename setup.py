import uuid

from setuptools import setup, find_packages
# Workaround to maintain backwards compatibility from https://github.com/napalm-automation-community/napalm-fortios/pull/66
try:
    from pip._internal.req import parse_requirements
except ImportError:
    from pip.req import parse_requirements

install_reqs = parse_requirements('requirements.txt', session=uuid.uuid1())

# Workaround for new parse_requirements generator attributes to maintain backwards compatibility
try:
    reqs = [str(ir.req) for ir in install_reqs]
except AttributeError:
    reqs = [str(ir.requirement) for ir in install_reqs]

setup(
    name="pyfg",
    version="0.50",
    packages=find_packages(),
    author="XNET",
    author_email="lindblom+pyfg@spotify.com",
    description="Python API for fortigate",
    url="https://github.com/spotify/pyfg",
    include_package_data=True,
    install_requires=reqs
)
