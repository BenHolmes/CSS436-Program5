from logging import error
from azure.cosmos import tableService, entity

table_service = tableService(account_name='myaccount', account_key='mykey')

table_service = tableService(connection_string='DefaultEndpointsProtocol=https;AccountName=myaccount;AccountKey=mykey;TableEndpoint=myendpoint;')

class res: 
	def __init__(first, last, phone, table): 
		self.first = first
		self.last = last
		self.phone = phone
		self.table = table

def sendReservation(first, last, phone, table): 
	try: 
		# IF THE TABLE NEEDS TO BE CREATED, CREATE WITH THIS LINE; COMMENT OUT OTHERWISE
		table_service.create_table('Reservation_Table')

		# reservation = res(first, last, phone, table) # initialize full object
		
		reserved = table_service.query_entities('Reservation_Table')
		tablesReserved = 0  
		reservations = 0
		for reserve in reserved: # walk through every reservation... 
			tablesReserved += reserve.tables # make this big
			reservations += 1 # increment this for row key
		if tablesReserved >= 10: 
			return
		elif tablesReserved + table > 10: 
			return
		else: # tablesReserved + num of tables user wants to reserve <= 10
			prefix = '00'
			result = "".join((prefix, str(reservations)))
			reservation = {'PartitionKey': 'res', 'RowKey': reservations, 'firstName': first, 'lastName': last, 'phoneNum': phone, 'table': table}
			table_service.insert_or_replace_entity('Reservation_Table', reservation)
			return
	except:
		print("An exception occurred")