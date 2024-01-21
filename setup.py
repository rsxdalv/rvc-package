import setuptools


setuptools.setup(
    name="rvc_pkg",
    packages=[
        "assets",
        "configs",
        "i18n",
        "lib",
        "tools",
        "infer",
    ],
    version="0.1.2",
    author="lj1995",
    description="An easy-to-use Voice Conversion framework based on VITS",
    url="https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI",
    project_urls={},
    scripts=[],
    include_package_data=True,
    install_requires=[
        "absl-py>=1.2.0",
        "audioread",
        "av",
        "colorama>=0.4.5",
        "Cython",
        "fairseq==0.12.2",
        "faiss-cpu==1.7.3",
        "ffmpeg-python>=0.2.0",
        "ffmpy==0.3.1",
        "fsspec>=2022.11.0",
        "httpx",
        "Jinja2>=3.1.2",
        "joblib>=1.1.0",
        "json5",
        "librosa==0.9.1",
        "llvmlite==0.39.0",
        "Markdown",
        "matplotlib-inline>=0.1.3",
        "matplotlib>=3.7.0",
        "numba==0.56.4",
        "numpy==1.23.5",
        "onnxruntime-gpu; sys_platform != 'darwin'",
        "onnxruntime; sys_platform == 'darwin'",
        "Pillow>=9.1.1",
        "praat-parselmouth>=0.4.2",
        "pyasn1-modules>=0.2.8",
        "pyasn1>=0.4.8",
        "pydub>=0.25.1",
        "python-dotenv>=1.0.0",
        "pyworld==0.3.2",
        "PyYAML>=6.0",
        "resampy>=0.4.2",
        "scikit-learn",
        "scipy",
        "soundfile>=0.12.1",
        "sympy>=1.11.1",
        "tabulate>=0.8.10",
        "tensorboard",
        "tensorboardX",
        "torchcrepe>=0.0.20",
        "torchfcpe",
        "tornado>=6.1",
        "tqdm>=4.63.1",
        "uc-micro-py>=1.0.1",
        "uvicorn>=0.21.1",
        "Werkzeug>=2.2.3",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
