import array


def node_flow_in_order(nodes):
    # Find the maximum position to ensure flow_array has enough space
    max_position = max(node["node_position"] for node in nodes)
    # Initialize flow_array with None values based on the highest node position
    flow_array = [None] * max_position

    for node in nodes:
        position = node["node_position"] - 1  # Adjust for 1-based index
        flow_array[position] = (
            node  # Assign the node dictionary to the correct position
        )

    return flow_array
