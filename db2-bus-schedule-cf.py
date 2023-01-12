import sys
import json
import os, ibm_db, ibm_db_dbi as dbi, pandas as pd
import requests

def main(params):
    db2_dsn = 'DATABASE={};HOSTNAME={};PORT={};PROTOCOL=TCPIP;UID={uid};PWD={pwd};SECURITY=SSL'.format(
        'bludb',
        'fbd88901-ebdb-4a4f-a32e-9822b9fb237b.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud',
        '32731',
        uid='lvr69441',
        pwd='R1SY9svsyKX3ruMV'
    )
    
    db2_connection = dbi.connect(db2_dsn)
    query = 'SELECT * FROM "LVR69441"."BUS_SCHEDULE"'
    bus_df = pd.read_sql_query(query, con=db2_connection)
   
    bus_route = params['bus_route']
    bus_stop = params['bus_stop'].lower()
    response = {}

    query_df = bus_df[(bus_df.BUS_ROUTE == bus_route) & (bus_df.BUS_STOP == bus_stop)]
        
    if query_df.shape[0] <= 0:
        response = {"Error" : "There are no records available with this data"}
    else:
        bus_route = query_df.BUS_ROUTE.item()
        bus_stop = query_df.BUS_STOP.item()
        bus_time = query_df.SCHEDULED_ARRIVAL_TIME.item()
        return_string = "Bus " + str(bus_route) + " is scheduled to arrive at " + bus_stop + " at " + str(bus_time)
        response = {"bus_message": return_string}
    return response
