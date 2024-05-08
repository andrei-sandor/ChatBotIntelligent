import discord
import os
import openai
import pandas as pd
from replit import db
from courseoutlineparser import *
import pandas
import joblib


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


OPENAI_KEY = os.getenv('OPENAI_KEY')

# Set up the OpenAI API client
openai.api_key = OPENAI_KEY

global gradesSpreadsheet

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith("GPT Please"):
        # Use the OpenAI API to generate a response to the message
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"{message.content}",
            max_tokens=2048,
            temperature=0.5,
        )

    list_course_outline = []
    if message.content.contains("Course Outline"):
        list_course_outline = ["Tutorial", "Lecture", "Week1", "Week2", "Week3","Week 4", "Week5", "Week6", "Week7", "Week8"]
        messgage_to_analyze = message.content
        if list_course_outline in messgage_to_analyze:
            for item in list_course_outline:
                if item in messgage_to_analyze:
                    await message.channel.send("Outline.pdf",1,item)
    if message.content.startswith("Give me more info on the course outline"):
        result = give_page_from_info(message)
        if result == "p1":
            await message.channel.send("See here for page 1")
            await message.send_file(open("p1Outline.pdf"))
        if result == "p2":
            await message.channel.send("See here for page 2")
            await message.send_file(open("p2Outline.pdf"))
        if result == "p4":
            await message.channel.send("See here for page 4")
            await message.send_file(open("p4Outline.pdf"))

    if message.author == client.administrator:
        if message.content.contains("Admin username"):
            admin_username = message.content[2]
            admin_password = message.content[5]


            if encrypted(admin_password):
                if message.content.contains("Course Outline"):
                    await message.channel.send("Here is the outline!")
                    await message.send_file(open("Outline.pdf"))

                if message.content.contains("Assignment1"):
                    await message.channel.send("Here is A1")
                    await message.send_file(open("A1.pdf"))


                if message.content.contains("Assignment2"):
                    await message.channel.send("Here is A2")
                    await message.send_file(open("A2.pdf"))

    if message.author == client.administrator:
        if message.content.contains("Please enter your grades"):
            gradesSpreadsheet = pd.read_csv("gradesSpreadsheet.csv")

    if message.content.startswith("260111111 Exam1"):
        gradesSpreadsheet["260111111"].loc["Exam1"] = message.content[2]
        model = joblib.load('model_dnn2_grade1.joblib')
        prediction = model.predict([message.content[2]])
        await message.channel.send("Your predicted final grade is " + prediction)

        grade_for_a = 85 - (int(message.content[2])) * 0.25
        grade_for_pass = 55 - (int(message.content[2])) * 0.25

        await message.channel.send("You need " + grade_for_a + "to get an A")
        await message.channel.send("You need " + grade_for_pass + "to pass")

    if message.content.startswith("260111111 Exam2"):
        gradesSpreadsheet["260111111"].loc["Exam2"] = message.content[2]
        model = joblib.load('model_dnn2_grade2.joblib')
        prediction = model.predict([message.content[2]])
        await message.channel.send("Your predicted final grade is " + prediction)

        grade_for_a = 85 - (int(message.content[2])) * 0.25 - (int (gradesSpreadsheet['260111111'].iloc['Exam1'])) * 0.25
        grade_for_pass = 55 - (int(message.content[2])) * 0.25 - (int (gradesSpreadsheet['260111111'].iloc['Exam1'])) * 0.25

        await message.channel.send("You need " + grade_for_a + "to get an A")
        await message.channel.send("You need " + grade_for_pass + "to pass")

    if message.content.startswith("260111111 Exam3"):
        gradesSpreadsheet["260111111"].loc["Exam3"] = message.content[2]

        grade = (int(message.content[2])) * 0.50 + (int(gradesSpreadsheet['260111111'].iloc['Exam1'])) * 0.25 + (int(gradesSpreadsheet['260111111'].iloc['Exam2'])) * 0.25
        await message.channel.send("Your final grade is " + grade)

    if message.content.startswith("260222222 Exam1"):
        gradesSpreadsheet["260222222"].loc["Exam1"] = message.content[2]
        model = joblib.load('model_dnn2_grade1.joblib')
        prediction = model.predict([message.content[2]])
        await message.channel.send("Your predicted final grade is " + prediction)

        grade_for_a = 85 - (int(message.content[2])) * 0.25
        grade_for_pass = 55 - (int(message.content[2])) * 0.25

        await message.channel.send("You need " + grade_for_a + "to get an A")
        await message.channel.send("You need " + grade_for_pass + "to pass")

    if message.content.startswith("260222222 Exam2"):
        gradesSpreadsheet["260222222"].loc["Exam2"] = message.content[2]
        model = joblib.load('model_dnn2_grade2.joblib')
        prediction = model.predict([message.content[2]])
        await message.channel.send("Your predicted final grade is " + prediction)

        grade_for_a = 85 - (int(message.content[2])) * 0.25 - (int (gradesSpreadsheet['260222222'].iloc['Exam1'])) * 0.25
        grade_for_pass = 55 - (int(message.content[2])) * 0.25 - (int (gradesSpreadsheet['260222222'].iloc['Exam1'])) * 0.25

        await message.channel.send("You need " + grade_for_a + "to get an A")
        await message.channel.send("You need " + grade_for_pass + "to pass")

    if message.content.startswith("260222222 Exam3"):
        gradesSpreadsheet["260222222"].loc["Exam3"] = message.content[2]

        grade = (int(message.content[2])) * 0.50 + (int(gradesSpreadsheet['260222222'].iloc['Exam1'])) * 0.25 + (int(gradesSpreadsheet['260222222'].iloc['Exam2'])) * 0.25
        await message.channel.send("Your final grade is " + grade)




client.run("MTIzNzIxMjg4MDg1NjgwOTU3Mw.GKn6mL.G3QTQpZS4r5OHx7SPGGJSFqGBK-rhJrRmuGgBk")