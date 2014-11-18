import textInterface
import puzzle
import sys
import os

def run():
	textInterface.welcomeWorld()
	textInterface.about()
	userName = textInterface.getName()
	lvl = textInterface.beginAdventure()
	#puzzle.play_level(lvl)
	textInterface.completedTasks()

def main():
	run()

if __name__ == '__main__':
  main()