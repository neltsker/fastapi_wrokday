#Random module for randomly accepting the values
# ‘X’ indicates the ships hit
# ‘-‘ indicates the hits missed
from random import randint

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse

app = FastAPI()
html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <h2>Your ID: <span id="ws-id"></span></h2>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var client_id = Date.now()
            document.querySelector("#ws-id").textContent = client_id;
            var ws = new WebSocket(`ws://localhost:8000/ws/${client_id}`);
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""


class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        if len(self.active_connections)>2:
            pass
            #await websocket.
        else:
            await websocket.accept()
            self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)


manager = ConnectionManager()


@app.get("/")
async def get():
    return HTMLResponse(html)


@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_personal_message(f"You wrote: {data}", websocket)
            await manager.broadcast(f"Client #{client_id} says: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client #{client_id} left the chat")



Hidden_Pattern=[[' ']*8 for x in range(8)]
Guess_Pattern=[[' ']*8 for x in range(8)]

let_to_num={'A':0,'B':1, 'C':2,'D':3,'E':4,'F':5,'G':6,'H':7}

def print_board(board):
    print(' A B C D E F G H')
    print(' ***************')
    manager.send_personal_message(' A B C D E F G H')
    manager.send_personal_message(' ***************')
    row_num=1
    for row in board:
        print("%d|%s|" % (row_num, "|".join(row)))
        manager.send_personal_message("%d|%s|" % (row_num, "|".join(row)))
        row_num +=1

def get_ship_location():
    #Enter the row number between 1 to 8
    row=input('Please enter a ship row 1-8 ').upper()
    while row not in '12345678':
        print("Please enter a valid row ")
        row=input('Please enter a ship row 1-8 ')
    #Enter the Ship column from A TO H
    column=input('Please enter a ship column A-H ').upper()
    while column not in 'ABCDEFGH':
        print("Please enter a valid column ")
        column=input('Please enter a ship column A-H ')
    return int(row)-1,let_to_num[column]

#Function that creates the ships
def create_ships(board):
    for ship in range(5):
        ship_r, ship_cl=randint(0,7), randint(0,7)
        while board[ship_r][ship_cl] =='X':
            ship_r, ship_cl = randint(0, 7), randint(0, 7)
        board[ship_r][ship_cl] = 'X'



def count_hit_ships(board):
    count=0
    for row in board:
        for column in row:
            if column=='X':
                count+=1
    return count

create_ships(Hidden_Pattern)
#print_board(Hidden_Pattern)
turns = 10
while turns > 0:
    print('Welcome to Battleship')
    print_board(Guess_Pattern)
    row,column =get_ship_location()
    if Guess_Pattern[row][column] == '-':
        print(' You already guessed that ')
    elif Hidden_Pattern[row][column] =='X':
        print(' Congratulations you have hit the battleship ')
        Guess_Pattern[row][column] = 'X'
        turns -= 1
    else:
        print('Sorry,You missed')
        Guess_Pattern[row][column] = '-'
        turns -= 1
    if  count_hit_ships(Guess_Pattern) == 5:
        print("Congratulations you have sunk all the battleships ")
        break
    print(' You have ' +str(turns) + ' turns remaining ')
    if turns == 0:
        print('Game Over ')
        break