import osm2gmns as og

net = og.getNetFromOSMFile('map.osm', network_type=('railway', 'aeroway', 'auto'), POIs=True, default_lanes=True,default_speed=True)

og.connectPOIWithNet(net)

og.generateNodeActivityInfo(net)

og.outputNetToCSV(net)