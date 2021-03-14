from azure.cosmos import exceptions, CosmosClient, PartitionKey
import reservationData

# Initialize the Cosmos client
endpoint = "endpoint" #waiting until I sumon the courage to use azure lol
key = 'primary_key' #the part I am scared of

# <create_cosmos_client>
client = CosmosClient(endpoint, key)
# </create_cosmos_client>

# Create a database
# <create_database_if_not_exists>
database_name = 'AzureReservationDatabase'
database = client.create_database_if_not_exists(id=database_name)
# </create_database_if_not_exists>

# Create a container
# Using a good partition key improves the performance of database operations.
# <create_container_if_not_exists>
container_name = 'ReservationContainer'
container = database.create_container_if_not_exists(
    id=container_name, 
    partition_key=PartitionKey(path="/lastName"),
    offer_throughput=400
)
# </create_container_if_not_exists>


# Add items to the container
reservation_items_to_create = [reservationData.get_smith_reservation_item(), reservationData.get_johnson_reservation_item()]

 # <create_item>
for reservation_item in reservation_items_to_create:
    container.create_item(body=reservation_item)
# </create_item>

# Read items (key value lookups by partition key and id, aka point reads)
# <read_item>
for reservation in reservation_items_to_create:
    item_response = container.read_item(item=reservation['id'], partition_key=reservation['lastName'])
    request_charge = container.client_connection.last_response_headers['x-ms-request-charge']
    print('Read item with id {0}. Operation consumed {1} request units'.format(item_response['id'], (request_charge)))
# </read_item>

# Query these items using the SQL query syntax. 
# Specifying the partition key value in the query allows Cosmos DB to retrieve data only from the relevant partitions, which improves performance
# <query_items>
query = "SELECT * FROM c WHERE c.lastName IN ('Wakefield', 'Andersen')"

items = list(container.query_items(
    query=query,
    enable_cross_partition_query=True
))

request_charge = container.client_connection.last_response_headers['x-ms-request-charge']

print('Query returned {0} items. Operation consumed {1} request units'.format(len(items), request_charge))
# </query_items>