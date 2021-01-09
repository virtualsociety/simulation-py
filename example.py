'''
Main script VS DES

By Dr. Raymond Hoogendoorn
Copyright 2020
'''

from random import randint
import simpy

#Config
TALKS_PER_SESSION = 3
TALK_LENGTH = 30
BREAK_LENGTH = 15
ATTENDEES = 10

def attendee(env, name, knowledge=0, hunger=0):
   talks =0
   breaks =0
   #Repeat sessions
   while True:
      # Visit talks
      for i in range(TALKS_PER_SESSION):
          print('Talk {0} begins at {1}'.format(talks+1, env.now))
          knowledge += randint(0, 3) / (1 + hunger)
          hunger += randint(1, 4)
          talks += 1
          yield env.timeout(TALK_LENGTH)
      print(f'Talk {talks} ends at {env.now}')
      print('Attendee %s finished talks with knowledge %.2f and hunger ' '%.2f' %( name, knowledge, hunger))

# Run Simulation
env = simpy.Environment()
for i in range(ATTENDEES):
   env.process(attendee(env, i))
env.run(until=250)