'''Random Agent Selector by Cael Shoop.'''

import tkinter as tk # GUI
from tkinter.messagebox import showerror, showinfo
import random # random number selector for choosing agents
import configparser as cp # Saving player info in .ini config file

# Global list of Valorant agents
agents = ['Astra', 'Breach', 'Brimstone', 'Chamber', 'Cypher',
          'Jett', 'Kay/O', 'Killjoy', 'Omen', 'Phoenix', 'Sage',
          'Skye', 'Sova', 'Raze', 'Reyna', 'Viper', 'Yoru']

# First part of the selecting agents function
def generate(window, config):
    select_win = tk.Toplevel(window) # New toplevel window
    select_win.resizable(True, True)
    select_win.geometry('300x300')
    select_win.title('Agent Selections')
    playersCheckedVars = []
    for ii in range(len(config.sections())): # Creates a list of tk variables
        playerCheckVars = tk.IntVar(select_win, 0)
        playersCheckedVars.append(playerCheckVars)
    counter = 0
    for player in config.sections(): # Displays a checkbox for each player
        tk.Checkbutton(select_win, text=player, variable=playersCheckedVars[counter], onvalue=1, offvalue=0).pack()
        counter += 1
    # Button that initializes selection. This can be used multiple times without closing this window
    tk.Button(select_win, text='Select Agents', command=lambda: select(select_win, playersCheckedVars, config)).pack()
    tk.Button(select_win, text='Back', command=lambda: select_win.destroy()).pack()

# Second part of selecting agents function
def select(select_win, playersCheckedVars, config):
    picked_win = tk.Toplevel(select_win)
    picked_win.resizable(True, True)
    picked_win.geometry('300x300')
    picked_win.title('Agents Selected')
    playersChecked = []
    counter = 0
    for player in config.sections(): # Creates a list of the selected player names
        if playersCheckedVars[counter].get():
            playersChecked.append(player)
        counter += 1
    usedAgents = [] # List to prevent repeated agents
    picked = -1
    for player in playersChecked: # Selects and displays the random agent for each player
        while agents[picked] in usedAgents or not config.has_option(player, agents[picked]):
            picked = random.randint(1, len(config.options(player)))
        usedAgents.append(agents[picked])
        output = str(player) + ': ' + str(agents[picked])
        picked = -1
        text = tk.Text(picked_win, height=1)
        text.insert('1.0', output) # Outputs selected agents in text fields
        text['state'] = 'disabled'
        text.pack()
    # Closes this window
    tk.Button(picked_win, text='Close', command=lambda: picked_win.destroy()).pack()

# First part of adding agents to a player
def add_agent(window, players, config):
    add_a_win = tk.Toplevel(window)
    add_a_win.geometry('300x525')
    add_a_win.title('Add Agent(s) to Player')
    tk.Label(add_a_win, text='Select a Player:').pack()
    selPlayer = tk.StringVar() # Selected player variable
    menu_button = tk.Menubutton(add_a_win, text='Click Here') # Dropdown list
    menu = tk.Menu(menu_button, tearoff=0)
    for player in players: # Adds each player to the dropdown list
        # When a radiobutton is selected, it calls show_agents()
        menu.add_radiobutton(label=player, value=player, variable=selPlayer, command=lambda: show_agents(add_a_win, selPlayer.get(), config))
    menu_button['menu'] = menu
    menu_button.pack()
    tk.Button(add_a_win, text='Back', command=lambda: add_a_win.destroy()).pack()

