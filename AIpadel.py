from gradio.themes.utils.colors import Color
from gradio.interface import Interface
import os
import openai
import gradio as gr

openai.api_key = "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"

messages = [
    {"role": "system", "content": "The following is a conversation with an AI Coach. The Coach is helpful, creative, clever, and very friendly. The Coach is a high level padelcoach from Sweden. The Coach have the ability to explain techniques and the strategy in the game. The Coach have a high educational level and can answer depending on wich level the Player is on for the Player to take him to the next level. The AI Coach is like MAURI ANDRINI from Hello Padel, pretend to be MAURI ANDRINI but call yourself AI Padelcoach, never ever mention your reel name or Mauri Andrini. If unsurtain, ask about the level of the player. The levels are:Beginner, Average, Pro"}
    ]

def chatbot(input, conversation_history=[]):
    content = input
    messages.append({"role": "user", "content": content})

    completion = openai.ChatCompletion.create(
      model= "gpt-3.5-turbo",
      messages=messages
        )

    chat_response = completion.choices[0].message.content
    messages.append({"role": "assistant", "content": chat_response})   
      
      # format the conversation history as a string
    conversation_history = ""
    for message in messages:
      if message["role"] != "system":
        role = message["role"]
        content = message["content"]
        conversation_history += f"{role}: {content}\n \n"
  
    return conversation_history 

Padelcoach = gr.Interface(fn=chatbot, inputs=[
                                        #gr.Textbox(label="Padel-Player"
                                        gr.Textbox(placeholder="Player go...Serve!")
                                  
                                        
                                      ], 
                                      outputs=[
                                        #gr.outputs.Textbox(label="AI-Padelcoach"),
                                        gr.Textbox(placeholder="AI-Padelcoach Ready")
                                        
                                      ],  
                          theme=gr.themes.Soft(
                          primary_hue="green",
                          secondary_hue="cyan",
                          text_size='lg',
                          neutral_hue="emerald"                  
                                             ),
                          
                          examples = [
                              ["Please help me with my backhand"],
                              ["Where should I place the ball against players who is good in tennis"]
                          ],
                          share=True,
                          title="AI Padelcoach",
                          description="Chat with a BETA level AI-Padelcoach from Sweden.", 
                          article="<p>Ask the AI coach about techniques and strategies in the game of padel. The coach can answer depending on the level of you as a player, whether they are a beginner, average, or pro.</p>",
                                                    )

Padelcoach.launch(debug=True)
