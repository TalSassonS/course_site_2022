from enum import Enum
from collections import namedtuple


def pop_out_agents(agents_list: tuple):
    """
    The function receives a list of agents and omitt all agents that are healthy or dead

    Parameters
    ----------
    agent_listing : tuple of Agents
    A list of all the agents with their name and status


    Returns
    -------
    new_agents_list : list
    The new list without the dead and healthy agents
    pop_out_list : list
    The list of all agents that were removed (the healthy and dead agents)
    """
    new_agents_list = []
    pop_out_list = []
    for agent in agents_list:
        if agent[1].name != "HEALTHY" and agent[1].name != "DEAD":
            new_agents_list += [agent]
        elif agent[1].name == "HEALTHY" or agent[1].name == "DEAD":
            pop_out_list += [agent]
    return (new_agents_list, pop_out_list)

def assigned_agents_meetings(agents_list: list):
    """The function receives a list of agents and takes out a new list of pairs of agents (tuples).
    If a single agent remains (there is an odd number of agents), it will be entered in the new list as its own tuple.

    Parameters
    ----------
    agent_listing : tuple of Agents
    A list of all the agents with their name and status

    Returns
    -------
    new_agents_list : list
    List of the agents sorted in pairs of meetings

    """
    new_agents_list = []

    while len(agents_list) > 1:
        first_agent = agents_list[0]
        second_agent = agents_list[1]
        agents_list.remove(first_agent)
        agents_list.remove(second_agent)
        tuple = (first_agent, second_agent,)
        new_agents_list += [tuple]

    if len(agents_list) ==1:
        tuple = (agents_list[0],)
        new_agents_list += [tuple]
    return new_agents_list

def pop_and_assigned(list_of_agents: tuple):
    """
    This function receives a list of agents and returns a list of agents sorted into pairs excluding the healthy and dead agents.
    The function also returns a list of all the healthy and dead agents.


    Parameters
    ----------
    list_of_agents : tuple of Agents
    A list of all the agents with their name and status

    Returns
    -------
    tuple_of_agents : tuple
    List of the agents sorted in pairs of meetings

    pop_out_list: list
    The list of all agents that were omitted
    """
    return_tuple = pop_out_agents(list_of_agents)
    pop_out_list = return_tuple[1]
    list_of_agents = return_tuple[0]
    list_of_agents = assigned_agents_meetings(list_of_agents)
    tuple_of_agents = tuple(list_of_agents)
    return (tuple_of_agents, pop_out_list)


def die_one(agent):
    """
    This function receives an agent and brings its status down by one level (sick will become dying, dying will become dead)

    Parameters
    ----------
    agent : Agent
    An agent including its name and status

    Returns
    -------
    agent : Agent
    An agent including its name and status (one level down)
    """

    agent =  Agent(agent[0], Type(agent[1].value +1))
    return agent


def cure_one(agent):
    """
    This function receives an agent and brings its status up by one level (sick will become healthy, dying will become sick)

    Parameters
    ----------
    agent : Agent
    An agent including its name and status

    Returns
    -------
    agent : Agent
    An agent including its name and status (one level up)
    """

    agent =  Agent(agent[0], Type(agent[1].value -1))
    return agent


def meetup(agent_listing: tuple) -> list:
    """Model the outcome of the meetings of pairs of agents.

    The pairs of agents are ((a[0], a[1]), (a[2], a[3]), ...). If there's an uneven
    number of agents, the last agent will remain the same.

    Notes
    -----
    The rules governing the meetings were described in the question. The outgoing
    listing may change its internal ordering relative to the incoming one.

    Parameters
    ----------
    agent_listing : tuple of Agent
        A listing  in which each element is of the Agent
        type.
        

    Returns
    -------
    updated_listing : list
        A list of Agents with their situation updated
       
    """

    return_tuple = pop_and_assigned(agent_listing)
    pop_out_list = return_tuple [1]
    agent_listing = return_tuple[0]

    new_list = []
    for meeting in agent_listing:
        if len(meeting) == 1:
            new_list += [meeting[0]]

        elif meeting[0][1].value == 1 and meeting[1][1].value == 1:
            new_list += [meeting[0]]
            new_list += [meeting[1]]

        elif meeting[0][1].value == 1 and meeting[1][1].value != 1:
            new_list += [cure_one(meeting[1])]
            new_list += [meeting[0]]

        elif meeting[0][1].value != 1 and meeting[1][1].value == 1:
            new_list += [cure_one(meeting[0])]
            new_list += [meeting[1]]

        elif meeting[0][1].value != 1 and meeting[1][1].value != 1:
            new_list += [die_one (meeting[0])]
            new_list += [die_one (meeting[1])]

    for agent in pop_out_list:
        new_list += [agent]

    agents_status_after_meetings_list = new_list
    return  agents_status_after_meetings_list


#Program

Type = Enum("Type", ("CURE", "HEALTHY", "SICK", "DYING", "DEAD"))
Agent = namedtuple("Agent", ("name", "category"))
