import grid2demand as gd

gd.ReadNetworkFiles()

gd.PartitionGrid(number_of_x_blocks=None, number_of_y_blocks=None, cell_width=500, cell_height=500, latitude=30)

gd.GetPoiTripRate(trip_purpose=1)

gd.GetNodeDemand()

gd.ProduceAccessMatrix(latitude=30)

gd.RunGravityModel(trip_purpose=1, a=None, b=None, c=None)

gd.GenerateAgentBasedDemand()