# Informational: Sending Skills to the Robot Dog

## The `sendSkillStr` Function

The `sendSkillStr` function is designed to send a specific skill command to the Petoi Robot, instructing it to perform a predefined action or movement. This function is part of the `PetoiRobot` module, which facilitates communication with the robot via serial commands.

## Parameters

- **skillStr** (str): This parameter is a string representing the skill command to be sent to the robot. Each skill corresponds to a specific action or movement that the robot can perform, such as sitting, standing, walking, or performing tricks like flips.
  
- **delayTime** (int): This parameter represents the delay time in milliseconds after the command is sent. The delay allows for proper execution timing of the skill, ensuring the robot has enough time to complete the action before receiving the next command.

## Usage Example

Here is an example of how to use the `sendSkillStr` function to make the robot sit:

```python
sendSkillStr("ksit", 1)
```

In this example:

- `"ksit"` is the skill command that instructs the robot to sit.
- `1` is the delay time in milliseconds, allowing the robot to execute the sit action for half a second before any other command is issued.

## Function Explanation

The `sendSkillStr` function sends a short skill string command to the robot via serial communication. This function uses the `send` function, which communicates with the robot's serial port, transmitting the skill command string and the specified delay time.

1. **Sending the Command**: The function calls the `send` function, passing the serial ports (`goodPorts`), the skill command string, and the delay time as a list.

2. **Delay Handling**: The delay time ensures that there is a proper interval between consecutive commands, allowing the robot to complete one action before starting another.

## Skills and Their Commands

Here is the list of all skills that can be sent using `sendSkillStr` and their corresponding commands. Each function is explained along with an example of its usage.

1. **Sit**: `ksit`
   - **Description**: Makes the robot sit down and delays for 1 second.
   - **Example**: `sendSkillStr("ksit", 1)`

2. **Stand Up**: `kup`
   - **Description**: Makes the robot stand up and delays for 1 second.
   - **Example**: `sendSkillStr("kup", 1)`

3. **Bottom Up**: `kbuttUp`
   - **Description**: Raises the robot's bottom and delays for 1 second.
   - **Example**: `sendSkillStr("kbuttUp", 1)`

4. **Stretch**: `kstr`
   - **Description**: Stretches the robot and delays for 1 second.
   - **Example**: `sendSkillStr("kstr", 1)`

5. **Rest**: `krest`
   - **Description**: Puts the robot in a resting position and delays for 1 second.
   - **Example**: `sendSkillStr("krest", 1)`

6. **Zero**: `kzero`
   - **Description**: Resets the robot to its default position and delays for 1 second.
   - **Example**: `sendSkillStr("kzero", 1)`

7. **Boxing**: `kbx`
   - **Description**: Makes the robot perform boxing movements and delays for 1 second.
   - **Example**: `sendSkillStr("kbx", 1)`

8. **Cheer**: `kchr`
   - **Description**: Makes the robot cheer and delays for 1 second.
   - **Example**: `sendSkillStr("kchr", 1)`

9. **Check Around**: `kck`
   - **Description**: Makes the robot check its surroundings and delays for 1 second.
   - **Example**: `sendSkillStr("kck", 1)`

10. **Dig**: `kdg`
    - **Description**: Makes the robot dig and delays for 1 second.
    - **Example**: `sendSkillStr("kdg", 1)`

11. **Stand on Hands**: `khds`
    - **Description**: Makes the robot stand on its hands and delays for 1 second.
    - **Example**: `sendSkillStr("khds", 1)`

12. **Hug**: `khg`
    - **Description**: Makes the robot give a hug and delays for 1 second.
    - **Example**: `sendSkillStr("khg", 1)`

13. **Hi**: `khi`
    - **Description**: Makes the robot wave hello and delays for 1 second.
    - **Example**: `sendSkillStr("khi", 1)`

14. **Hands Up**: `khu`
    - **Description**: Makes the robot raise its hands and delays for 1 second.
    - **Example**: `sendSkillStr("khu", 1)`

15. **Jump**: `kjmp`
    - **Description**: Makes the robot jump and delays for 1 second.
    - **Example**: `sendSkillStr("kjmp", 1)`

16. **Kick**: `kkc`
    - **Description**: Makes the robot kick and delays for 1 second.
    - **Example**: `sendSkillStr("kkc", 1)`

17. **Nod**: `knd`
    - **Description**: Makes the robot nod and delays for 1 second.
    - **Example**: `sendSkillStr("knd", 1)`

18. **Play Dead**: `kpd`
    - **Description**: Makes the robot play dead and delays for 1 second.
    - **Example**: `sendSkillStr("kpd", 1)`

19. **Pee**: `kpee`
    - **Description**: Makes the robot simulate peeing and delays for 1 second.
    - **Example**: `sendSkillStr("kpee", 1)`

20. **Push Up**: `kpu`
    - **Description**: Makes the robot do push-ups and delays for 1 second.
    - **Example**: `sendSkillStr("kpu", 1)`

21. **Scratch**: `kscrh`
    - **Description**: Makes the robot scratch and delays for 1 second.
    - **Example**: `sendSkillStr("kscrh", 1)`

