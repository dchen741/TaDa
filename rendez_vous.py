import puzzle

def main():
  # def __init__(self, title, lesson, lines, code, answer):
  p = puzzle.Puzzle("Rendez-vous",
                    "In this puzzle, we must ensure that both threads execute their first statement before either's second is run.",
                    ['  a1done.signal()', '  a1done.wait()', '  b1done.signal()', '  b1done.wait()'],
                    "Thread A:\n  statement a1\n  statement a2\n\nThread B:\n  statement b1\n  statement b2",
                    "Thread A:\n  statement a1\n  a1done.signal()\n  b1done.wait()\n  statement a2\n\nThread B:\n  statement b1\n  b1done.signal()\n  a1done.wait()\n  statement b2",
                    )
  p.start_puzzle()

if __name__ == '__main__':
  main()
