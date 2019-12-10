Intcode = [3,8,1001,8,10,8,105,1,0,0,21,38,63,80,105,118,199,280,361,442,99999,3,9,102,5,9,9,1001,9,3,9,1002,9,2,9,4,9,99,3,9,1001,9,4,9,102,4,9,9,101,4,9,9,102,2,9,9,101,2,9,9,4,9,99,3,9,1001,9,5,9,102,4,9,9,1001,9,4,9,4,9,99,3,9,101,3,9,9,1002,9,5,9,101,3,9,9,102,5,9,9,101,3,9,9,4,9,99,3,9,1002,9,2,9,1001,9,4,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,99]

def computer(intcode, inputs):
    memory = list(intcode)
    log = []
    halt = False
    address = 0
    i_inputs = 0
    while address != len(intcode):
        opcode = str(memory[address]).zfill(4)  # pad opcode string with '0'
        DE = int(opcode[-2:])
        if DE == 99:
            halt = True
            print(halt)
            return {'memory':memory, 'log':log, 'halt':halt}

        elif DE in (1, 2, 5, 6, 7, 8):
            # position if mode == 1 else immediate
            A = memory[address+3]
            B = memory[address+2] if opcode[-4] == '0' else address + 2
            C = memory[address+1] if opcode[-3] == '0' else address + 1
            if DE == 1:
                memory[A] = memory[B] + memory[C]
                address += 4

            elif DE == 2:
                memory[A] = memory[B] * memory[C]
                address += 4

            elif DE == 5:
                if memory[C] != 0:
                    address = memory[B]

                else: 
                    address += 3

            elif DE == 6:
                if memory[C] == 0:
                    address = memory[B]

                else: 
                    address += 3
            
            elif DE == 7:
                memory[A] = 1 if memory[B] > memory[C] else 0 
                address += 4

            elif DE == 8:
                memory[A] = 1 if memory[B] == memory[C] else 0 
                address += 4

        elif DE == 3:
            memory[memory[address+1]] = int(inputs[i_inputs])
            i_inputs = min(i_inputs + 1, len(inputs) - 1)
            address += 2

        elif DE == 4:
            log.append(memory[memory[address+1]])
            address += 2

    # return out


def generate_phase_settings(range_phase_setting):
    valid_settings = []
    for a in range_phase_setting:
        for b in range_phase_setting:
            for c in range_phase_setting:
                for d in range_phase_setting:
                    for e in range_phase_setting:
                        abcde = ''.join([str(x) for x in [a, b, c, d, e]])
                        if set(abcde) == set([str(x) for x in list(range_phase_setting)]):
                            valid_settings.append(abcde)

    return valid_settings


def amplify(intcode, phase_settings):
    thrusts = []
    for abcde in phase_settings:
        a, b, c, d, e = abcde
        amp_A = computer(intcode, [a, 0])['log'][0]
        amp_B = computer(intcode, [b, amp_A])['log'][0]
        amp_C = computer(intcode, [c, amp_B])['log'][0]
        amp_D = computer(intcode, [d, amp_C])['log'][0]
        amp_E = computer(intcode, [e, amp_D])['log'][0]
        thrusts.append(amp_E)
    
    return thrusts


print(max(amplify(Intcode, generate_phase_settings(range(5)))))


def feedback_loop(intcode, phase_settings):
    thrusts = []
    for abcde in phase_settings:
        a, b, c, d, e = abcde
        amp_A = computer(intcode, [0])       
        amp_B = computer(intcode, [b, amp_A['log'][0]])
        amp_C = computer(intcode, [c, amp_B['log'][0]])
        amp_D = computer(intcode, [d, amp_C['log'][0]])
        amp_E = computer(intcode, [e, amp_D['log'][0]])
        print(amp_E)
        while not amp_E['halt']:
            amp_A = computer(intcode, [a, amp_E['log'][0]])
            print(amp_A) 
            amp_B = computer(intcode, [b, amp_A['log'][0]])
            print(amp_B) 

            amp_C = computer(intcode, [c, amp_B['log'][0]])
            print(amp_C) 

            amp_D = computer(intcode, [d, amp_C['log'][0]])
            print(amp_D) 

            amp_E = computer(intcode, [e, amp_D['log'][0]])
            print(amp_E) 

        thrusts.append(amp_E['log'][0])
    
    return thrusts

Intcode = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
print(feedback_loop(Intcode, ['98765']))
