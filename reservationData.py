import uuid


# def get_andersen_family_item():
#     andersen_item = {
#     'id': 'Andersen_' + str(uuid.uuid4()),
#     'lastName': 'Andersen',
#     'district': 'WA5',
#     'parents': [
#         {
#             'familyName': None,
#             'firstName': 'Thomas'
#         },
#         {
#             'familyName': None,
#             'firstName': 'Mary Kay'
#         }
#     ],
#     'children': None,
#     'address': {
#         'state': 'WA',
#         'county': 'King',
#         'city': 'Seattle'
#     },
#     'registered': True
# }
#     return andersen_item

# def get_wakefield_family_item():
#     wakefield_item = {
#         'id': 'Wakefield_' + str(uuid.uuid4()),
#         'lastName': 'Wakefield',
#         'district': 'NY23',
#         'parents': [
#             {
#                 'familyName': 'Wakefield',
#                 'firstName': 'Robin'
#             },
#             {
#                 'familyName': 'Miller',
#                 'firstName': 'Ben'
#             }
#         ],
#         'children': [
#             {
#                 'familyName': 'Merriam',
#                 'firstName': 'Jesse',
#                 'gender': None,
#                 'grade': 8,
#                 'pets': [
#                     {
#                         'givenName': 'Goofy'
#                     },
#                     {
#                         'givenName': 'Shadow'
#                     }
#                 ]
#             },
#             {
#                 'familyName': 'Miller',
#                 'firstName': 'Lisa',
#                 'gender': 'female',
#                 'grade': 1,
#                 'pets': None
#             }
#         ],
#         'address': {
#             'state': 'NY',
#             'county': 'Manhattan',
#             'city': 'NY'
#         },
#         'registered': True
#     }
#     return wakefield_item

def get_smith_reservation_item():
    smith_item = {
    'id': 'Table_' + str(uuid.uuid4()),
    'ownerlastName': 'Johnson',
    'ownerfirstName' : 'Smith',
    'numtablesReserved' : '1',
    'phone' : '12065559185'
    }
    return smith_item

def get_johnson_reservation_item():
    johnson_item = {
    'id': 'Table_' + str(uuid.uuid4()),
    'ownerlastName': 'Smith',
    'ownerfirstName' : 'Johnson',
    'numtablesReserved' : '2',
    'phone' : '14252865165'
    }
    return johnson_item