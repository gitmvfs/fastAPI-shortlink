from cassandra.cqlengine import connection
from cassandra.cqlengine.management import create_keyspace_simple
from cassandra.cluster import Cluster
from cassandra.query import dict_factory
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

#env
node_database_string = str(os.getenv('node_database'))
node_database_list = node_database_string.split(',')
replication_factor = int(os.getenv('replication_factor'))

#Allow permissions schema managment
os.environ['CQLENG_ALLOW_SCHEMA_MANAGEMENT'] = '1'

#Innitial connection 
cluster = Cluster(node_database_list)
session = cluster.connect()

#Create keyspace for local dev
keyspace_name = 'database_url'

def get_database_session():
    try:
        connection.setup(node_database_list, keyspace_name, protocol_version=3)
        
        create_keyspace_simple(keyspace_name, replication_factor=replication_factor)
        
        session = cluster.connect(keyspace_name)
        session.row_factory = dict_factory
        
        print(f'ScyllaDB connected to successfully!')
        return session
    except Exception as e:
        print(f'Error in database process: {e}')
        return None