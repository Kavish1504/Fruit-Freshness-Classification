import os
import json
import joblib
import base64
import yaml
from pathlib import Path
from typing import Any

from box.exceptions import BoxValueError
from ensure import ensure_annotations
from box import ConfigBox


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    from src.cnnClassifier import logger
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml {yaml_file} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    from src.cnnClassifier import logger
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    from src.cnnClassifier import logger
    with open(path) as f:
        content = json.load(f)
    logger.info(f"json file loaded successfully from: {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    from src.cnnClassifier import logger
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    from src.cnnClassifier import logger
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data


@ensure_annotations
def get_size(path: Path) -> str:
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~ {size_in_kb} KB"


def decodeImage(imgstring, filename):
    imgdata = base64.b64decode(imgstring)
    with open(filename, "wb") as f:
        f.write(imgdata)


def encodeImageIntoBase64(croppedImage):
    with open(croppedImage, "rb") as f:
        return base64.b64encode(f.read())
