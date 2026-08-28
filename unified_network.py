import pandas as pd 
import networkx as nx

def create_unified_network(
        relationship_file,
        cdr_file,
        transaction_file, 
        location_file
):
    graph = nx.Graph()

    # -----------------------

    # 1. General relationships

    #-------------------------

    relationships = pd.read_csv( relationship_file)
    relationships.columns=relationships.columns.str.strip()
    for _, row in relationships.iterrows():

        source = row["source"]
        target = row["target"] 
        relationship = row["type"]

        graph.add_node(source)
        graph.add_node(target)
        graph.add_edge(
            source,
            target,
            relationship=relationship)
    # -------------------
    #2. CDR relationships
    # -------------------

    cdr = pd.read_csv(cdr_file)
    cdr.columns=cdr.columns.str.strip()
    for _, row in cdr.iterrows():
        caller = row["caller"] 
        receiver = row["receiver"]

        graph.add_node(caller)
        graph.add_node(receiver)

        if graph.has_edge(caller, receiver):
            graph[caller] [receiver]["relationship"] = "Communication"
        else:
            graph.add_edge(caller,receiver,relationship="Communication")
    #-------------------
    #3. Financial relationships
    #----------------------
    transactions = pd.read_csv( transaction_file)
    transactions.columns=transactions.columns.str.strip()
    for _, row in transactions.iterrows():
        sender = row["sender"] 
        receiver = row["receiver"]

        graph.add_node(sender)
        graph.add_node(receiver)

        if graph.has_edge(sender, receiver):
            graph[sender] [receiver][ "relationship"]="Financial"
        else:
            graph.add_edge(sender,
                       receiver,
                       relationship="Financial")
    # ----------------------
    # 4. Location relationships
    # ----------------------
    locations = pd.read_csv( location_file)
    locations.columns=locations.columns.str.strip()
    for _, row in locations.iterrows():
        person = row["person"] 
        location = row["location"]

        graph.add_node(person)
        graph.add_node(location)

        graph.add_edge(
        person,
        location,
        relationship="Location")

    return graph

def get_entity_type(entity):

    if entity.startswith("Person_"): 
        return "Person"
    elif entity.startswith("Phone_"): 
        return "Phone"
    elif entity.startswith("Bank_"): 
        return "Bank"
    elif entity.startswith("Location_"): 
        return "Location"
    else:
        return "Other"
