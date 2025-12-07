# wheelbot_agent.py (runs on a NEW Pi)

from uagents import Agent, Context, Model
import RPi.GPIO as GPIO
import asyncio

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
# CONFIGURATION (CHANGE THESE)
# -------------------------------
NEW_PI_IP = "10.64.173.150"  # ← change to NEW Pi IP

agent = Agent(
    name="wheelbot_agent",          # ← unique name
    seed="wheelbot_agent_seed",     # ← unique seed
    port=8003,                      # ← new port NOT used elsewhere
    endpoint=[f"http://{NEW_PI_IP}:8003/submit"]
)


# -------------------------------
# GPIO Setup
# -------------------------------
GPIO.setmode(GPIO.BCM)

LEFT_FWD  = 5
LEFT_BWD  = 6
RIGHT_FWD = 13
RIGHT_BWD = 19

motor_pins = [LEFT_FWD, LEFT_BWD, RIGHT_FWD, RIGHT_BWD]
for p in motor_pins:
    GPIO.setup(p, GPIO.OUT)
    GPIO.output(p, GPIO.LOW)

position = [0, 0]


# -------------------------------
# Movement Helpers
# -------------------------------
def stop():
    for p in motor_pins:
        GPIO.output(p, GPIO.LOW)

def forward():
    GPIO.output(LEFT_FWD, 1)
    GPIO.output(RIGHT_FWD, 1)

def backward():
    GPIO.output(LEFT_BWD, 1)
    GPIO.output(RIGHT_BWD, 1)

def left_turn():
    GPIO.output(LEFT_BWD, 1)
    GPIO.output(RIGHT_FWD, 1)

def right_turn():
    GPIO.output(LEFT_FWD, 1)
    GPIO.output(RIGHT_BWD, 1)


# -------------------------------
# Message Handler
# -------------------------------
@agent.on_message(model=Command)
async def handle_command(ctx: Context, sender: str, msg: Command):

    old_pos = position.copy()

    if msg.direction == "FRONT":
        forward()
    elif msg.direction == "BACK":
        backward()
    elif msg.direction == "LEFT":
        left_turn()
    elif msg.direction == "RIGHT":
        right_turn()

    # Move for 0.5 seconds
    await asyncio.sleep(0.5)
    stop()

    # fake update for now (depends on wheel odometry)
    if msg.direction == "FRONT":  position[1] += 1
    if msg.direction == "BACK":   position[1] -= 1
    if msg.direction == "LEFT":   position[0] -= 1
    if msg.direction == "RIGHT":  position[0] += 1

    status = Status(old_pos=tuple(old_pos), new_pos=tuple(position), obstacle_type=msg.obstacle_type)
    await ctx.send(sender, status)


# -------------------------------
# Startup
# -------------------------------
@agent.on_event("startup")
async def startup(ctx: Context):
    print("[Wheelbot] Agent ready.")


# -------------------------------
# Run
# -------------------------------
if _name_ == "_main_":
    agent.run()
