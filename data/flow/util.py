import os
import pendulum
from slugify import slugify

import prefect
from prefect.engine.serializers import Serializer

RAW_DIR = "local/01-raw/en"
PROCESSED_DIR = "local/02-processed/en"
CLEAN_DIR = "local/03-clean/en"

logger = prefect.context.get("logger")


def format_dir(suffix: str) -> str:
    return os.path.join(os.path.dirname(__file__), "..", RAW_DIR, suffix)


def format_loc(task_name: str, **kwargs) -> str:
    ts = slugify(pendulum.now("utc").isoformat())
    filename = f"{task_name}_{ts}.dat"
    filepath = os.path.join(os.path.dirname(__file__), "..", PROCESSED_DIR, filename)
    logger.info(f"Writing {filepath}")
    return filepath


class ReadableListSerializer(Serializer):
    def deserialize(self, value: bytes) -> list:
        return value.decode().split("\n")

    def serialize(self, value: list) -> bytes:
        return "\n".join(value).encode()


class ReadableDictSerializer(Serializer):
    def deserialize(self, value: bytes) -> dict:
        return dict(wc.split(",") for wc in value.decode().split("\n"))

    def serialize(self, value: dict) -> bytes:
        return "\n".join((f"{w},{c}" for w, c in value.items())).encode()
