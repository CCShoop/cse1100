'''Random Agent Selector by Cael Shoop.'''

import tkinter as tk # GUI
from tkinter import ttk
from tkinter.messagebox import showerror, showinfo
import random # random number selector for choosing agents
import configparser as cp # Saving player info in .ini config file
import os
import sys
import time

# Global config instances and list of Valorant agents
agentConfig = cp.ConfigParser()
try:
    agentConfig.read_file(open('agents.ini'))
except: # Throws non-fatal error if file doesn't exist
    showerror(title='Error', message='agents.ini not found. Please add agents.')
    agentConfig.read('agents.ini')
    main()
agents = [] # List of agents
for agent in agentConfig.sections():
    agents.append(agent)
playerConfig = cp.ConfigParser()
try:
    playerConfig.read_file(open('players.ini'))
except:
    showerror(title='Error', message='players.ini not found. Please add players.')
    playerConfig.read('players.ini')
    main()
changed = False
for player in playerConfig.sections():
    for option in playerConfig.options(player):
        if not playerConfig.getint(player, option):
            playerConfig.remove_option(player, option)
            changed = True
if changed:
    with open('players.ini', 'w') as configfile:
        playerConfig.write(configfile)
sortingList = []
for player in playerConfig.sections():
    sortingList.append([len(playerConfig.options(player)), player, playerConfig.options(player)])
sortingList.sort()
newPConfig = cp.ConfigParser()
for item in sortingList:
    newPConfig.add_section(item[1])
    item[2].sort()
    for option in item[2]:
        newPConfig.set(item[1], str(option), '1')
with open('players.ini', 'w') as configfile:
    newPConfig.write(configfile)
mapConfig = cp.ConfigParser()
try:
    mapConfig.read_file(open('maps.ini'))
except:
    showerror(title='Error', message='maps.ini not found. Please add maps.')
    mapConfig.read('maps.ini')
    main()
mapList = mapConfig.sections()
mapList.sort()
with open('maps.ini', 'w') as configfile:
    mapConfig.write(configfile)

# Second part of selecting agents function
def select_agents(select_win, playersCheckedVars):
    picked_win = tk.Toplevel(select_win)
    picked_win.resizable(False, False)
    picked_win.configure(bg='white')
    picked_win.title('Agents Selected')
    playersChecked = []
    counter = 0
    for player in playerConfig.sections(): # Creates a list of all player names
        if playersCheckedVars[counter].get():
            playersChecked.append(player)
        counter += 1
    if len(playersChecked) < 1:
        showerror(title='Error', message='Please select at least one player.')
        refresh()
    usedAgents = [] # List to prevent repeated agents
    output = []
    longestOutput = 0
    for player in playersChecked: # Selects and displays the random agent for each player
        random.seed(round(time.time() * 1000))
        picked = random.randint(1, len(playerConfig.options(player))) - 1
        infinite = 0
        while agents[picked] in usedAgents or not playerConfig.has_option(player, agents[picked].lower()):
            picked = random.randint(1, len(agentConfig.sections())) - 1
            infinite += 1
            if infinite > 1000000:
                showerror(title='Error', message='Failed to pick agents. Please try again.')
                refresh()
        usedAgents.append(agents[picked])
        newOutput = str(player) + ': ' + str(agents[picked]) + '\n'
        if len(newOutput) + 2 > longestOutput: # Updates longest output, +2 is for brackets
            longestOutput = len(newOutput) + 2
        output.append(newOutput)
        picked = -1
    text = tk.Text(picked_win, width=longestOutput, height=len(output))
    for ii in range(len(output)):
        line = str(ii + 1) + '.0'
        outputStep = output[ii].strip('{').strip('}')
        text.insert(line, outputStep) # Outputs selected agents in text fields
    text['state'] = 'disabled'
    text.pack(padx=5, pady=5)
    # Button to copy output to clipboard
    tk.Button(picked_win, text='Copy', command=lambda: copy(picked_win, text)).pack(pady=5)
    ttk.Separator(picked_win, orient='horizontal').pack(fill='x', pady=5)
    # Closes this window
    tk.Button(picked_win, text='Close', command=lambda: picked_win.destroy()).pack(pady=5)

# Copies everything in the text field to clipboard
def copy(picked_win, text):
    picked_win.clipboard_clear()
    picked_win.clipboard_append(text.get('1.0', 'end').strip('\n\n'))
    picked_win.update()

# Selects a random map
def select_map(window):
    maps = []
    for map in mapConfig.sections():
        maps.append(map)
    random.seed(round(time.time() * 1000))
    map = random.randint(1, len(maps)) - 1
    showinfo(title='Map Selection', message=f'Selected map: {maps[map]}')

