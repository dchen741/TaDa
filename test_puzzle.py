import puzzle

p = puzzle.Puzzle("Hello World Puzzle",
                "This bit explains the concepts.",
                "Where would you put 'print 'hello world!'?",
                "print 'ahoy'\nprint 'yahoo'",
                "print 'ahoy'\nprint 'hello world!'\nprint 'yahoo'",
                )

def main():
  # def __init__(self, title, lesson, prompt, code, answer):
  p.start_puzzle()

if __name__ == '__main__':
  main()