#10章webAPIのコードは、拠点関係のAPIを作ったマンなので省略
#でも気になるのでコピペして挙動だけ見たいやつ

import requests, json, turtle
#requestsなんてモジュールはないと怒られる
#調べてもよくわからんので誰かに聞く

iss = turtle.Turtle()

def setup(window):
    global iss

    window.setup(1000,500)
    window.bgpic('earth.gif')
    window.setworldcoordinates(-180, -90, 180, 90)
    turtle.register_shape("iss.gif")
    iss.shape("iss.gif")

def move_iss(lat, long):
    global iss

    iss.penup()
    iss.goto(long, lat)
    iss.pendown()

def track_iss():
    url = 'http://api.open-notify.org/iss-now.json'
    response = requests.get(url)
    if response.status_code == 200:
        response_dictionary = json.loads(response.text)
        position = response_dictionary['iss_position']
        lat = float(position['latitude'])
        long = float(position['longitude'])
        move_iss(lat, long)
    else:
        print("Houston, we have a problem:", response.status_code)
    widget = turtle.getcanvas()
    widget.after(5000, track_iss)

def main():
    global iss
    screen = turtle.Screen()
    setup(screen)
    track_iss()

if __name__ == "__main__":
    main()
    turtle.mainloop()                     
