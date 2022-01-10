from opentrons import protocol_api

# copied from the json file
metadata = {
    "protocolName": "SCORE test",
    "author": "The CRI / Tatiana Prist",
    "description": "this is a simple test protocol",
    "created": 1641819540901,
    "lastModified": 1641820713381,
    "category": null,
    "subcategory": null,
    "tags": [],
    'apiLevel': '2.11'}

amount = 12.5
result_plateD = ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1']
Source_plate = ['A1']

# обязательно писать функцию run пч робот не понимает без нее
def run(protocol: protocol_api.ProtocolContext):
    source_plate = protocol.load_labware('corning_96_wellplate_2ml_deep', 1)
    result_plate = protocol.load_labware('corning_96_wellplate_2ml_deep', 2)
    tiprack_1 = protocol.load_labware('opentrons_96_tiprack_300ul', 3)
    p300 = protocol.load_instrument('p300_single', 'left', tip_racks=[tiprack_1])


for source in [0-6]:
    p300.transfer(amount,
                  source=source,
                  dest=result_plate
                  )
    amount += 12.5
