from setuptools import find_packages, setup

setup(
	name="corenet",
	version="0.0.1",
	author="Chris Abbott",
	description="chris.abbott.swe@gmail.com",
	url="https://github.com/chrisabbott/corenet",
	license="Apache",
	packages=find_packages(),
	install_requires=[
		"dataclasses==0.6",
		"dataclasses-jsonschema==2.15.0",
		"google-cloud-storage==2.2.1",
		"json5==0.9.6",
		"jsonschema==4.4.0",
		"moderngl==5.6.4",
		"pandas==1.3.5",
		"Pillow==9.0.1",
		"ray==1.11.0",
		"scikit-image==0.19.2",
		"tensorboard==2.8.0",
		"tensorflow-gpu==2.8.0",
		"torch==1.11.0",
		"torchvision==0.12.0",
		"tqdm==4.63.0",
		"PyOpenGL==3.1.6",
		"jq==1.2.2",
		"h5py==3.6.0",
		"k3d==2.12.0"
	])
