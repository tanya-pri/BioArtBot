from opentrons import protocol_api

metadata = {
    "protocolName": "Mixing2",
    "author": "CRI / PRISTINSKAYA, IMEZGAREN",
    "description": "transformation of P.pastoris",
    'apiLevel': '2.11'}

def run(protocol: protocol_api.ProtocolContext):
    tiprack_1 = protocol.load_labware('opentrons_96_tiprack_1000ul', 6)
    source_plate = protocol.load_labware('nest_12_reservoir_15ml', 7)
    result_plate = protocol.load_labware('nest_96_wellplate_2ml_deep', 4)
    p1000 = protocol.load_instrument('p1000_single', 'left', tip_racks=[tiprack_1])

    #1 Wash the cells with 1 ml of water

    #2 Add 1 ml LiCl to each well:
    p1000.pick_up_tip()
    p1000.transfer(1000,
                     source_plate['A1'],
                     result_plate['A1'],
                     new_tip = 'never'
                     )
    p1000.mix(10, 600, result_plate['A1'].bottom(0.5), rate = 2.5)
    
    p1000.return_tip()

    #3 incubation:
    protocol.pause('Incubate for 10 minutes, wash')

    #4 add 400ul of LiCl:
    p1000.pick_up_tip()
    p1000.transfer(400,
                    source_plate['A1'],
                    result_plate['A1'],
                    new_tip = 'never'
                    )
    p1000.mix(7, 250, result_plate['A1'].bottom(0.5), rate = 2.5)

    p1000.return_tip()

    #4.5 dilution
    p1000.pick_up_tip()

    p1000.mix(7, 250, result_plate['A1'].bottom(0.5), rate = 2.5)
    p1000.distribute(50, 
                      result_plate['A1'],
                      result_plate.columns_by_name()['2'][:6],
                      new_tip = 'never'
                      )
    p1000.drop_tip()

    #5 centrifuge
    protocol.pause('centrefuge')

    #6 add the DNA mix to the wells 
    ls = ['A', 'B', 'C', 'D', 'E', 'F']  
    for i in range (2):
      p1000.pick_up_tip()

      p1000.transfer(339,
                     source_plate['A3'],
                     result_plate['{}2'.format(ls[i])],
                     mix_before = (5, 450),
                     air_gap =(20),
                     touch_tip = True,
                     new_tip = 'never'
                     )
             
      p1000.mix(12, 200, result_plate['{}2'.format(ls[i])].bottom(0.5), rate = 1.5)
      
      p1000.drop_tip()

    for i in range (3):
      p1000.pick_up_tip()

      p1000.transfer(339,
                     source_plate['A3'],
                     result_plate['{}2'.format(ls[i+2])],
                     mix_before = (5, 450),
                     air_gap =(20),
                     touch_tip = True,
                     new_tip = 'never'
                     )
             
      p1000.mix(12, 200, result_plate['{}2'.format(ls[i+2])].bottom(0.5), rate = 1.5)
      
      p1000.drop_tip()
      