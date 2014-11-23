import puzzle

def main():
  # def __init__(self, title, lesson, prompt, code, answer):
  p = puzzle.Puzzle("Hello World Puzzle",
                    "This bit explains the concepts.",
                    "Where would you put 'print 'hello world!'?",
                    "1 print 'ahoy'\n2 print 'yahoo'",
                    "print 'ahoy'\nprint 'hello world!'\nprint 'yahoo'",
                    )
  p.start_puzzle()

if __name__ == '__main__':
  main()