# This shows each of the agents. I figured out the other way that I used for the players
# later on after a couple hours of trial and error, but I already wrote it this way
# and it works so I don't want to change it until I have a reason to.
def show_agents(add_win, player, config):
    agentsChecked = [] # If an agent is checked, they are added to the list
    if config.has_option(player, agents[0]): # If the player has the agent in the .ini
        # Put that value into the agent variable
        astra = tk.IntVar(add_win, config.getint(player, agents[0]))
    else:
        # Put a value of 0 into the agent variable
        astra = tk.IntVar(add_win, 0)
    tk.Checkbutton(add_win, text=agents[0], variable=astra, onvalue=1, offvalue=0, command=lambda: agentsChecked.append([agents[0], astra.get()])).pack()
    if config.has_option(player, agents[1]):
        breach = tk.IntVar(add_win, config.getint(player, agents[1]))
    else:
        breach = tk.IntVar(add_win, 0)
    tk.Checkbutton(add_win, text=agents[1], variable=breach, onvalue=1, offvalue=0, command=lambda: agentsChecked.append([agents[1], breach.get()])).pack()
    if config.has_option(player, agents[2]):
        brimstone = tk.IntVar(add_win, config.getint(player, agents[2]))
    else:
        brimstone = tk.IntVar(add_win, 0)
    tk.Checkbutton(add_win, text=agents[2], variable=brimstone, onvalue=1, offvalue=0, command=lambda: agentsChecked.append([agents[2], brimstone.get()])).pack()
    if config.has_option(player, agents[3]):
        chamber = tk.IntVar(add_win, config.getint(player, agents[3]))
    else:
        chamber = tk.IntVar(add_win, 0)
    tk.Checkbutton(add_win, text=agents[3], variable=chamber, onvalue=1, offvalue=0, command=lambda: agentsChecked.append([agents[3], chamber.get()])).pack()
    if config.has_option(player, agents[4]):
        cypher = tk.IntVar(add_win, config.getint(player, agents[4]))
    else:
        cypher = tk.IntVar(add_win, 0)
    tk.Checkbutton(add_win, text=agents[4], variable=cypher, onvalue=1, offvalue=0, command=lambda: agentsChecked.append([agents[4], cypher.get()])).pack()
    if config.has_option(player, agents[5]):
        jett = tk.IntVar(add_win, config.getint(player, agents[5]))
    else:
        jett = tk.IntVar(add_win, 0)
    tk.Checkbutton(add_win, text=agents[5], variable=jett, onvalue=1, offvalue=0, command=lambda: agentsChecked.append([agents[5], jett.get()])).pack()
    if config.has_option(player, agents[6]):
        kayo = tk.IntVar(add_win, config.getint(player, agents[6]))
    else:
        kayo = tk.IntVar(add_win, 0)
    tk.Checkbutton(add_win, text=agents[6], variable=kayo, onvalue=1, offvalue=0, command=lambda: agentsChecked.append([agents[6], kayo.get()])).pack()
    if config.has_option(player, agents[7]):
        killjoy = tk.IntVar(add_win, config.getint(player, agents[7]))
    else:
        killjoy = tk.IntVar(add_win, 0)
    tk.Checkbutton(add_win, text=agents[7], variable=killjoy, onvalue=1, offvalue=0, command=lambda: agentsChecked.append([agents[7], killjoy.get()])).pack()
    if config.has_option(player, agents[8]):
        omen = tk.IntVar(add_win, config.getint(player, agents[8]))
    else:
        omen = tk.IntVar(add_win, 0)
    tk.Checkbutton(add_win, text=agents[8], variable=omen, onvalue=1, offvalue=0, command=lambda: agentsChecked.append([agents[8], omen.get()])).pack()
    if config.has_option(player, agents[9]):
        phoenix = tk.IntVar(add_win, config.getint(player, agents[9]))
    else:
        phoenix = tk.IntVar(add_win, 0)
    tk.Checkbutton(add_win, text=agents[9], variable=phoenix, onvalue=1, offvalue=0, command=lambda: agentsChecked.append([agents[9], phoenix.get()])).pack()
    if config.has_option(player, agents[10]):
        sage = tk.IntVar(add_win, config.getint(player, agents[10]))
    else:
        sage = tk.IntVar(add_win, 0)
    tk.Checkbutton(add_win, text=agents[10], variable=sage, onvalue=1, offvalue=0, command=lambda: agentsChecked.append([agents[10], sage.get()])).pack()
    if config.has_option(player, agents[11]):
        skye = tk.IntVar(add_win, config.getint(player, agents[11]))
    else:
        skye = tk.IntVar(add_win, 0)
    tk.Checkbutton(add_win, text=agents[11], variable=skye, onvalue=1, offvalue=0, command=lambda: agentsChecked.append([agents[11], skye.get()])).pack()
    if config.has_option(player, agents[12]):
        sova = tk.IntVar(add_win, config.getint(player, agents[12]))
    else:
        sova = tk.IntVar(add_win, 0)
    tk.Checkbutton(add_win, text=agents[12], variable=sova, onvalue=1, offvalue=0, command=lambda: agentsChecked.append([agents[12], sova.get()])).pack()
    if config.has_option(player, agents[13]):
        raze = tk.IntVar(add_win, config.getint(player, agents[13]))
    else:
        raze = tk.IntVar(add_win, 0)
    tk.Checkbutton(add_win, text=agents[13], variable=raze, onvalue=1, offvalue=0, command=lambda: agentsChecked.append([agents[13], raze.get()])).pack()
    if config.has_option(player, agents[14]):
        reyna = tk.IntVar(add_win, config.getint(player, agents[14]))
    else:
        reyna = tk.IntVar(add_win, 0)
    tk.Checkbutton(add_win, text=agents[14], variable=reyna, onvalue=1, offvalue=0, command=lambda: agentsChecked.append([agents[14], reyna.get()])).pack()
    if config.has_option(player, agents[15]):
        viper = tk.IntVar(add_win, config.getint(player, agents[15]))
    else:
        viper = tk.IntVar(add_win, 0)
    tk.Checkbutton(add_win, text=agents[15], variable=viper, onvalue=1, offvalue=0, command=lambda: agentsChecked.append([agents[15], viper.get()])).pack()
    if config.has_option(player, agents[16]):
        yoru = tk.IntVar(add_win, config.getint(player, agents[16]))
    else:
        yoru = tk.IntVar(add_win, 0)
    tk.Checkbutton(add_win, text=agents[16], variable=yoru, onvalue=1, offvalue=0, command=lambda: agentsChecked.append([agents[16], yoru.get()])).pack()
    # Saves the configuration. This includes adding and removing agents from players.
    tk.Button(add_win, text='Save', command=lambda: a_config(add_win, player, agentsChecked, config)).pack()

