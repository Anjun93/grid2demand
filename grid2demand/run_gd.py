import grid2demand as gd

"Step 1: Read Input Network Data"
net = gd.ReadNetworkFiles('UMD_dataset')

"Step 2: Partition Grid into cells"
zone = gd.PartitionGrid(number_of_x_blocks=None, number_of_y_blocks=None, cell_width=200, cell_height=200,
                        latitude=30)
# user can customize number of grid cells or cell's width and height

"Step 3: Get Production/Attraction Rates of Each Land Use Type with a Specific Trip Purpose"
triprate = gd.GetPoiTripRate(trip_rate_folder=None, trip_purpose=1)
# user can customize poi_trip_rate.csv and trip purpose

"Step 4: Define Production/Attraction Value of Each Node According to POI Type"
nodedemand = gd.GetNodeDemand()

"Step 5: Calculate Zone-to-zone Accessibility Matrix by Centroid-to-centroid Straight Distance"
accessibility = gd.ProduceAccessMatrix(latitude=30, accessibility_folder=None)
# user can customize the latitude of the research area and accessibility.csv

"Step 6: Apply Gravity Model to Conduct Trip Distribution"
demand = gd.RunGravityModel(trip_purpose=1, a=None, b=None, c=None)
# user can customize friction factor coefficients under a specific trip purpose

"Step 7: Generate Agent"
agent = gd.GenerateAgentBasedDemand()
