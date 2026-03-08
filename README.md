# AWSatisfactory

[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://www.python.org/)

An advanced production line simulator for the video game **Satisfactory**, integrated with AWS cloud infrastructure for energy cost analysis and industrial process optimization.

## 🎯 Overview

AWSatisfactory simulates production lines from the assembly phases of the Satisfactory game, cross-referencing production data with real-time electricity prices from the Energy Charts API. The system identifies bottlenecks, calculates operational costs, and provides insights for production line optimization.

### ✨ Key Features

- **Production Line Simulation** : Faithful modeling of machines, recipes, and production flows
- **Energy Integration** : Real-time electricity price retrieval via Energy Charts API
- **Cost Analysis** : Automatic calculation of production line energy costs
- **Bottleneck Detection** : Failure simulation to identify breaking points
- **Cloud Architecture** : Data storage and processing on AWS (DataLake + DataWarehouse)
- **Visualization** : Interactive dashboards with AWS QuickSight
- **Orchestration** : Automation via AWS Lambda and EventBridge

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Simulation    │    │   Energy API    │    │     AWS Cloud   │
│   Engine        │◄──►│   (Energy       │    │   (DataLake)    │
│                 │    │    Charts)      │    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│  Cost Analysis  │    │   Data          │    │   QuickSight    │
│                 │    │   Processing    │    │   Dashboard     │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

### Components

#### 🔧 Simulation Engine
- **Domain Models** : Machines, recipes, items, production lines
- **Production Lines** : Assembly phase production chains (Phase 2)
- **Fault Simulation** : Failure injection for bottleneck analysis

#### ⚡ Energy Integration
- **Energy Charts API** : Spot electricity prices retrieval (EUR/MWh)
- **Cost Calculator** : Energy costs calculation per machine and line
- **Time Series** : Price history for temporal analysis

#### ☁️ AWS Infrastructure
- **DataLake (S3)** : Raw storage of simulation and energy data
- **DataWarehouse (Redshift)** : Analytical database for complex queries
- **Lambda Functions** : Serverless data processing
- **EventBridge** : Scheduled task orchestration
- **QuickSight** : Visualization and dashboards

## 🚀 Installation

### Prerequisites
- Python 3.12+
- Configured AWS CLI
- AWS account with appropriate permissions

### Local Installation

```bash
# Clone repository
git clone https://github.com/TomPineau/AWSatisfactory
cd AWSatisfactory

# Development mode installation
pip install -e .

# Additional dependencies installation
pip install pandas boto3 awscli
```

### AWS Configuration

```bash
# AWS CLI configuration
aws configure

## 📊 Usage

### Basic Simulation

```python
from awsatisfactory.simulation.run_simulation import run_simulation

# Launch simulation
run_simulation()
```

### Energy Price Retrieval

```python
from awsatisfactory.data_sources.EnergyCharts import EnergyCharts

# Create instance for France
energy_api = EnergyCharts("price", "FR")

# Retrieve data
data = energy_api.fetch_data()
print(f"Current price: {data['price'][-1]} EUR/MWh")
```

### Cost Analysis

# TODO

# Calculate production costs
# TODO: Implement cost calculation
```

## 🏭 Simulated Production Lines

### Phase 2 - Project Assembly

#### Automated Wiring Line
- **Inputs** : Iron, Coal, Copper
- **Outputs** : Automated Wiring
- **Machines** : Miners, Smelters, Constructors, Assemblers
- **Overclocks** : Optimizations to maximize production

#### Smart Plating Line
- **Inputs** : Iron, Coal
- **Outputs** : Smart Plating
- **Focus** : Bottleneck analysis

#### Versatile Framework Line
- **Inputs** : Iron, Coal
- **Outputs** : Versatile Framework
- **Complexity** : Multi-step chain with dependencies

## 🔍 Data Analysis

### Calculated Metrics
- **Production Rate** : Items/minute per line
- **Energy Cost** : Total energy cost (€/hour)
- **Efficiency** : Machine efficiency with overclock
- **Bottlenecks** : Identified breaking points
- **ROI** : Energy return on investment

### QuickSight Visualizations
- **Real-time Dashboards** : Production metrics
- **Cost Analysis** : Energy price evolution
- **Heat Maps** : Bottleneck identification
- **Automated Reports** : PDF/CSV exports

## 🔄 AWS Orchestration

### AWS Lambda
- **Data Ingestion** : Energy Charts data retrieval
- **Simulation Runner** : Cloud-based simulation execution
- **Cost Calculator** : Energy cost calculations
- **Data Processing** : Data transformation and cleaning

### AWS EventBridge
- **Scheduled Runs** : Automated simulations (hourly/daily)
- **API Calls** : Regular energy price retrieval
- **Alerts** : Notifications for threshold exceedances
- **Maintenance** : Cleanup and archiving tasks

## 📈 Usage Examples

### Simulation with Energy Data

```python
from awsatisfactory.simulation.run_simulation import run_simulation
from awsatisfactory.data_sources.EnergyCharts import EnergyCharts
import pandas as pd

# Retrieve energy prices
energy_api = EnergyCharts("price", "FR")
energy_data = energy_api.fetch_data()

# Production simulation
simulation_results = run_simulation()

# Cross analysis
# TODO: Implement production/energy cross analysis
```

### Bottleneck Detection

```python
# Simulation with failure injection
# TODO: Implement failure simulation
bottleneck_analysis = simulate_with_failures()
print(f"Identified bottlenecks: {bottleneck_analysis}")
```

## 🧪 Testing

```bash
# Run tests
python -m pytest tests/

# Specific test
python tests/test_production_lines.py
```

## 🤝 Contributing

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 Roadmap

- [ ] Complete implementation of assembly phases
- [ ] Real-time integration with Energy Charts API
- [ ] Advanced failure simulation and recovery
- [ ] Complete AWS infrastructure
- [ ] Predefined QuickSight dashboards
- [ ] Multi-region support for energy prices

## 🙏 Acknowledgments

- **Coffee Stain Studios** for the Satisfactory game, so much hours spent on this game and not even close from the end. Currently at Phase 3, with fuel generators.
- **Energy Charts** for the public energy price API
- **AWS** for the cloud infrastructure

## 📞 Contact

- **Author** : [Tom Pineau]
- **Email** : [tom.pineau@hotmail.fr]
- **LinkedIn** : [https://www.linkedin.com/in/tom-pineau/]

---

*Built with ❤️ to optimize Satisfactory production lines*