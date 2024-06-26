import turtle as t
import time

def afficher(st):
    t.clear() 
    t.goto(0, -t.window_height() / 2 + 20)
    t.write(st, align="center", font=("Arial", 16, "normal"))
    time.sleep(3)

sts = [
        "It might seem crazy what I'm 'bout to say", # [Couplet 1]
        "Sunshine she's here, you can take a break",
        "I'm a hot air balloon that could go to space",
        "With the air, like I don't care, baby, by the way",
        "(Because I'm happy)", # [Refrain]
        "Clap along if you feel like a room without a roof",
        "(Because I'm happy)",
        "Clap along if you feel like happiness is the truth",
        "(Because I'm happy)",
        "Clap along if you know what happiness is to you",
        "(Because I'm happy)",
        "Clap along if you feel like that's what you wanna do",
        "Here come bad news, talking this", # [Couplet 2]
        "and that (Yeah!)",
        "Well, give me all you got, don't",
        "hold it back (Yeah!)",
        "Well, I should probably warn ya,",
        "I'll be just fine (Yeah!)",
        "No offense to you, don’t waste your time, here's why",
        "(Because I'm happy)", # [Refrain]
        "Clap along if you feel like a room without a roof",
        "(Because I'm happy)",
        "Clap along if you feel like happiness is the truth",
        "(Because I'm happy)",
        "Clap along if you know what happiness is to you",
        "(Because I'm happy)",
        "Clap along if you feel like that's what you wanna do",
        "Bring me down", # [Pont]
        "Can't nothing bring me down",
        "My level's too high to bring me down",
        "Can't nothing bring me down, I said",
        "Bring me down",
        "Can't nothing bring me down",
        "My level's too high to bring me down",
        "Can't nothing bring me down, I said",
        "(Because I'm happy)", # [Refrain]
        "Clap along if you feel like a room without a roof",
        "(Because I'm happy)",
        "Clap along if you feel like happiness is the truth",
        "(Because I'm happy)",
        "Clap along if you know what happiness is to you",
        "(Because I'm happy)",
        "Clap along if you feel like that's what you wanna do",
        "(Because I'm happy)",
        "Clap along if you feel like a room without a roof",
        "(Because I'm happy)",
        "Clap along if you feel like happiness is the truth",
        "(Because I'm happy)",
        "Clap along if you know what happiness is to you",
        "(Because I'm happy)",
        "Clap along if you feel like that's what you wanna do",
        "Bring me down", # [Pont]
        "Can't nothing bring me down",
        "My level's too high to bring me down",
        "Can't nothing bring me down, I said...",
        "(Because I'm happy)", # [Refrain]
        "Clap along if you feel like a room without a roof",
        "(Because I'm happy)",
        "Clap along if you feel like happiness is the truth",
        "(Because I'm happy)",
        "Clap along if you know what happiness is to you",
        "(Because I'm happy)",
        "Clap along if you feel like that's what you wanna do",
        "(Because I'm happy)",
        "Clap along if you feel like a room without a roof",
        "(Because I'm happy)",
        "Clap along if you feel like happiness is the truth",
        "(Because I'm happy)",
        "Clap along if you know what happiness is to you",
        "(Because I'm happy)",
        "Clap along if you feel like that's what you wanna do (Come on)", ]
def st_settings():
    t.speed(1)
    t.bgcolor("black")
    t.color("white")
    t.hideturtle()
    t.penup()
def subtitles():
    st_settings()
    for st in sts:
        afficher(st)