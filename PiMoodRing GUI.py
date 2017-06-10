from guizero import App, PushButton, TextBox, Text
from moodring import sentiment_search
from moodring_display import mood_ring, mood_clear

mood_clear()

app = App(title="Pi Mood Ring", height=800, width=1000, layout="auto", bgcolor="#42e2f4")


message = Text(app, text="Welcome to Pi Mood Ring.")
message = Text(app, text="You can use Pi Mood Ring to guage the mood of specific places, events, topics, or phrases on Twitter.")
message = Text(app, text="Attach a Raspberry Pi Sense HAT and you're ready to go!")
message = Text(app, text="Please type the hashtag, location, or topic that you would like to search.")

input_box = TextBox(app, width=40)



def button_push():
    #print("button pushed")
    search_term = input_box.get()
    message = Text(app, text=search_term) 
    mood_num = sentiment_search(search_term)
    message = Text(app, text=mood_num)
    mood_ring(mood_num)
    input_box.set("")
    
button = PushButton(app, command=button_push, text="Search")

message = Text(app, text="The number below represents the positivity or negativity of the language of Tweets that contain your search term. \n -1 being the most negative and 1 being the most positive")
message = Text(app, text="On the sense HAT, green indicates positive and red indicates negative. \n The size of the square indicates intensity.")
message = Text(app, text="") 

app.display()



