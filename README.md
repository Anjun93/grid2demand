# GRID2DEMAND: A tool for generating zone-to-zone travel demand based on grid cells

## Introduction
Grid2demand is an open-source quick demand generation tool based on the trip generation and trip distribution methods of the standard 4-step travel model for teaching transportation planning and applications. By taking advantage of OSM2GMNS tool to obtain routable transportation network from OpenStreetMap, Grid2demand aims to further utilize Point of Interest (POI) data to construct trip demand matrix aligned with standard travel models.
## Quick Start
Users can refer to the [code template and test data set](https://github.com/asu-trans-ai-lab/Grid2Demand/) to have a quick start.

## Installation
```
pip install grid2demand
```
If you meet installation issues, please refer to the [user guide](https://github.com/asu-trans-ai-lab/grid2demand/blob/main/README.md) for solutions.


## Simple Example
```python
import grid2demand as gd

"Step 1: Read Input Network Data"
gd.ReadNetworkFiles()

"Step 2: Partition Grid into cells"
gd.PartitionGrid(number_of_x_blocks=None, number_of_y_blocks=None, cell_width=1000, cell_height=1000, latitude=30)
# users can customize number of grid cells or cell's width and height in meters

"Step 3: Get Production/Attraction Rates of Each Land Use Type with a Specific Trip Purpose"
gd.GetPoiTripRate(trip_purpose=1)
# users can customize trip purpose and poi_trip_rate.csv

"Step 4: Define Production/Attraction Value of Each Node According to POI Type"
gd.GetNodeDemand(residential_production=20, residential_attraction=20, boundary_production=1000, boundary_attraction=1000)
# users can customize production and attraction values of residential nodes and boundary nodes

"Step 5: Calculate Zone-to-zone Accessibility Matrix by Centroid-to-centroid Straight Distance"
gd.ProduceAccessMatrix(latitude=30)
# users need to input the latitude of the area of interest for calculating accessibility

"Step 6: Apply Gravity Model to Perform Trip Distribution"
gd.RunGravityModel(trip_purpose=1, a=None, b=None, c=None)
# users can customize friction factor coefficients under a specific trip purpose

"Step 7: Generate Agent"
gd.GenerateAgentBasedDemand()
```

## Visualization
Open [QGIS](https://www.qgis.org/) and add Delimited Text Layer of the output files.

## User guide
Users can check the [user guide](https://github.com/asu-trans-ai-lab/grid2demand/blob/main/README.md) for a detailed introduction of grid2demand.
