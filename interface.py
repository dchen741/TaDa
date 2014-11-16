import textInterface
import sys
import os

def run():
	textInterface.welcomeWorld()
	textInterface.about()
	userName = textInterface.getName()
	textInterface.beginAdventure()
	textInterface.completedTasks()

def main():
	run()

if __name__ == '__main__':
  main()