import puzzle

def main():
  # def __init__(self, title, lesson, prompt, code, answer):
  p = puzzle.Puzzle("Hello World Puzzle",
                    "This bit explains the concepts.",
                    "Where would you put 'print 'hello world!'?",
                    "print 'ahoy'\nprint 'yahoo'",
                    "print 'ahoy'\nprint 'hello world!'\nprint 'yahoo'",
                    )
  p.start_puzzle()

if __name__ == '__main__':
  main()