import importlib.resources
import pendulum
from slugify import slugify

import prefect
from prefect.engine.serializers import Serializer

logger = prefect.context.get("logger")

LOCAL_BASE_PATH = importlib.resources.files("data.local")


def format_dir(suffix: str) -> str:
    return str(LOCAL_BASE_PATH.joinpath("raw/en", suffix))


def format_loc(task_name: str, **kwargs) -> str:
    ts = slugify(pendulum.now("utc").isoformat())
    filename = f"{task_name}_{ts}.dat"
    filepath = LOCAL_BASE_PATH.joinpath("processed/en", filename)
    return str(filepath)


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
