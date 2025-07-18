# Informational: Sending Skills to the Robot Dog

## The `sendSkillStr` Function

The `sendSkillStr` function is designed to send a specific skill command to the Petoi Robot, instructing it to perform a predefined action or movement. This function is part of the unified `Petoi` module, which facilitates communication with the robot via serial commands.

## Parameters

- **skillStr** (str): This parameter is a string representing the skill command to be sent to the robot. Each skill corresponds to a specific action or movement that the robot can perform, such as sitting, standing, walking, or performing tricks like flips.
  
- **delayTime** (int): This parameter represents the delay time in seconds after the command is sent. The delay allows for proper execution timing of the skill, ensuring the robot has enough time to complete the action before receiving the next command.

## Function Explanation

The `sendSkillStr` function sends a short skill string command to the robot via serial communication. This function uses the `send` function, which communicates with the robot's serial port, transmitting the skill command string and the specified delay time.

1. **Sending the Command**: The function calls the `send` function, passing the serial ports (`goodPorts`), the skill command string, and the delay time as a list.

2. **Delay Handling**: The delay time ensures that there is a proper interval between consecutive commands, allowing the robot to complete one action before starting another.

## Skills and Their Commands

Here is the comprehensive list of all skills that can be sent using `sendSkillStr`. To use any skill, simply take the **Command** value from the table and put it in the `sendSkillStr` function like this:

```python
sendSkillStr("CHANGE_ME_TO_THE_COMMAND", 1)
```

To use this template, just replace `CHANGE_ME_TO_THE_COMMAND` with any command from the table below. For example:

- To make the robot sit: `sendSkillStr("ksit", 1)`
- To make the robot stand up: `sendSkillStr("kup", 1)`
- To make the robot do a back flip: `sendSkillStr("kbf", 1)`

The number `1` represents the delay time in seconds. This controls how long the system waits after sending the command before it's ready to accept the next command, not how long the robot performs the action. The robot will complete each skill on its own timing.

| **Skill Name** | **Command** | **Description** |
|---|---|---|
| Sit | `ksit` | Makes the robot sit down |
| Stand Up | `kup` | Makes the robot stand up |
| Bottom Up | `kbuttUp` | Raises the robot's bottom |
| Stretch | `kstr` | Stretches the robot |
| Rest | `krest` | Puts the robot in a resting position |
| Zero | `kzero` | Resets the robot to its default position |
| Boxing | `kbx` | Makes the robot perform boxing movements |
| Cheer | `kchr` | Makes the robot cheer |
| Check Around | `kck` | Makes the robot check its surroundings |
| Dig | `kdg` | Makes the robot dig |
| Stand on Hands | `khds` | Makes the robot stand on its hands |
| Hug | `khg` | Makes the robot give a hug |
| Hi | `khi` | Makes the robot wave hello |
| Hands Up | `khu` | Makes the robot raise its hands |
| Jump | `kjmp` | Makes the robot jump |
| Kick | `kkc` | Makes the robot kick |
| Nod | `knd` | Makes the robot nod |
| Play Dead | `kpd` | Makes the robot play dead |
| Pee | `kpee` | Makes the robot simulate peeing |
| Push Up | `kpu` | Makes the robot do push-ups |
| Scratch | `kscrh` | Makes the robot scratch |
| Sniff | `ksnf` | Makes the robot sniff |
| Stepping | `kvtF` | Makes the robot perform a stepping movement |
| Crawl Forward | `kcrF` | Makes the robot crawl forward |
| Crawl Left | `kcrL` | Makes the robot crawl to the left |
| Crawl Right | `kcrR` | Makes the robot crawl to the right |
| Push Forward | `kphF` | Makes the robot push forward |
| Push Left | `kphL` | Makes the robot push to the left |
| Push Right | `kphR` | Makes the robot push to the right |
| Walk Forward | `kwkF` | Makes the robot walk forward |
| Walk Left | `kwkL` | Makes the robot walk to the left |
| Walk Right | `kwkR` | Makes the robot walk to the right |
| Back | `kbk` | Makes the robot move backward |
| Back Left | `kbkL` | Makes the robot move backward to the left |
| Back Right | `kbkR` | Makes the robot move backward to the right |
| Trot Forward | `ktrF` | Makes the robot trot forward |
| Trot Left | `ktrL` | Makes the robot trot to the left |
| Trot Right | `ktrR` | Makes the robot trot to the right |
| Back Flip | `kbf` | Makes the robot perform a backflip |
| Front Flip | `kff` | Makes the robot perform a front flip |
| Balance | `kbalance` | Makes the robot stand up neutral |
| Bound Forward | `kbdF` | Makes the robot bound forward |
| Angry | `kang` | Makes the robot display an angry stance |
| Spin Left | `kvtL` | Makes the robot spin to the left |
| Moon Walk | `kmw` | Makes the robot perform the moonwalk |
| Recover | `krc` | Makes the robot recover from a fall |
| Roll | `krl` | Makes the robot roll |
| Be Table | `ktbl` | Makes the robot assume a "table" position |
| Wave Head | `kwh` | Makes the robot wave its head |
| Test | `kts` | Puts the robot in test mode |
| Calibration | `kcalib` | Puts the robot in calibration pose |
| Dropped | `kdropped` | Makes the robot assume dropped position (dropped by back legs) |
| Lifted | `klifted` | Makes the robot assume lifted position (lifted by neck) |
| Landing | `klnd` | Makes the robot assume landing pose |
| Jump Forward | `kjpF` | Makes the robot jump forward |
| Hand Shake | `khsk` | Makes the robot shake hands |
| Push Up One Hand | `kpu1` | Makes the robot do push-ups with one hand |
| High Five | `kfiv` | Makes the robot give a high five |
| Good Boy | `kgdb` | Makes the robot perform good boy behavior |
