import startapp
import lifecounter

# Can I leave this outside the start app?
print('Welcome to the Guess Game App!', '\n')

# Load lives from file
# If it fails for whatever reason - no problem!
# the exception will be caught, the default value will be used and the application will continue
lifecounter.LifeCounter.loadLivesFromFile()

# Start the game
startapp.StartApp.startGame()

# TO DO

# make sure the app runs if the settings file is absent, ie a default lives value is used
# run continuously with new numbers every time
# have the lives remaining in the bottom + show lives before the user guess
# Add restart
# Add scores! Lose them if you run out of lives