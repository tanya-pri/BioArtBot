#protocol_new

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
    ls = ['A', 'B', 'C', 'D', 'E', 'F'] 
    #2 Add 1 ml 1M and 100mM LiCl to each well:
    p1000.pick_up_tip()
    p1000.transfer(1000,
                        source_plate['A1'],
                        result_plate['A1'],
                        mix_before = (3, 1000),
                        new_tip = 'never'
                        )
    p1000.mix(12, 700, result_plate['A1'], rate = 3)
    p1000.return_tip()
    p1000.pick_up_tip()
    p1000.transfer(1000,
                        source_plate['A1'],
                        result_plate['B1'],
                        mix_before = (3, 1000),
                        new_tip = 'never'
                        )
    p1000.mix(12, 700, result_plate['B1'], rate = 3)
    p1000.return_tip()
    p1000.pick_up_tip()
    p1000.transfer(1000,
                        source_plate['A2'],
                        result_plate['C1'],
                        mix_before = (3, 1000),
                        new_tip = 'never'
                        )
    p1000.mix(12, 700, result_plate['C1'], rate = 3)
    p1000.return_tip()
    p1000.pick_up_tip()
    p1000.transfer(1000,
                        source_plate['A2'],
                        result_plate['D1'],
                        mix_before = (3, 1000),
                        new_tip = 'never'
                        )
    p1000.mix(12, 700, result_plate['D1'], rate = 3)
    p1000.return_tip()
    
    #3 incubation:
    protocol.pause('Incubate for 10 minutes, wash')

    #4 add 400ul of LiCl:
    for i in range(4):
        if i <= 1 :
            p1000.pick_up_tip()
            p1000.transfer(400,
                    source_plate['A1'],
                    result_plate['{}1'.format(ls[i])],
                    mix_before = (3, 1000),
                    new_tip = 'never'
                    )
            p1000.mix(12, 300, result_plate['{}1'.format(ls[i])], rate = 3)
            p1000.return_tip() 
        else :
            p1000.pick_up_tip()
            p1000.transfer(400,
                    source_plate['A2'],
                    result_plate['{}1'.format(ls[i])],
                    mix_before = (3, 1000),
                    new_tip = 'never'
                    )
            p1000.mix(12, 300, result_plate['{}1'.format(ls[i])], rate = 3)
            p1000.return_tip()

    #4.5 dilution 
    for i in range(4):
        p1000.pick_up_tip()
        p1000.mix(12, 300, result_plate['{}1'.format(ls[i])], rate = 3)
        p1000.distribute(50, 
                      result_plate['{}1'.format(ls[i])],
                      result_plate.rows_by_name()[ls[i]][1:7],
                      new_tip = 'never'
                      )
        p1000.return_tip()
 

    #5 centrifuge
    protocol.pause('centrefuge')

    #6 add the LiCl 36uL to the wells  
    for i in range(4):
        if i <= 1 :
            p1000.pick_up_tip()
            p1000.distribute(36, 
                    source_plate['A1'],
                    result_plate.rows_by_name()[ls[i]][1:7],
                    new_tip = 'never'
            )
            p1000.return_tip()
        else:
            p1000.pick_up_tip()
            p1000.distribute(36, 
                    source_plate['A2'],
                    result_plate.rows_by_name()[ls[i]][1:7],
                    new_tip = 'never'
            )
            p1000.return_tip()

    # add PEG and SSDNA:
    for i in range (4):
        p1000.transfer(265, 
                    source_plate['A3'],
                    result_plate.rows_by_name()[ls[i]][1:7],
                    mix_before = (8, 450),
                    air_gap =(20),
                    touch_tip = True,
                    new_tip = 'always'
        )

    #add plasmid 1 or 2 ug and water for volume balance:
    for i in range (6):
        if i <= 3 :
            p1000.distribute(1,
                    result_plate['A12'],
                    result_plate.columns_by_name()[str(i+1)][:4],
                    new_tip = 'always'
                    )
        else :
            p1000.distribute(2,
                    result_plate['A12'],
                    result_plate.columns_by_name()[str(i+1)][:4],
                    new_tip = 'always'
            )
                
    # Add DMSO and water balance
    for i in range (4):
        if i == 1 or i == 3:
            p1000.distribute(30, 
                    result_plate['A11'],
                    result_plate.rows_by_name()[ls[i]][:6]
            )
        else:
             p1000.distribute(30, 
                    source_plate['A6'],
                    result_plate.rows_by_name()[ls[i]][:6]
                    )

    for i in range(4):
        for y in range(6):
            p1000.pick_up_tip()
            p1000.mix(15, 240, result_plate['{}{}'.format(ls[i], str(y+1))])
            p1000.return_tip()