# First part of adding agents to a player
def add_agent(window):
    add_a_win = tk.Toplevel(window)
    add_a_win.resizable(False, False)
    add_a_win.configure(bg='white')
    add_a_win.title('Add Agent(s) to Player')
    tk.Label(add_a_win, bg='white', text='Select a Player:').pack(padx=75, pady=5)
    selPlayer = tk.StringVar() # Selected player variable
    menu_button = tk.Menubutton(add_a_win, bg='grey75', disabledforeground='grey20', text='Click Here') # Dropdown list
    menu = tk.Menu(menu_button, tearoff=0)
    players = playerConfig.sections()
    for player in players: # Adds each player to the dropdown list
        # When a radiobutton is selected, it calls show_agents()
        menu.add_radiobutton(label=player, value=player, variable=selPlayer, command=lambda: show_agents(add_a_win, selPlayer.get(), menu_button))
    menu_button['menu'] = menu
    menu_button.pack(padx=50, pady=5)

# This shows each of the agents. I figured out the other way that I used for the players
# later on after a couple hours of trial and error, but I already wrote it this way
# and it works so I don't want to change it until I have a reason to.
def show_agents(add_win, player, menu_button):
    menu_button['state'] = 'disabled'
    menu_button['text'] = player
    ttk.Separator(add_win, orient='horizontal').pack(fill='x', pady=5)
    agentsCheckedVars = []
    counter = 0
    for agent in agentConfig.sections(): # Creates a list of tk variables
        if playerConfig.has_option(player, agent):
            agentCheckVars = tk.IntVar(add_win, playerConfig.getint(player, agent))
        else:
            agentCheckVars = tk.IntVar(add_win, 0)
        agentsCheckedVars.append([agents[counter], agentCheckVars])
        counter += 1
    counter = 0
    for agent in agentConfig.sections(): # Displays a checkbox for each player
        tk.Checkbutton(add_win, text=agent, variable=agentsCheckedVars[counter][1], onvalue=1, offvalue=0).pack()
        counter += 1
    # Saves player name and agents to config file
    tk.Button(add_win, text='Save', command=lambda: a_config(add_win, player, agentsCheckedVars)).pack(pady=5)

# Function to specifically add agents to players
def a_config(add_a_win, player, agentsCheckedVars):
    for agent in agentsCheckedVars:
        # Adds every agent (and value, could be 0 for not having the agent) to each player
        playerConfig.set(player, agent[0], str(agent[1].get()))
    with open('players.ini', 'w') as configfile: # Write to the config file
        playerConfig.write(configfile)
    # Closes the toplevel window
    refresh()

# Function to add a player and their unlocked agents to the player config file
def add_player(window):
    add_win = tk.Toplevel(window)
    add_win.resizable(False, False)
    add_win.configure(bg='white')
    add_win.title('Add New Player')
    tk.Label(add_win, bg='white', text='Player Name:').pack(pady=5) # Label for input field
    entryName = tk.StringVar() # For taking player's name as input
    intake = tk.Entry(add_win, textvariable=entryName, width=40)
    intake.pack(padx=10, pady=5) # Text entry field
    ttk.Separator(add_win, orient='horizontal').pack(fill='x', pady=5)
    tk.Label(add_win, bg='white', text='Select this Player\'s Unlocked Agents:').pack(pady=5)
    agentsCheckedVars = []
    for ii in range(len(agentConfig.sections())): # Creates a list of tk variables
        if ii == 2 or ii == 5 or ii == 9 or ii == 10 or ii == 12:
            agentCheckVars = tk.IntVar(add_win, 1)
        else:
            agentCheckVars = tk.IntVar(add_win, 0)
        agentsCheckedVars.append(agentCheckVars)
    counter = 0
    for agent in agentConfig.sections(): # Displays a checkbox for each player
        tk.Checkbutton(add_win, text=agent, variable=agentsCheckedVars[counter], onvalue=1, offvalue=0).pack()
        counter += 1
    # Saves player name and agents to config file
    tk.Button(add_win, text='Save', command=lambda: p_config(add_win, intake, agentsCheckedVars)).pack(pady=5)
    ttk.Separator(add_win, orient='horizontal').pack(fill='x', pady=5)
    tk.Button(add_win, text='Back', command=lambda: add_win.destroy()).pack(pady=5)

# Appends new section to the player config file
def p_config(add_win, intake, agentsCheckedVars):
    agentsChecked = []
    counter = 0
    for agent in agentConfig.sections(): # Creates a list of all player names
        if agentsCheckedVars[counter].get():
            agentsChecked.append(agent)
        counter += 1
    name = intake.get() # Retrieves string from variable
    if playerConfig.has_section(name): # If player exists in config file, close window
        showerror(title='Error', message='Player already exists.')
        add_win.destroy()
        return
    playerConfig_add = cp.ConfigParser()
    playerConfig_add.add_section(name)
    for agent in agentsChecked: # creates the section in a new config instance
        playerConfig_add.set(name, agent, '1')
    with open('players.ini', 'a') as configfile: # Appends the new instance to config file
        playerConfig_add.write(configfile)
    # Destroy toplevel window and refresh
    add_win.destroy()
    refresh()

