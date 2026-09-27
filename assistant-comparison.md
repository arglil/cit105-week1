# Assistant Comparison Report

Task
I gave GitHub Copilot and Claude Code the same task: build a Python password checker. A strong password needs at least 8 characters, an uppercase letter, a lowercase letter, a number and a special character. The checker had to tell the user what was missing. I used the exact same prompt for both so the comparison would be fair.
GitHub Copilot
Copilot wrote 58 lines of code right inside PyCharm. It added a few extra helper and alias functions, even though I only asked for one function. When I tested "hello", it said the password was missing length, an uppercase letter, a number and a special character. When I tested "Hello123!", it said the password was strong.
Claude Code
Claude Code also wrote a 58-line file. Its main function, check_password_strength(), lists which requirements a password is missing. It also added is_strong() for a yes/no answer and report() for a readable message. It added three things I didn't ask for: hidden typing when you enter a password, a loop that keeps asking for new passwords, and a quick check of five sample passwords. When I said I wanted to test it, it wrote 10 tests, and all 10 passed.
My Comparison
Copilot was faster because it worked inside PyCharm and I could test the code right away. Claude needed more review because I had to check its extra features and the 10 tests. For a small task like this, I would use Copilot again because it was quick and simple. Claude would be the better choice if I needed more testing.