# Function to specifically add agents to players
def a_config(add_a_win, player, selAgents, config):
    for agent in selAgents:
        # Adds every agent (and value, could be 0 for not having the agent) to each player
        config.set(player, agent[0], str(agent[1]))
    with open('players.ini', 'w') as configfile: # Write to the config file
        config.write(configfile)
    # Reminds the user to refresh the main window to reload config file
    showinfo(title='Add Successful', message='Please Refresh.')
    # Closes the toplevel window
    add_a_win.destroy()

# Function to add a player and their unlocked agents to the config file
def add_player(window, config):
    entryName = tk.StringVar() # For taking player's name as input
    add_win = tk.Toplevel(window)
    add_win.geometry('500x525')
    add_win.title('Add New Player')
    tk.Label(add_win, text='Player Name:').pack() # Label for input field
    intake = tk.Entry(add_win, textvariable=entryName, width=40)
    intake.pack() # Text entry field
    if config.has_section(intake.get()): # If player exists in config file, close window
        showerror(title='Error', message='Player already exists.')
        add_win.destroy()
        return
    tk.Label(add_win, text='Select this Player\'s Unlocked Agents:').pack()
    agentsChecked = []
    # Checkbox variables (some agents are unlocked by default)
    astra = tk.IntVar(add_win, 0)
    breach = tk.IntVar(add_win, 0)
    brimstone = tk.IntVar(add_win, 1)
    chamber = tk.IntVar(add_win, 0)
    cypher = tk.IntVar(add_win, 0)
    jett = tk.IntVar(add_win, 1)
    kayo = tk.IntVar(add_win, 0)
    killjoy = tk.IntVar(add_win, 0)
    omen = tk.IntVar(add_win, 0)
    phoenix = tk.IntVar(add_win, 1)
    sage = tk.IntVar(add_win, 1)
    skye = tk.IntVar(add_win, 0)
    sova = tk.IntVar(add_win, 1)
    raze = tk.IntVar(add_win, 0)
    reyna = tk.IntVar(add_win, 0)
    viper = tk.IntVar(add_win, 0)
    yoru = tk.IntVar(add_win, 0)
    # Checkboxes
    tk.Checkbutton(add_win, text=agents[0], variable=astra, onvalue=1, offvalue=0, command=lambda: agentsChecked.append([agents[0], astra.get()])).pack()
    tk.Checkbutton(add_win, text=agents[1], variable=breach, onvalue=1, offvalue=0, command=lambda: agentsChecked.append([agents[1], breach.get()])).pack()
    tk.Checkbutton(add_win, text=agents[2], variable=brimstone, onvalue=1, offvalue=0, command=lambda: agentsChecked.append([agents[2], brimstone.get()])).pack()
    tk.Checkbutton(add_win, text=agents[3], variable=chamber, onvalue=1, offvalue=0, command=lambda: agentsChecked.append([agents[3], chamber.get()])).pack()
    tk.Checkbutton(add_win, text=agents[4], variable=cypher, onvalue=1, offvalue=0, command=lambda: agentsChecked.append([agents[4], cypher.get()])).pack()
    tk.Checkbutton(add_win, text=agents[5], variable=jett, onvalue=1, offvalue=0, command=lambda: agentsChecked.append([agents[5], jett.get()])).pack()
    tk.Checkbutton(add_win, text=agents[6], variable=kayo, onvalue=1, offvalue=0, command=lambda: agentsChecked.append([agents[6], kayo.get()])).pack()
    tk.Checkbutton(add_win, text=agents[7], variable=killjoy, onvalue=1, offvalue=0, command=lambda: agentsChecked.append([agents[7], killjoy.get()])).pack()
    tk.Checkbutton(add_win, text=agents[8], variable=omen, onvalue=1, offvalue=0, command=lambda: agentsChecked.append([agents[8], omen.get()])).pack()
    tk.Checkbutton(add_win, text=agents[9], variable=phoenix, onvalue=1, offvalue=0, command=lambda: agentsChecked.append([agents[9], phoenix.get()])).pack()
    tk.Checkbutton(add_win, text=agents[10], variable=sage, onvalue=1, offvalue=0, command=lambda: agentsChecked.append([agents[10], sage.get()])).pack()
    tk.Checkbutton(add_win, text=agents[11], variable=skye, onvalue=1, offvalue=0, command=lambda: agentsChecked.append([agents[11], skye.get()])).pack()
    tk.Checkbutton(add_win, text=agents[12], variable=sova, onvalue=1, offvalue=0, command=lambda: agentsChecked.append([agents[12], sova.get()])).pack()
    tk.Checkbutton(add_win, text=agents[13], variable=raze, onvalue=1, offvalue=0, command=lambda: agentsChecked.append([agents[13], raze.get()])).pack()
    tk.Checkbutton(add_win, text=agents[14], variable=reyna, onvalue=1, offvalue=0, command=lambda: agentsChecked.append([agents[14], reyna.get()])).pack()
    tk.Checkbutton(add_win, text=agents[15], variable=viper, onvalue=1, offvalue=0, command=lambda: agentsChecked.append([agents[15], viper.get()])).pack()
    tk.Checkbutton(add_win, text=agents[16], variable=yoru, onvalue=1, offvalue=0, command=lambda: agentsChecked.append([agents[16], yoru.get()])).pack()
    # Saves player name and agents to config file
    tk.Button(add_win, text='Save', command=lambda: p_config(add_win, intake, agentsChecked)).pack()
    tk.Button(add_win, text='Back', command=lambda: add_win.destroy()).pack()

