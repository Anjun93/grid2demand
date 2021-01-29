# GRID2DEMAND: A tool for generating zone-to-zone travel demand based on grid cells

## Introduction
Grid2demand is an open-source quick demand generation tool based on the trip generation and trip distribution methods of the standard 4-step travel model for teaching transportation planning and applications. By taking advantage of OSM2GMNS tool to obtain routable transportation network from OpenStreetMap, Grid2demand aims to further utilize Point of Interest (POI) data to construct trip demand matrix aligned with standard travel models.
## Quick Start
Users can refer to the [template code and test data set](https://github.com/asu-trans-ai-lab/Grid2Demand/) to have a quick start.

## Installation
```
pip install grid2demand
```
If you meet installation issues, please refer to the [user guide](https://github.com/asu-trans-ai-lab/grid2demand/blob/main/README.md) for solutions.


## Simple Example
```python
import grid2demand as gd
gd.ReadNetworkFiles("folder")
gd.PartitionGrid(number_of_x_blocks=None, number_of_y_blocks=None, cell_width=500, cell_height=500, latitude=30)
gd.GetPoiTripRate(trip_rate_folder="folder", trip_purpose=1)
gd.GetNodeDemand()
gd.ProduceAccessMatrix(latitude=30,accessibility_folder=None)
gd.RunGravityModel(trip_purpose=1, a=None, b=None, c=None)
gd.GenerateAgentBasedDemand()
```

## Visualization
Open [QGIS](https://www.qgis.org/) and add Delimited Text Layer of the output files.

## User guide
Users can check the [user guide](https://github.com/asu-trans-ai-lab/grid2demand/blob/main/README.md) for a detailed introduction of grid2demand.