22. **Sniff**: `ksnf`
    - **Description**: Makes the robot sniff and delays for 1 second.
    - **Example**: `sendSkillStr("ksnf", 1)`

23. **Stepping**: `kvtF`
    - **Description**: Makes the robot perform a stepping movement and delays for 1 second.
    - **Example**: `sendSkillStr("kvtF", 1)`

24. **Crawl Forward**: `kcrF`
    - **Description**: Makes the robot crawl forward and delays for 1 second.
    - **Example**: `sendSkillStr("kcrF", 1)`

25. **Crawl Left**: `kcrL`
    - **Description**: Makes the robot crawl to the left and delays for 1 second.
    - **Example**: `sendSkillStr("kcrL", 1)`

26. **Crawl Right**: `kcrR`
    - **Description**: Makes the robot crawl to the right and delays for 1 second.
    - **Example**: `sendSkillStr("kcrR", 1)`

27. **Push Forward**: `kphF`
    - **Description**: Makes the robot push forward and delays for 1 second.
    - **Example**: `sendSkillStr("kphF", 1)`

28. **Push Left**: `kphL`
    - **Description**: Makes the robot push to the left and delays for 1 second.
    - **Example**: `sendSkillStr("kphL", 1)`

29. **Push Right**: `kphR`
    - **Description**: Makes the robot push to the right and delays for 1 second.
    - **Example**: `sendSkillStr("kphR", 1)`

30. **Walk Forward**: `kwkF`
    - **Description**: Makes the robot walk forward and delays for 1 second.
    - **Example**: `sendSkillStr("kwkF", 1)`

31. **Walk Left**: `kwkL`
    - **Description**: Makes the robot walk to the left and delays for 1 second.
    - **Example**: `sendSkillStr("kwkL", 1)`

32. **Walk Right**: `kwkR`
    - **Description**: Makes the robot walk to the right and delays for 1 second.
    - **Example**: `sendSkillStr("kwkR", 1)`

33. **Back**: `kbk`
    - **Description**: Makes the robot move backward and delays for 1 second.
    - **Example**: `sendSkillStr("kbk", 1)`

34. **Back Left**: `kbkL`
    - **Description**: Makes the robot move backward to the left and delays for 1 second.
    - **Example**: `sendSkillStr("kbkL", 1)`

35. **Back Right**: `kbkR`
    - **Description**: Makes the robot move backward to the right and delays for 1 second.
    - **Example**: `sendSkillStr("kbkR", 1)`

36. **Trot Forward**: `ktrF`
    - **Description**: Makes the robot trot forward and delays for 1 second.
    - **Example**: `sendSkillStr("ktrF", 1)`

37. **Trot Left**: `ktrL`
    - **Description**: Makes the robot trot to the left and delays for 1 second.
    - **Example**: `sendSkillStr("ktrL", 1)`

38. **Trot Right**: `ktrR`
    - **Description**: Makes the robot trot to the right and delays for 1 second.
    - **Example**: `sendSkillStr("ktrR", 1)`

39. **Back Flip**: `kbf`
    - **Description**: Makes the robot perform a backflip and delays for 1 second.
    - **Example**: `sendSkillStr("kbf", 1)`

40. **Front Flip**: `kff`
    - **Description**: Makes the robot perform a front flip and delays for 1 second.
    - **Example**: `sendSkillStr("kff", 1)`

41. **Balance**: `kbalance`
    - **Description**: Makes the robot stand up neutral and delays for 1 second.
    - **Example**: `sendSkillStr("kbalance", 1)`

42. **Bound Forward**: `kbdF`
    - **Description**: Makes the robot bound forward and delays for 1 second.
    - **Example**: `sendSkillStr("kbdF", 1)`

43. **Angry**: `kang`
    - **Description**: Makes the robot display an angry stance and delays for 1 second.
    - **Example**: `sendSkillStr("kang", 1)`

44. **Spin Left**: `kvtL`
    - **Description**: Makes the robot spin to the left and delays for 1 second.
    - **Example**: `sendSkillStr("kvtL", 1)`

45. **Moon Walk**: `kmw`
    - **Description**: Makes the robot perform the moonwalk and delays for 1 second.
    - **Example**: `sendSkillStr("kmw", 1)`

46. **Recover**: `krc`
    - **Description**: Makes the robot recover from a fall and delays for 1 second.
    - **Example**: `sendSkillStr("krc", 1)`

47. **Roll**: `krl`
    - **Description**: Makes the robot roll and delays for 1 second.
    - **Example**: `sendSkillStr("krl", 1)`

48. **Be Table**: `ktbl`
    - **Description**: Makes the robot assume a "table" position and delays for 1 second.
    - **Example**: `sendSkillStr("ktbl", 1)`

49. **Wave Head**: `kwh`
    - **Description**: Makes the robot wave its head and delays for 1 second.
    - **Example**: `sendSkillStr("kwh", 1)`

50. **Test**: `kts`
    - **Description**: Puts the robot in test mode and delays for 1 second.
    - **Example**: `sendSkillStr("kts", 1)`
