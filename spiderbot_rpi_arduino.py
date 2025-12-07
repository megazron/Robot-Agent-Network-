from uagents import Agent, Context, Model
import asyncio
import os

# -------------------------------
# Models
# -------------------------------
class Command(Model):
    direction: str
    reason: str
    obstacle_type: str

class Status(Model):
    old_pos: tuple
    new_pos: tuple
    obstacle_type: str

# -------------------------------
# Configuration
# -------------------------------
COM_PORT = "/dev/ttyACM0"
BAUD_RATE = 9600

# Check if Arduino exists
arduino = None
if os.path.exists(COM_PORT):
    import serial
    arduino = serial.Serial(COM_PORT, BAUD_RATE, timeout=1)
    print(f"Arduino connected on {COM_PORT}")
else:
    print(f"Arduino not connected. Will skip sending commands.")

agent = Agent(
    name="pi_agent",
    seed="pi_agent_seed",
    port=8001
)

bot_pos = [5, 5]

# Map directions to Arduino commands
DIRECTION_MAP = {
    "LEFT": b'A',
    "RIGHT": b'B',
    "FRONT": b'C',
    "BACK": b'D',
}

# -------------------------------
# Handle Commands from Laptop
# -------------------------------
@agent.on_message(model=Command)
async def handle_command(ctx: Context, sender: str, msg: Command):
    global bot_pos

    print(f"Received command: {msg.direction}, Reason: {msg.reason}, Obstacle: {msg.obstacle_type}")

    # Send to Arduino if connected
    if arduino and msg.direction in DIRECTION_MAP:
        arduino.write(DIRECTION_MAP[msg.direction])
        print(f"Sent to Arduino: {DIRECTION_MAP[msg.direction].decode()}")
    elif not arduino:
        print("Arduino not connected; skipping serial send.")

    # Update bot position for simulation
    old_pos = bot_pos.copy()
    if msg.direction == "LEFT":
        bot_pos[0] = max(0, bot_pos[0]-1)
    elif msg.direction == "RIGHT":
        bot_pos[0] = min(9, bot_pos[0]+1)
    elif msg.direction == "FRONT":
        bot_pos[1] = max(0, bot_pos[1]-1)
    elif msg.direction == "BACK":
        bot_pos[1] = min(9, bot_pos[1]+1)

    await ctx.send(sender, Status(old_pos=old_pos, new_pos=bot_pos, obstacle_type=msg.obstacle_type))
    print(f"Updated bot pos: {bot_pos}")

# -------------------------------
# Startup
# -------------------------------
@agent.on_event("startup")
async def startup(ctx: Context):
    print("Pi Agent started and ready!")

# -------------------------------
# Run agent
# -------------------------------
if __name__ == "__main__":
    agent.run()
