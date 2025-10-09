# 🏢 IT Service Management Framework

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![ITIL](https://img.shields.io/badge/ITIL-v4-orange.svg)](https://www.axelos.com/best-practice-solutions/itil)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)](https://github.com/yourusername/IT_Service_Management)

A comprehensive **IT Service Management (ITSM)** framework implementation that aligns with **ITIL v4** standards. This project demonstrates practical application of ITIL processes through a Python-based system for managing IT assets, configuration items, and service dependencies.

## 📋 Table of Contents

- [Features](#-features)
- [ITIL Processes Implemented](#-itil-processes-implemented)
- [Architecture](#-architecture)
- [Quick Start](#-quick-start)
- [Usage Examples](#-usage-examples)
- [ITIL Process Flow](#-itil-process-flow)
- [Maturity Assessment](#-maturity-assessment)
- [Future Enhancements](#-future-enhancements)
- [Contributing](#-contributing)

## 🚀 Features

### Core ITSM Capabilities
- **🔧 Configuration Management Database (CMDB)** - Track configuration items and relationships
- **📦 Asset Management** - Complete IT asset lifecycle tracking
- **🗺️ Service Mapping** - Map business services to technical assets
- **📊 Monitoring & Reporting** - Automated status monitoring and reporting
- **🔗 Dependency Management** - Track service and asset dependencies

### ITIL Alignment
- ✅ **Configuration Management** - CMDB with CI relationships
- ✅ **Asset Management** - Lifecycle tracking from procurement to disposal
- ✅ **Service Design** - Service-to-asset mapping
- ✅ **Service Operation** - Automated monitoring and status reporting
- ✅ **Continual Service Improvement** - Performance measurement and reporting

## 🏗️ ITIL Processes Implemented

| ITIL Process | Implementation Status | Key Features |
|--------------|----------------------|--------------|
| **Configuration Management** | ✅ Implemented | CMDB, CI relationships, dependency mapping |
| **Asset Management** | ✅ Implemented | Lifecycle tracking, ownership management |
| **Service Mapping** | ✅ Implemented | Business service to asset mapping |
| **Monitoring & Reporting** | ✅ Implemented | Automated status checks, comprehensive reports |
| **Incident Management** | 🔄 Partial | Status monitoring enables incident detection |
| **Change Management** | 🔄 Partial | CMDB relationships support impact analysis |
| **Problem Management** | 🔄 Partial | Asset relationships help root cause analysis |

## 🏛️ Architecture

```
IT_Service_Management/
├── 📁 cmdb/              # Configuration Management Database
│   └── ConfigurationItem class with relationships
├── 📁 assets/            # Asset Inventory Management  
│   └── Asset class with lifecycle tracking
├── 📁 service_mapping/   # Service-to-Asset Mapping
│   └── Service mapping functions
├── 📁 monitoring/        # Status Monitoring & Reporting
│   └── Automated monitoring and reporting
└── 📄 main.py           # Integration & Demo
```

### Key Classes

#### ConfigurationItem (CMDB)
```python
class ConfigurationItem:
    - name: str              # CI identifier
    - type: str              # CI type (Server, DB, Network)
    - status: str            # Current status (Active, Maintenance, Operational)
    - relationships: list    # Dependencies and relationships
    - add_relationship(other_item)  # Add dependency
```

#### Asset (Asset Management)
```python
class Asset:
    - asset_id: str          # Unique asset identifier
    - name: str              # Asset name
    - owner: str             # Asset owner/responsible party
    - lifecycle_status: str  # Current lifecycle state
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- No external dependencies required

### Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/IT_Service_Management.git
cd IT_Service_Management

# Run the demo
python main.py
```

### Expected Output
```
=== CMDB Summary ===
  Web Server (Server) - Status: Active | Relationships: None
  Database (DB) - Status: Active | Relationships: Web Server
  Application Server (Server) - Status: Maintenance | Relationships: Database
  Firewall (Network) - Status: Operational | Relationships: Web Server

=== Service Mapping ===
Service: Website Hosting
  Assets:
    - Server (ID: A004, Owner: Bob, Status: Active)
    - Router (ID: A002, Owner: IT Dept, Status: Operational)
    - Switch (ID: A003, Owner: IT Dept, Status: Operational)

=== Monitoring Report ===
  Laptop: OK
  Router: Warning
  Switch: OK
  Server: OK
  Storage Array: Critical
  Firewall Appliance: OK
```

## 💡 Usage Examples

### Creating Configuration Items
```python
from cmdb import ConfigurationItem

# Create CIs
web_server = ConfigurationItem("Web Server", "Server", "Active")
database = ConfigurationItem("Database", "DB", "Active")

# Add relationships
database.add_relationship(web_server)
```

### Managing Assets
```python
from assets import Asset

# Create assets
laptop = Asset("A001", "Laptop", "Alice", "In Use")
server = Asset("A004", "Server", "Bob", "Active")
```

### Service Mapping
```python
from service_mapping import map_service_to_assets

# Map service to assets
website_service = map_service_to_assets("Website Hosting", [server, router, switch])
```

### Monitoring and Reporting
```python
from monitoring import generate_report

# Generate status report
all_assets = [laptop, server, router, switch]
report = generate_report(all_assets)
```

## 🔄 ITIL Process Flow

### Service Lifecycle Overview
```mermaid
graph TD
    A[Service Strategy] --> B[Service Design]
    B --> C[Service Transition]
    C --> D[Service Operation]
    D --> E[Continual Service Improvement]
    E --> A
    
    A1[Service Portfolio] --> A
    B1[Service Catalog] --> B
    C1[Change Management] --> C
    D1[Incident Management] --> D
    E1[7-Step Process] --> E
```

### Incident Management Process
```mermaid
graph TD
    A[Incident Detected] --> B[Incident Logged]
    B --> C[Initial Categorization]
    C --> D{Priority Assessment}
    D -->|High| E[Immediate Escalation]
    D -->|Medium| F[Standard Processing]
    D -->|Low| G[Routine Processing]
    E --> H[Resolution]
    F --> H
    G --> H
    H --> I[Closure]
    I --> J[Post-Resolution Review]
```

### Change Management Process
```mermaid
graph TD
    A[Change Request] --> B[RFC Creation]
    B --> C[Initial Assessment]
    C --> D{Change Type}
    D -->|Standard| E[Pre-approved]
    D -->|Normal| F[CAB Review]
    D -->|Emergency| G[Emergency CAB]
    E --> H[Implementation]
    F --> I{Approved?}
    G --> I
    I -->|Yes| H
    I -->|No| J[Rejected]
    H --> K[Post-Implementation Review]
    K --> L[Closed]
```

## 📊 Maturity Assessment

### Current Maturity Level: **2-3** (Managed to Defined)

#### ✅ Achieved Capabilities
- Basic CMDB implementation with CI relationships
- Asset lifecycle tracking and ownership management
- Service mapping capabilities for impact analysis
- Automated monitoring and status reporting
- Modular, extensible architecture

#### 🔄 Areas for Improvement
- Process formalization and documentation
- Integration between ITSM processes
- Metrics collection and KPI tracking
- Governance and control mechanisms

### Target Maturity Level: **4-5** (Quantitatively Managed to Optimizing)

## 🎯 Future Enhancements

### Phase 1: Foundation (Months 1-3)
- [ ] **Process Documentation** - Document all ITSM processes
- [ ] **Basic Metrics** - Implement KPI collection and dashboards
- [ ] **Data Persistence** - Add database support (SQLite/PostgreSQL)

### Phase 2: Enhancement (Months 4-6)
- [ ] **Process Integration** - Connect CMDB with incident management
- [ ] **Workflow Automation** - Implement ticket creation and approval workflows
- [ ] **Web Interface** - Create web-based dashboard

### Phase 3: Optimization (Months 7-9)
- [ ] **Advanced Analytics** - Add trend analysis and predictive capabilities
- [ ] **Service Level Management** - Implement SLA monitoring and reporting
- [ ] **API Integration** - REST API for external system integration

### Phase 4: Innovation (Months 10-12)
- [ ] **Continuous Improvement** - Implement CSI processes
- [ ] **Machine Learning** - Add predictive analytics and automated remediation
- [ ] **Advanced Features** - Mobile apps, chatbot integration

## 📈 Key Performance Indicators (KPIs)

| Metric | Description | Target | Status |
|--------|-------------|---------|--------|
| **Service Availability** | Percentage of time service is available | 99.9% | 🔄 In Development |
| **MTTR** | Mean Time To Repair | < 4 hours | 🔄 In Development |
| **Change Success Rate** | Percentage of successful changes | 95% | 🔄 In Development |
| **Asset Accuracy** | CMDB data accuracy | 98% | ✅ Implemented |

## 🤝 Contributing

We welcome contributions to improve this ITSM framework! Here's how you can help:

### How to Contribute
1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Areas for Contribution
- 🔧 **Process Implementation** - Add missing ITIL processes
- 📊 **Analytics & Reporting** - Enhance monitoring and reporting capabilities
- 🎨 **User Interface** - Improve user experience and dashboards
- 📚 **Documentation** - Expand documentation and examples
- 🧪 **Testing** - Add comprehensive test coverage

## 📚 ITIL Learning Resources

### Certification Paths
- **ITIL Foundation** - Entry-level certification (2-3 days)
- **ITIL Intermediate** - Specialized modules (Service Lifecycle & Capability)
- **ITIL Expert** - Advanced knowledge and application
- **ITIL Master** - Real-world leadership and implementation

### Key ITIL Concepts Demonstrated
- **Service Value System (SVS)** - End-to-end service delivery
- **Service Value Chain** - Plan, Improve, Engage, Design & Transition, Obtain/Build, Deliver & Support
- **Guiding Principles** - Focus on value, start where you are, progress iteratively
- **Management Practices** - 34 practices including the core ITSM processes

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **ITIL Framework** - Based on AXELOS ITIL v4 best practices
- **Python Community** - For the excellent tools and libraries
- **ITSM Professionals** - For sharing knowledge and best practices

## 📞 Support

- 📧 **Email**: me@shayshab.xyz
- 💬 **Discussions**: [GitHub Discussions](https://github.com/yourusername/IT_Service_Management/discussions)
- 🐛 **Issues**: [GitHub Issues](https://github.com/yourusername/IT_Service_Management/issues)
- 📖 **Documentation**: [Wiki](https://github.com/yourusername/IT_Service_Management/wiki)

---

<div align="center">

**Built with ❤️ for the IT Service Management Community**

[⭐ Star this repo](https://github.com/yourusername/IT_Service_Management) | [🍴 Fork it](https://github.com/yourusername/IT_Service_Management/fork) | [🐛 Report Bug](https://github.com/yourusername/IT_Service_Management/issues) | [💡 Request Feature](https://github.com/yourusername/IT_Service_Management/issues)

</div>
