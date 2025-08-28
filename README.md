
# IT Service Management & Configuration Management Framework

This project implements comprehensive IT service management processes aligned with ITIL standards:
- Configuration Management Database (CMDB) design
- Asset inventory management
- Service mapping
- Automated monitoring and reporting for IT assets and configuration items

## Features
- **CMDB**: Track configuration items and their relationships
- **Asset Inventory**: Manage IT assets lifecycle and ownership
- **Service Mapping**: Visualize dependencies between services and assets
- **Monitoring & Reporting**: Automated status checks and reporting

## Project Structure
- `/cmdb/` — CMDB models and logic (`ConfigurationItem`)
- `/assets/` — Asset inventory management (`Asset`)
- `/service_mapping/` — Service mapping logic (`map_service_to_assets`)
- `/monitoring/` — Monitoring and reporting scripts (`generate_report`)
- `main.py` — Example usage and entry point

## Requirements
- Python 3.10+

## Getting Started
1. Clone the repository
2. (Optional) Create a virtual environment: `python3 -m venv venv && source venv/bin/activate`
3. Run the main script:
	```bash
	python main.py
	```

## Example Usage
The `main.py` file demonstrates how to use the modules:

```python
from cmdb import ConfigurationItem
from assets import Asset
from service_mapping import map_service_to_assets
from monitoring import generate_report

# Create configuration items and assets
ci1 = ConfigurationItem("Web Server", "Server", "Active")
ci2 = ConfigurationItem("Database", "DB", "Active")
ci1.add_relationship(ci2)

asset1 = Asset("A001", "Laptop", "Alice", "In Use")
asset2 = Asset("A002", "Router", "IT Dept", "Operational")

# Map service to assets
service_map = map_service_to_assets("Website Hosting", [asset1, asset2])

# Generate monitoring report
report = generate_report([asset1, asset2])

print("Service Mapping:", service_map)
print("Monitoring Report:", report)
```

## License
MIT
# IT_Service_Management
