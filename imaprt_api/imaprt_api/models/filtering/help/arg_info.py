class ArgInfo:
    def __init__(self, variable_name: str, variable_type: str, description: str):
        self._variable_name = variable_name
        self._variable_type = variable_type
        self._description = description

    def to_dict(self):
        return {
            "variableName": self._variable_name,
            "type": self._variable_type,
            "description": self._description
        }
