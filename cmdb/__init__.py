# CMDB module

# Models and logic for configuration items

class ConfigurationItem:
    def __init__(self, name, type, status, relationships=None):
        self.name = name
        self.type = type
        self.status = status
        self.relationships = relationships or []

    def add_relationship(self, other_item):
        self.relationships.append(other_item)
