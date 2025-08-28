"""
Main entry point for IT Service Management & Configuration Management Framework
"""
from cmdb import ConfigurationItem
from assets import Asset
from service_mapping import map_service_to_assets
from monitoring import generate_report


# --- Configuration Items (CMDB) ---
ci_web = ConfigurationItem("Web Server", "Server", "Active")
ci_db = ConfigurationItem("Database", "DB", "Active")
ci_app = ConfigurationItem("Application Server", "Server", "Maintenance")
ci_firewall = ConfigurationItem("Firewall", "Network", "Operational")
ci_db.add_relationship(ci_web)
ci_app.add_relationship(ci_db)
ci_firewall.add_relationship(ci_web)

# --- Assets ---
asset_laptop = Asset("A001", "Laptop", "Alice", "In Use")
asset_router = Asset("A002", "Router", "IT Dept", "Operational")
asset_switch = Asset("A003", "Switch", "IT Dept", "Operational")
asset_server = Asset("A004", "Server", "Bob", "Active")
asset_storage = Asset("A005", "Storage Array", "Infra Team", "Active")

# --- Service Mapping ---
services = [
	{"name": "Website Hosting", "assets": [asset_server, asset_router, asset_switch]},
	{"name": "Database Service", "assets": [asset_server, asset_storage]},
	{"name": "Internal Application", "assets": [asset_server, asset_laptop]},
	{"name": "Network Security", "assets": [asset_firewall := Asset("A006", "Firewall Appliance", "SecOps", "Operational")]}  # Inline asset
]

service_maps = [map_service_to_assets(s["name"], s["assets"]) for s in services]

# --- Monitoring & Reporting ---
all_assets = [asset_laptop, asset_router, asset_switch, asset_server, asset_storage, asset_firewall]
report = generate_report(all_assets)

# --- Professional Output ---
def print_service_mapping(service_maps):
	print("\n=== Service Mapping ===")
	for sm in service_maps:
		print(f"Service: {sm['service']}")
		print("  Assets:")
		for asset in sm['assets']:
			print(f"    - {asset.name} (ID: {asset.asset_id}, Owner: {asset.owner}, Status: {asset.lifecycle_status})")
		print()

def print_monitoring_report(report):
	print("=== Monitoring Report ===")
	for asset_name, status in report.items():
		print(f"  {asset_name}: {status}")

def print_cmdb_summary(items):
	print("=== CMDB Summary ===")
	for ci in items:
		rels = ", ".join([r.name for r in ci.relationships]) if ci.relationships else "None"
		print(f"  {ci.name} ({ci.type}) - Status: {ci.status} | Relationships: {rels}")

if __name__ == "__main__":
	print_cmdb_summary([ci_web, ci_db, ci_app, ci_firewall])
	print_service_mapping(service_maps)
	print_monitoring_report(report)
