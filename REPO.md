Activities:
4a and 4b: Made a pre-commit git hook with the contents -
#!/bin/sh
python3.9 ~/TJN0012-SQA2023-AUBURN/KubeSec-master/fuzz.py
bandit -r ~/TJN0012-SQA2023-AUBURN/KubeSec-master > bandit-report.csv
exit 0
This runs whenever a commit is made and runs bandit on the repository and runs the fuzzing program I made. The fuzzing program works by throwing various good and bad values at methods in scanner.py to test for errors. None were found.

4c: I used the same myLogger.py from workshop 8 and implemented the logging within the methods in the same manner. This was done in parser.py

Lessons Learned: I learned that using ">" in the command line writes to an output file, and having anysort of tab/whitespace before the #!/bin/sh will break the hook.
