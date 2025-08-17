# from pyfiglet import Figlet
# import random
# string=input("Enter Name/text: ")
# x=Figlet()
# z=x.getFonts()
# while True:
#     try:
#             choice=int(input("""Press '1' to Print & Download it in a Random Font.
# Press '2' to Print & Download it by Selecting a Font
#                                                         Pressing: """).strip())
#             if choice==1:     
#                    random_font=random.choice(z)
#                    x.setFont(font=random_font)
#                    print("Font= ",random_font)
#                    print()
#                    print(x.renderText(string))
#                    break
#             elif choice==2:
#                     for f in z:
#                           i=1
#                           x.setFont(font=f)
#                           print(i,f"Font Name={f}")
#                           print()
#                           print(f"{x.renderText(string)}")
#                     Select_font=input("Enter the Name of the font you want to Print & Download your text in: ")
#                     if Select_font in z:
#                            print(x.renderText(string))
#                     break       
#     except: 
#             print("Incorrect Value Entered. Please enter an expected value")

# from pyfiglet import Figlet
# import random
# import os

# string=input("Enter Name/text: ")
# x=Figlet()
# z=x.getFonts()

# while True:
#     try:
#         choice=int(input("""Press '1' to Print & Download it in a Random Font.
# Press '2' to Print & Download it by Selecting a Font
#                                                         Pressing: """).strip())
#         if choice==1:     
#             random_font=random.choice(z)
#             x.setFont(font=random_font)
#             print("Font= ",random_font)
#             print()
#             art = x.renderText(string)
#             print(art)
#             # 🔹 Save to file
#             with open(f"{string}_{random_font}.txt", "w", encoding="utf-8") as f:
#                 f.write(art)
#             print(f"✅ Saved as {os.path.abspath(string+'_'+random_font+'.txt')}")
#             break

#         elif choice==2:
#             i=1
#             for f in z:
#                 x.setFont(font=f)
#                 print(i,f"Font Name={f}")
#                 print()
#                 print(f"{x.renderText(string)}")
#                 i+=1
#             Select_font=input("Enter the Name of the font you want to Print & Download your text in: ")
#             if Select_font in z:
#                 x.setFont(font=Select_font)
#                 art = x.renderText(string)
#                 print(art)
#                 # 🔹 Save to file
#                 with open(f"{string}_{Select_font}.txt", "w", encoding="utf-8") as f:
#                     f.write(art)
#                 print(f"✅ Saved as {os.path.abspath(string+'_'+Select_font+'.txt')}")
#             break       

#     except: 
#         print("Incorrect Value Entered. Please enter an expected value")

# import streamlit as st
# from pyfiglet import Figlet
# import random

# string = st.text_input("Enter Name/text: ")
# x = Figlet()
# z = x.getFonts()

# choice = st.radio(
#     """Press '1' to Print & Download it in a Random Font.
# Press '2' to Print & Download it by Selecting a Font""",
#     (1, 2)
# )

# if string:  # only run when user enters text
#     try:
#         if choice == 1:     
#             random_font = random.choice(z)
#             x.setFont(font=random_font)
#             st.write("Font= ", random_font)
#             st.write("")
#             art = x.renderText(string)
#             st.text(art)

#             # download button
#             st.download_button(
#                 label="Download ASCII Art",
#                 data=art,
#                 file_name=f"{string}_{random_font}.txt",
#                 mime="text/plain"
#             )

#         elif choice == 2:
#             i = 1
#             for f in z:
#                 x.setFont(font=f)
#                 st.write(i, f"Font Name = {f}")
#                 st.text(x.renderText(string))
#                 i += 1

#             Select_font = st.selectbox(
#                 "Enter the Name of the font you want to Print & Download your text in:", 
#                 z
#             )
#             if Select_font in z:
#                 x.setFont(font=Select_font)
#                 art = x.renderText(string)
#                 st.text(art)

#                 # download button
#                 st.download_button(
#                     label="Download ASCII Art",
#                     data=art,
#                     file_name=f"{string}_{Select_font}.txt",
#                     mime="text/plain"
#                 )
#     except Exception as e:
#         st.error("Incorrect Value Entered. Please enter an expected value.")
import streamlit as st
from pyfiglet import Figlet
import random
import cowsay
st.title("🎨 PyFiglet ASCII Art Generator")
string = st.text_input("Enter Name/Text:")

# Create Figlet instance
x = Figlet()
z = x.getFonts()

choice = st.radio(
    "Choose how to generate ASCII art:",
    ["Press 'R' for Random Font", "'S' to Select Font of your own Choice"]
)

if string: 
    try:
        if choice == "R" or choice=="r":
            if st.button("Generate Random"):
                random_font = random.choice(z)
                x.setFont(font=random_font)
                art = x.renderText(string)

                st.write(f"Font used: **{random_font}**")
                st.text(art)

                # download button
                st.download_button(
                    label="Download ASCII Art",
                    data=art,
                    file_name=f"{string}_{random_font}.txt",
                    mime="text/plain"
                )

        elif choice == "S" or choice=="s":

            Select_font = st.selectbox("Pick a font:", z)

            if st.button("Generate Selected"):
                x.setFont(font=Select_font)
                art = x.renderText(string)
                st.text(art)

                # download button
                st.download_button(
                    label="Download ASCII Art",
                    data=art,
                    file_name=f"{string}_{Select_font}.txt",
                    mime="text/plain"
                )

    except Exception as e:
        st.error(f"Error: {e}")

 