from puzzle import Puzzle

test_puzzle_p = Puzzle("Hello World Puzzle",
                "This bit explains the concepts.",
                ["print 'hello world!'"],
                "print 'ahoy'\nprint 'yahoo'",
                "print 'ahoy'\nprint 'hello world!'\nprint 'yahoo'",
                )

def main():
  test_puzzle_p.start_puzzle()

if __name__ == '__main__':
  main()
