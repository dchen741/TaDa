from puzzle import Puzzle
import simulator

rendez_vous_p = Puzzle("Rendez-vous",
                "Alice and Bob are going to the amusement park. They intend to meet at the gate and enter together. You can use 'alice.signal()' to signal alice's arrival, and 'alice.wait()' to wait until alice has signaled her arrival. The same is true for 'bob.signal()' and 'bob.wait()'. Add these lines to the given code to ensure neither will enter the park without the other.",
                ['  alice.signal()', '  alice.wait()', '  bob.signal()', '  bob.wait()'],
                "Thread Alice:\n  Alice arrives\n  Alice enters the park\n\nThread Bob:\n  Bob arrives\n  Bob enters the park",
                "Thread Alice:\n  Alice arrives\n  alice.signal()\n  bob.wait()\n  Alice enters the park\n\nThread Bob:\n  Bob arrives\n  bob.signal()\n  alice.wait()\n  Bob enters the park",
                )

def main():
  rendez_vous_p.start_puzzle()
  #rendez_vous_p.run_code("one", "two")

if __name__ == '__main__':
  main()
