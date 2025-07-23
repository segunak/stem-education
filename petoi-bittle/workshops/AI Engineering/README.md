# AI Engineering Workshop

## 🚀 How to Start

1. **Open VS Code** and navigate to the `challenges` folder
2. **Start with Challenge 1**: Open `challenge-1-commands.py`
3. **Read the instructions** at the top of the file
4. **Run the file** by clicking the ▶️ play button in VS Code
5. **Complete the challenge** by following the hints
6. **Move to the next challenge** when done!

## 📁 Folder Structure

```text
AI Engineering/
├── challenges/           ← YOUR WORKSPACE (edit these files!)
│   ├── challenge-1-commands.py
│   ├── challenge-2-transparency.py
│   ├── challenge-3-sequences.py
│   ├── challenge-4-rag.py
│   ├── challenge-5-robot-arm.py (OPTIONAL - requires arm)
│   ├── robot-dog-commands.md
│   └── robot-arm-commands.md
└── lib/                 ← SYSTEM FILES (don't edit these)
    ├── robot_controller.py
    ├── PetoiRobot.py
    ├── ardSerial.py
    ├── SerialCommunication.py
    ├── config.py
    └── requirements.txt
```

## 🎯 Learning Journey

**Challenge 1**: Learn how AI gets smarter through context by teaching it robot commands

**Challenge 2**: Understand responsible AI by making the system transparent

**Challenge 3**: Create complex behaviors using command sequences

**Challenge 4**: Implement RAG (Retrieval Augmented Generation) with live API data

**Challenge 5** (OPTIONAL): Master robot arm control through natural language - requires [Bittle X+Arm model](https://www.petoi.com/products/petoi-robot-dog-bittle-x-voice-controlled?variant=49985955791160)

## 💡 Tips

- **Use GitHub Copilot**: Click the Copilot button in VS Code (upper right)
- **Ask for help**: Your instructor is there to support you
- **Experiment**: Try different commands and see what happens
- **Have fun**: This is about learning and exploring AI!

## 🔧 Setup Required

- **OpenAI API key**: Create a `.env` file in the `lib` folder with `OPENAI_API_KEY=your_key_here`
- **Robot dog**: Connected via USB or Bluetooth
- **Python environment**: With required packages installed

**Important**: The `.env` file must be in the `lib` folder, not the `challenges` folder!

Ask your instructor for help with setup!

## 🦾 Optional Robot Arm Challenge

If your robot has an arm attachment, you can try Challenge 5! This challenge teaches you how to control complex hardware through natural language and good documentation reading. No code changes needed, just expert prompting skills!
