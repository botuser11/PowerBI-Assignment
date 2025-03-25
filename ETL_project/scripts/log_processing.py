import pandas as pd
from sqlalchemy import create_engine, text
import psycopg2
import os
import geoip2.database
from user_agents import parse as parse_ua
import urllib.parse

# PostgreSQL Connection
DB_USER = 'postgres'
DB_PASSWORD = urllib.parse.quote_plus('YourPasswordHere')  # Replace your password
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'postgres'

engine = create_engine(f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
conn = engine.connect()

# Paths
log_directory = '/home/craig/w3c/LogFiles/'  # Change path to match your machine
geoip_db_path = '/home/craig/w3c/GeoLite2-City.mmdb'  # GeoLite2 path
geo_reader = geoip2.database.Reader(geoip_db_path)

# Function to parse log files
def parse_logs():
    all_logs = []
    for filename in os.listdir(log_directory):
        if filename.endswith(".log"):
            filepath = os.path.join(log_directory, filename)
            with open(filepath, 'r') as f:
                for line in f:
                    if line.startswith('#'):
                        continue
                    fields = line.split()
                    try:
                        if len(fields) < 12:
                            continue
                        bytes_sent = int(fields[11]) if fields[11].isdigit() else 0
                        all_logs.append({
                            'date': fields[0],
                            'time': fields[1],
                            'ip': fields[8],
                            'method': fields[3],
                            'uri': fields[4],
                            'status': fields[10],
                            'user_agent': fields[14] if len(fields) > 14 else '',
                            'referrer': fields[13] if len(fields) > 13 else '',
                            'bytes_sent': bytes_sent
                        })
                    except:
                        continue
    df = pd.DataFrame(all_logs)
    return df

# Geolocation
def geolocate(ip):
    try:
        response = geo_reader.city(ip)
        return {
            'city': response.city.name or 'Unknown',
            'state': response.subdivisions.most_specific.name or 'Unknown',
            'country': response.country.name or 'Unknown',
            'postcode': response.postal.code or 'Unknown'
        }
    except:
        return {'city': 'Unknown', 'state': 'Unknown', 'country': 'Unknown', 'postcode': 'Unknown'}
