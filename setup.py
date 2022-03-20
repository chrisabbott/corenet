import setuptools

setuptools.setup(
	name="corenet",
  version="0.0.1",
  author="Chris Abbott",
  description="chris.abbott.swe@gmail.com",
  url="https://github.com/chrisabbott/corenet",
  license="Apache",
  packages=["corenet"],
	install_requires=[
		"dataclasses-jsonschema==2.12.0",
		"google-cloud-storage==1.28.1",
		"json5==0.9.5",
		"jsonschema==3.2.0",
		"moderngl==5.6.0",
		"pandas==1.0.3",
		"Pillow==7.1.2",
		"ray==1.0.1",
		"scikit-image==0.17.2",
		"tensorboard==2.4.0",
		"tensorflow-gpu==2.3.1",
		"torch==1.7.0",
		"torchvision==0.8.1",
		"tqdm==4.46.1",
		"PyOpenGL==3.1.5",
		"jq==1.1.1",
		"h5py==2.10.0",
		"k3d==2.12.0"
	])
