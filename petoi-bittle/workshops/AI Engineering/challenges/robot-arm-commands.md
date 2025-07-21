# Robot Arm Commands - Quick Reference

⚠️ **Safety**: Never put hands between robot claws when arm is moving!

## Basic Commands

| Pick Up Objects | Put Down Objects | Movement Control |
|---|---|---|
| "pick up object in front" | "put it down in front" | "turn left" (AI sends +angle) |
| "grab something to your left" | "place it to your left" | "rotate right" (AI sends -angle) |
| "pick up object underneath" | "drop it" (opens gripper) | "raise arm up" / "lower arm down" |

## Precision & Special Actions

| Movement Size | Speed Control | Special Actions |
|---|---|---|
| **Small**: "slightly", "a bit" | "slowly turn left" | "hunt for object" |
| **Medium**: "some", "more" | "quickly close gripper" | "show what you're holding" |
| **Large**: "a lot", "much more" | "smoothly sweep right" | "throw it forward" |
| **Maximum**: "all the way", "extreme" | | "grip tighter" |

**Joint Ranges**: Base -125° to +125° (250°) • Shoulder -90° to +120° (210°) • Gripper -60° to +120° (180°)

## Multi-Step Commands & Challenge

**Combine Actions**: "walk forward, pick up object, turn right, put it down" • "turn left, grab red ball, walk back, place it here"

**Mission**: Find object → Navigate → Pick up → Move → Put down **Pro Goal**: Do it all with ONE complex prompt!

## Advanced Examples & Troubleshooting

| Extreme Positions | Complex Sequences | Troubleshooting |
|---|---|---|
| "arm straight up above head" | "scan room left to right slowly" | **No response?** Check "Robot Arm DETECTED" |
| "rotate all the way left" | "victory dance with arm" | **Wrong object?** Try lighter items |
| "maximum grip strength" | "test full range of motion" | **Still stuck?** Say "calibrate gripper" |
| "sweep entire area" | "carefully approach from above" | |
