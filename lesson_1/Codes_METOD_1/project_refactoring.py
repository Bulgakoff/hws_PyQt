class MessageSplitter:
    def __init__(self, deserializer) -> None:
        self._deserializer = deserializer

    def feed(self, data) -> None:
        ...
        self._deserializer.on_msg(msg_data)


class Deserializer:
    def __init__(self, msg_factory) -> None:
        self._msg_factory = msg_factory

    def on_msg(self, msg_data) -> None:
        ...
        self._msg_factory.on_msg(msg_dict)
