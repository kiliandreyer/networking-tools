def calculate(ip, mask):
    # initialize 
    binary_ip = []
    binary_mask = []
    network_id = []
    network_id_text = ""
    network_id_text1 = ""
    network_id_text2 = ""
    network_id_text3 = ""
    # Append binary to new lists
    for i in range(0, 4):
        binary_ip.append(bin(int(ip[i]))[2:])
        binary_mask.append(bin(int(mask[i]))[2:])
    # Calculate
    for x, y in zip(str(binary_ip[0]), str(binary_mask[0])):
        if x == y:
            network_id_text = network_id_text + "1"
        else:
            network_id_text = network_id_text + "0"
    network_id.append(network_id_text)   
    for x, y in zip(str(binary_ip[1]), str(binary_mask[1])):
        if x == y:
            network_id_text1 = network_id_text1 + "1"
        else:
            network_id_text1 = network_id_text1 + "0"
    network_id.append(network_id_text1)   
    for x, y in zip(str(binary_ip[2]), str(binary_mask[2])):
        if x == y:
            network_id_text2 = network_id_text2 + "1"
        else:
            network_id_text2 = network_id_text2 + "0"
    network_id.append(network_id_text2)   
    for x, y in zip(str(binary_ip[3]), str(binary_mask[3])):
        if x == y:
            network_id_text3 = network_id_text3 + "1"
        else:
            network_id_text3 = network_id_text3 + "0"
    network_id.append(network_id_text3)       

    # Convert from binary to decimal
    first = int(network_id[0], 2)
    second = int(network_id[1], 2)
    third = int(network_id[2], 2)
    fourth = int(network_id[3], 2)

    return (str(first) + "." + str(second) + "." + str(third) + "." + str(fourth))
