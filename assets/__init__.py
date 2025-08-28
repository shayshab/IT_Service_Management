# Asset Inventory module

# Models and logic for asset management

class Asset:
    def __init__(self, asset_id, name, owner, lifecycle_status):
        self.asset_id = asset_id
        self.name = name
        self.owner = owner
        self.lifecycle_status = lifecycle_status
