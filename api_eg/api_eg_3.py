from tkinter import*
import requests
root = Tk()
root.title('Weather Details')
root.geometry('400x200')

def s():

    api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=3b38f7256941d04dc249f965f535ca29&q='
    city = cityv.get()
    url = api_address + city
    print(url)
    json_data = requests.get(url).json()
    print(json_data)
    format_add = json_data['weather'][0]['main']
    format_add2 = json_data['coord']['lon']
    format_add3 = json_data['coord']['lat']
    print(format_add3,format_add2,format_add)
    c.set(format_add3)
    b.set(format_add2)
    a.set(format_add)





Label(root, text="city").grid(row=0, column=0)

cityv = StringVar()
Entry(root, textvariable=cityv).grid(row=0, column=1)

Button(root, text="submit",command=s).grid(row=0, column=2)


Label(root, text="lat").grid(row=1, column=0)
c = StringVar()
Entry(root, textvariable=c).grid(row=1, column=1)

Label(root, text="lon").grid(row=2, column=0)
b = StringVar()
Entry(root, textvariable=b).grid(row=2, column=1)

Label(root, text="weather").grid(row=3, column=0)
a = StringVar()
Entry(root, textvariable=a).grid(row=3, column=1)


root.mainloop()