# For adding a new agent to the agent config file
def new_agent(window):
    new_win = tk.Toplevel(window)
    new_win.resizable(False, False)
    new_win.configure(bg='white')
    new_win.title('Add New Agent')
    tk.Label(new_win, bg='white', text='Agent Name:').pack(pady=5) # Label for input field
    entryName = tk.StringVar() # For taking player's name as input
    intake = tk.Entry(new_win, textvariable=entryName, width=40)
    intake.pack(padx=10, pady=5) # Text entry field
    tk.Button(new_win, text='Save', command=lambda: a_n_config(new_win, intake)).pack(pady=5)
    ttk.Separator(new_win, orient='horizontal').pack(fill='x', pady=5)
    tk.Button(new_win, text='Back', command=lambda: new_win.destroy()).pack(pady=5)

# Appends new section to agent config file
def a_n_config(new_win, intake):
    name = intake.get()
    if agentConfig.has_section(name): # If agent exists in config file, close window
        showerror(title='Error', message='Agent already exists.')
        new_win.destroy()
        return
    agentConfig_add = cp.ConfigParser()
    agentConfig_add.add_section(name)
    with open('agents.ini', 'a') as configfile:
        agentConfig_add.write(configfile)
    new_win.destroy()
    refresh()

# Adds new map to map config file
def new_map(window):
    new_win = tk.Toplevel(window)
    new_win.resizable(False, False)
    new_win.configure(bg='white')
    new_win.title('Add New Map')
    tk.Label(new_win, bg='white', text='Map Name:').pack(pady=5) # Label for input field
    entryName = tk.StringVar() # For taking player's name as input
    intake = tk.Entry(new_win, textvariable=entryName, width=40)
    intake.pack(padx=10, pady=5) # Text entry field
    tk.Button(new_win, text='Save', command=lambda: m_config(new_win, intake)).pack(pady=5)
    ttk.Separator(new_win, orient='horizontal').pack(fill='x', pady=5)
    tk.Button(new_win, text='Back', command=lambda: new_win.destroy()).pack(pady=5)

# Appends new section to map config file
def m_config(new_win, intake):
    name = intake.get()
    if mapConfig.has_section(name): # If map exists in config file, close window
        showerror(title='Error', message='Map already exists.')
        new_win.destroy()
        return
    mapConfig_add = cp.ConfigParser()
    mapConfig_add.add_section(name)
    with open('maps.ini', 'a') as configfile:
        mapConfig_add.write(configfile)
    new_win.destroy()
    refresh()

# Refreshes the window by using execv to run the program again
def refresh():
    os.execv(sys.executable, ['python3'] + sys.argv)

# Closes the window and exits the program
def close(window):
    window.destroy()
    exit()


def main():
    # GUI
    window = tk.Tk()
    window.resizable(False, False)
    window.configure(bg='white')
    window.title('Random Agent Selector')
    # Config
    if playerConfig.sections() and agentConfig.sections():
        # Buttons
        xPadding = 100 # Makes adjusting window sizing easier
        tk.Label(window, bg='white', text='Select current players:').pack(padx=xPadding, pady=5)
        playersCheckedVars = []
        for ii in range(len(playerConfig.sections())): # Creates a list of tk variables
            playerCheckVars = tk.IntVar(window, 0)
            playersCheckedVars.append(playerCheckVars)
        counter = 0
        for player in playerConfig.sections(): # Displays a checkbox for each player
            tk.Checkbutton(window, bg='white', text=player, variable=playersCheckedVars[counter], onvalue=1, offvalue=0).pack()
            counter += 1
        tk.Button(window, text='Select Agents', command=lambda: select_agents(window, playersCheckedVars)).pack(padx=50, pady=5)
        ttk.Separator(window, orient='horizontal').pack(fill='x', pady=5)
    if mapConfig.sections():
        tk.Button(window, text='Select Map', command=lambda: select_map(window)).pack(padx=50, pady=5)
        ttk.Separator(window, orient='horizontal').pack(fill='x', pady=5)
    if playerConfig.sections() and agentConfig.sections():
        tk.Button(window, text='Add Agent to Player', command=lambda: add_agent(window)).pack(padx=xPadding, pady=5)
        ttk.Separator(window, orient='horizontal').pack(fill='x', pady=5)
    tk.Button(window, text='Add New Player', command=lambda: add_player(window)).pack(padx=xPadding, pady=5)
    ttk.Separator(window, orient='horizontal').pack(fill='x', pady=5)
    tk.Button(window, text='Add New Agent', command=lambda: new_agent(window)).pack(padx=xPadding, pady=5)
    ttk.Separator(window, orient='horizontal').pack(fill='x', pady=5)
    tk.Button(window, text='Add New Map', command=lambda: new_map(window)).pack(padx=xPadding, pady=5)
    ttk.Separator(window, orient='horizontal').pack(fill='x', pady=5)
    tk.Button(window, text='Exit', command=lambda: close(window)).pack(padx=xPadding, pady=5)

    # Show window
    window.mainloop()


if __name__ == '__main__':
    main()