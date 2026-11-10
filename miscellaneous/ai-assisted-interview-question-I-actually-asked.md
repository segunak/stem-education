# AI-Assisted Interview Question I Actually Asked

In September 2026 I was voluntold by Microsoft recruiting to help out with internship interviews for Summer 2027. I obliged, and had some fun with it, specifically because they told me I could choose to turn on the [HackerRank AI-Assisted Interview Tool](https://support.hackerrank.com/articles/5821380141-ai-assisted-interviews) if I wanted to.

I turned it on for the 2 students I interviewed. Here's the question I asked. They had an AI chat window the whole time that was locked down to provide guidance but not the outright answer. And I could see what they sent and got back, so the whole chat was visible to me. Also, if they clicked off to a different tab, the HackerRank system alerted me to that, so I could also tell if they were trying to cheat in any way. It's actually a pretty nifty tool.

## The Last Seat In Class

### Description

A coding agent wrote a pull request for the class registration system of a school.

**The problem.** A class has one free seat. Two students click Register at the same time. The system puts the two students in the class. Now the class has more students than seats.

**The message from the agent.** "I repaired the problem. Each request now waits a different time before it starts. Now two requests do not occur at the same time. The test passes each time."

The test uses two threads. The threads make the two students register at the same time.

**The code has four parts.**

1. **Settings.** You can change these values to do tests.
2. **The database.** This part is correct. Do not change it.
3. **The pull request.** This is the code that the agent changed. Review this part.
4. **The test.** You can change the test or add more tests.

### Your Tasks

1. Do you approve this pull request? Tell me why or why not.
2. If you do not approve it, show that the problem can still occur. You can change the test or the values.
3. Make the code correct.

Tell me your ideas while you work. You can use the AI Assistant.

### Code Area

```python
import threading
import time

# ==================================================================
# PART 1. SETTINGS
# You can change these values to do tests.
# ==================================================================

SAVE_SECONDS = 0.01  # One save to the database takes 0.01 seconds (10 milliseconds).


# ==================================================================
# PART 2. THE DATABASE
# This part is correct. Do not change it.
# It acts like a real database. A real save takes some time.
# ==================================================================

seats_left = 1  # The class has one free seat.
enrolled = []   # The students in the class.


def save_to_database(student):
    time.sleep(SAVE_SECONDS)  # A real save takes some time.
    enrolled.append(student)


# ==================================================================
# PART 3. THE PULL REQUEST
# This is the code that the agent changed. Review this part.
# ==================================================================

def register(student, request_number):
    global seats_left

    # The agent added this line. Each request waits before it starts.
    # Request 0 waits 0 seconds. Request 1 waits 0.1 seconds.
    time.sleep(request_number * 0.1)

    if seats_left > 0:               # Step 1. Check for a free seat.
        save_to_database(student)    # Step 2. Save the student. This takes some time.
        seats_left = seats_left - 1  # Step 3. Take the seat.


# ==================================================================
# PART 4. THE TEST
# You can change this test or add more tests.
# ==================================================================

def test_last_seat():
    global seats_left
    seats_left = 1
    enrolled.clear()

    # Two students click Register at the same time. The class has one free seat.
    ana = threading.Thread(target=register, args=("Ana", 0))
    ben = threading.Thread(target=register, args=("Ben", 1))
    ana.start()  # start() starts each thread. The two threads run at the same time.
    ben.start()
    ana.join()   # join() waits until each thread stops.
    ben.join()

    print("Enrolled:", enrolled, "| Seats left:", seats_left)
    assert len(enrolled) == 1, "Too many students are in the class."
    print("PASS")


test_last_seat()
```

### What Running the Code Prints

```text
Enrolled: ['Ana'] | Seats left: 0
PASS
```

## Answer Key (Not Visible to Student)

**The main idea.** A registration has three steps. Step 1 checks for a free seat. Step 2 saves the student, and that takes time. Step 3 takes the seat. During step 2, a second student can find the same free seat.

The wait from the agent does not stop this problem. The wait only makes the test pass.

### What the Line From the Agent Does

- `SAVE_SECONDS` is the time for one mock save. It is 0.01 seconds, or 10 milliseconds.
- Ben is request 1, so he waits 0.1 seconds before step 1. The save for Ana takes only 0.01 seconds. The registration for Ana is complete before Ben starts. That is the only reason that the test passes.
- The wait does not stop two registrations at the same time. The wait works only when the save is faster than the wait.

### Ways to Show the Problem Still Occurs

1. **A slow database.** In part 1, change `SAVE_SECONDS` to `0.2`. Now the save for Ana takes more time than the wait for Ben. Ben does step 1 while Ana is in step 2. Ben finds a free seat. The two students go into the class, and the test fails.
2. **The same number.** In part 4, give request number `0` to the two students. This occurs when two web servers each start to count at 0. No request waits, and the two students go into the class.
3. **Slow for all users.** Request 500 waits 50 seconds. On registration day, thousands of students register. That wait is not acceptable, even when the result is correct.

### The Correct Code

Change only part 3. Remove the line that the agent added. Put a lock around steps 1, 2, and 3. The lock lets only one student at a time do the three steps.

```python
lock = threading.Lock()


def register(student, request_number):
    global seats_left
    with lock:  # Only one thread at a time can do the steps in this block.
        if seats_left > 0:               # Step 1. Check for a free seat.
            save_to_database(student)    # Step 2. Save the student. This takes some time.
            seats_left = seats_left - 1  # Step 3. Take the seat.
```

Now the test passes when `SAVE_SECONDS` is `0.2`. The test also passes when the two students have request number `0`.

## Follow Up Questions for the Student

1. "A real system has many servers. Does your lock work on many servers?" No. A lock works only in one program. The database must do steps 1 and 3 in one operation. An example is `UPDATE classes SET seats_left = seats_left - 1 WHERE id = 'CS101' AND seats_left > 0`. If the database changes no row, the class is full.
2. "The agent now agrees with you. If you told the agent that the lock was wrong, the agent can agree with that too. How do you know which answer is correct?" Do not accept an answer only because the agent agrees. Write a test that fails before the repair and passes after the repair. The test is the proof.
3. "Is a sleep ever useful here?" Yes, to find the problem. Make `SAVE_SECONDS` larger. Then the problem occurs each time. A sleep can help you find a problem. A sleep does not repair a problem.

## Hints to Help the Student If Stuck

1. "Part 2 is correct. The problem is in part 3."
2. "What occurs if the save takes more time?"
3. "What occurs if two requests have the same number?"

## Grading Rubric

In terms of stars. 5 is the highest.

- **4 or 5** Does not approve the PR. Tells me about the gap between step 1 and step 3. Shows the problem with a test. Adds a lock and removes the sleep. Knows the database answer for many servers.
- **3** Thinks that the sleep is wrong. Adds a lock with some help.
- **2 or 1** Approves the pull request, or makes the wait longer.
