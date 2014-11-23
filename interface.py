import text_interface as interface
import puzzle
import sys
import os

def run():
	interface.welcomeWorld()
	interface.about()
	userName = interface.getName()
	lvl = interface.beginAdventure()
	#puzzle.play_level(lvl)
	interface.completedTasks()

def main():
	run()

if __name__ == '__main__':
  main()