# Appends new section to config file
def p_config(add_win, intake, selAgents):
    name = intake.get() # Retrieves string from variable
    config_add = cp.ConfigParser()
    config_add.add_section(name)
    for agent in selAgents: # creates the section in a new config instance
        config_add.set(name, agent[0], str(agent[1]))
    with open('players.ini', 'a') as configfile: # Appends the new instance to config file
        config_add.write(configfile)
    # Reminds user to refresh main window
    showinfo(title='Save Successful', message='Please Refresh.')
    # Closes toplevel window
    add_win.destroy()

# Refreshes the window by destroying the window and calling main again.
# Probably should not be used excessively, or RAM usage may climb noticeably
def refresh(window):
    window.destroy()
    main()

# Closes the window and exits the program
def close(window):
    window.destroy()
    exit()


def main():
    # GUI
    window = tk.Tk()
    window.resizable(True, True)
    window.geometry('500x300')
    window.title('Random Agent Selector')
    # Config
    config = cp.ConfigParser()
    config.read_file(open('players.ini'))
    if config.sections():
        # Buttons
        tk.Button(window, text='Generate', command=lambda: generate(window, config)).pack()
        tk.Button(window, text='Add Agent', command=lambda: add_agent(window, config.sections(), config)).pack()
        tk.Button(window, text='Add Player', command=lambda: add_player(window, config)).pack()
        tk.Button(window, text='Refresh', command=lambda: refresh(window)).pack()
        tk.Button(window, text='Exit', command=lambda: close(window)).pack()
    else:
        # Buttons
        tk.Button(window, text='Add Player', command=lambda: add_player(window)).pack()
        tk.Button(window, text='Refresh', command=lambda: refresh(window)).pack()
        tk.Button(window, text='Exit', command=lambda: close(window)).pack()

    # Show window
    window.mainloop()


if __name__ == '__main__':
    main()